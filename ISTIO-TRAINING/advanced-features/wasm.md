


| Topic                     | Description                                                                                          |
|---------------------------|------------------------------------------------------------------------------------------------------|
| What is Wasm              | WebAssembly (Wasm) is a portable, binary format for executable code, based on an open standard.     |
| Language Support          | Code can be written in languages like Go or Rust and compiled to Wasm.                              |
| Why Use Wasm for Plugins  | Wasm is language-agnostic and binary-portable, making it ideal for plugin systems.                  |
| Execution Environment     | Wasm plugins run in a memory-safe sandbox (virtual machine) and are isolated from the host.          |
| Communication             | Plugins interact with the host via a well-defined API.                                               |
| Proxy-Wasm                | ABI specification to extend proxies (like Envoy) using Wasm plugins.                                 |
| Lua Filter (Envoy)        | Allows embedding Lua scripts for lightweight tasks using EnvoyFilter resource.                      |
| Wasm Filter               | Enables writing complex functionality, compiled into Wasm, and loaded dynamically by Envoy.         |
| WasmPlugin Resource       | Introduced in Istio 1.12, it simplifies referencing Wasm plugins stored in OCI-compliant registries. |
| OCI Registry Support      | Istio agent can download Wasm plugins from OCI-compliant registries (like Docker images).            |


WasmPlugin resource
----------------------

The WasmPlugin resource allows us to configure Wasm plugins for Envoy proxies 
running in the Istio service mesh. Here is an example WasmPlugin resource:


```
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: hello-world-wasm
  namespace: default
spec:
  selector:
    labels:
      app: hello-world
  url: oci://my-registry/tetrate/hello-world:v1
  pluginConfig:
    greeting: hello
    something: anything
  vmConfig:
    - name: TRUST_DOMAIN
      value: "cluster.local"


```

| Field/Setting     | Description                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------|
| `selector`        | Uses labels to determine which workloads the Wasm plugin will be applied to.                                |
| `url`             | Specifies the plugin location. Supports `oci://` (default), `file://`, and `http[s]://`.                     |
| `imagePullPolicy` | (Optional) Used with `oci://` URLs to define image pull behavior.                                            |
| `imagePullSecret` | (Optional) Secret to authenticate when pulling Wasm plugins from private OCI registries.                    |
| `pluginConfig`    | Custom configuration passed to the plugin; accessible via Proxy-Wasm ABI calls inside the plugin.           |
| `vmConfig`        | VM-specific configuration, such as environment variables to be used by the plugin.                          |
| `priority`        | Sets the order in which multiple Wasm plugins are applied.                                                  |
| `phase`           | Defines the position in the Envoy filter chain where the plugin will be injected.                          |








