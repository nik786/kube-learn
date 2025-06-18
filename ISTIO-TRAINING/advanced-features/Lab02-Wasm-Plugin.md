
Lab 2: Wasm Plugin

- Write a web assembly plugin in Rust
- Load it into envoy sidecar via istio
- Add custom HTTP headers to response


  ```
   rustp target add wasm32-wasi

   mkdir wasm-extension-rs &&  cd wasm-extension-rs

   cargo init --lib

  vim Cargo.toml

  [package]
  name = "wasm-extension-rs"
  version = "0.1.0"
  edition = "2021"

  [dependencies]
   proxy-wasm = "0.2.2"
  serde_json = "1.0"
  serde = { version = "1.0", features = ["derive"] }
  log = "0.4"

  [lib]
  crate-type = ["cdylib"]

  
  
   cargo build --release --target wasm32-wasi

   cp target/wasm32-wasi/release/wasm_extension_rs.wasm plugin.wasm

   The crate-type = ["cdylib"] setting ensures the output is a dynamic library, making it suitable for Wasm compilation
  

  ```

3. Writing the Plugin Logic

vim src/lib.rs








  
