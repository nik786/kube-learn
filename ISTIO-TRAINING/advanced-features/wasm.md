


## Wasm Plugins

- WebAssembly is a portable binary format for executing code in a memory-safe sandbox.
- Language agnostic: Write code in multiple languages and compile to WASM 
- Ideal for extending envoys' functionality within Istio.
- Proxy-Wasm is the API specification for extending proxies with Wasm


## Extending Envoy with Wasm

- Lua Filters:
    - Used for simple HTTP request modifications
    - Example: Injecting headers into responses
 
- Wasm Filters
    - More powerful and flexible
    - Written in languages like Go or Rust
    - Compiled into wasm and loaded dynamically by envoy
      


- selector: Defines workloads that the wasm plugins apply to
- url: Specifies the plugin's location(OCI registry, file or HTTP)
- pluginConfig: Configuration setting for the Wasm plugin.
- vmConfig: Environment variables injected into the wasm vm.



- Additional wasmplugin settings
   - priority: Determines execution order when multiple wasm plugins are applied
   - phase: Controls where in the filter chain the plugin is injected

