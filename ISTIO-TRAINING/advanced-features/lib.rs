

use log::info;
use proxy_wasm::traits::*;
use proxy_wasm::types::*;
use serde::Deserialize;

// 1. Define a struct to store custom header configurations
#[derive(Deserialize, Default, Clone)]
struct PluginConfig {
    header_1: String,
    header_2: String,
}

proxy_wasm::main! {{
    proxy_wasm::set_log_level(LogLevel::Trace);
    proxy_wasm::set_root_context(|_| -> Box<dyn RootContext> {
        Box::new(HttpHeadersRoot::default())
    });
}}

#[derive(Default)]
struct HttpHeadersRoot {
    config: PluginConfig,
}

impl Context for HttpHeadersRoot {}

impl RootContext for HttpHeadersRoot {
    // Called when the Wasm VM initializes or when the configuration is updated
    fn on_configure(&mut self, _config_size: usize) -> bool {
        // Retrieve the `pluginConfig` passed by Istio’s WasmPlugin, typically as JSON-serialized bytes
        if let Some(config_bytes) = self.get_plugin_configuration() {
            if !config_bytes.is_empty() {
                let config_str = String::from_utf8(config_bytes).unwrap_or_default();
                info!("Got plugin config: {}", config_str);

                // Parse the JSON configuration into the PluginConfig struct
                match serde_json::from_str::<PluginConfig>(&config_str) {
                    Ok(parsed) => {
                        self.config = parsed;
                        info!("Parsed plugin config successfully!");
                    }
                    Err(e) => {
                        info!("Failed to parse plugin config: {}", e);
                    }
                }
            }
        }
        true
    }

    // Indicate that this RootContext will process HTTP traffic
    fn get_type(&self) -> Option<ContextType> {
        Some(ContextType::HttpContext)
    }

    // Create an HttpContext for each HTTP request
    fn create_http_context(&self, context_id: u32) -> Option<Box<dyn HttpContext>> {
        Some(Box::new(HttpHeaders {
            context_id,
            config: self.config.clone(),
        }))
    }
}

struct HttpHeaders {
    context_id: u32,
    config: PluginConfig,
}

impl Context for HttpHeaders {}

impl HttpContext for HttpHeaders {
    // Do not short-circuit the request; allow it to continue to the backend
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        for (name, value) in &self.get_http_request_headers() {
            info!("#{} -> {}: {}", self.context_id, name, value);
        }
        Action::Continue
    }

    // Add custom headers during the backend response phase
    fn on_http_response_headers(&mut self, _: usize, _: bool) -> Action {
        for (name, value) in &self.get_http_response_headers() {
            info!("#{} <- {}: {}", self.context_id, name, value);
        }

        // Inject `header_1` and `header_2` into the response headers if configured in `pluginConfig`
        if !self.config.header_1.is_empty() {
            self.add_http_response_header("header_1", &self.config.header_1);
        }
        if !self.config.header_2.is_empty() {
            self.add_http_response_header("header_2", &self.config.header_2);
        }

        Action::Continue
    }

    fn on_log(&mut self) {
        info!("#{} completed.", self.context_id);
    }
}
