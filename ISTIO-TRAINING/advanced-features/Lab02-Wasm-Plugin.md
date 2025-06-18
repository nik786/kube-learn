
Lab 2: Wasm Plugin

- Write a web assembly plugin in Rust
- Load it into envoy sidecar via istio
- Add custom HTTP headers to response



1. Installing Dependencies

   1. Rust Toolchain
      First, install Rust (requires the cargo command to be available).
      It is recommended to use stable or a later version of Rust.
   

   2.  Wasm Target
       We need to compile Rust into Wasm (WASI). Add the target:

       rustp target add wasm32-wasi

    3. Docker / Podman
       
       Used to package the compiled .wasm file into an image and push it to an OCI registry

  


2. Initializing the Plugin Project

     1. Create the Working Directory
        
        mkdir wasm-extension-rs && cd wasm-extension-rs
         

     3. Initialise a Cargo Project

         cargo init --lib

         This will generate a Cargo.toml and src/lib.rs file.

     4. Add Dependencies to Cargo.toml

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

 3. Writing the Plugin Logic

     vim src/lib.rs

     [lib-rs](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/advanced-features/lib.rs)       



4. Compiling the Wasm Binary

   Run the following command in the project directory:
  
   cargo build --release --target wasm32-wasi

   cp target/wasm32-wasi/release/wasm_extension_rs.wasm plugin.wasm

   The crate-type = ["cdylib"] setting ensures the output is a dynamic library, making it suitable for Wasm compilation
  

5.  Packaging and Pushing to an OCI Registry

    Similar to the previous experiment, we will use Docker to package an empty image containing only the compiled plugin.wasm file.

    ## Example Dockerfile:

  ```
    FROM scratch
    COPY plugin.wasm /plugin.wasm
  ```


  Build and push the image (using Docker Hub as an example, but you can use a private registry instead):


```
 export REPO="jimmysong/wasm-plugin-rs"
 docker build -t $REPO:v1 .
 docker push $REPO:v1
```

6. Creating the WasmPlugin Resource

  ```
  cat wasm-plugin-rs.yaml

   apiVersion: extensions.istio.io/v1alpha1
   kind: WasmPlugin
   metadata:
     name: wasm-example-rs
     namespace: default
   spec:
     selector:
       matchLabels:
         app: httpbin
      url: oci://docker.io/your-dockerhub-username/wasm-plugin-rs:v1
      imagePullPolicy: IfNotPresent
      pluginConfig:
        header_1: "my-first-header"
        header_2: "my-second-header"

kubectl apply -f wasm-plugin-rs.yaml

```

  
7.  Deploying and Testing the Application

   ```

      1. Enable sidecar injection in the default namespace:

          kubectl label namespace default istio-injection=enabled

      2.   Deploy httpbin:

            kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples

      3. Wait for the Pod to start successfully:
         kubectl get pods

     4.  Deploy a test pod and perform a curl test:
  
        
         kubectl run curl --image=curlimages/curl:latest --image-pull-policy=IfNotPresent --command -- /bin/sh -c "sleep infinity"
         kubectl exec -it curl -- curl -s --head httpbin:8000/get

```


Through this lab, you have learned how to write a simple Proxy-Wasm plugin using Rust, package it into an OCI Registry, 
and load it into Envoy using Istio’s WasmPlugin CRD. In real-world scenarios, you can implement more complex logic 
in Rust plugins (such as authentication, metrics collection, and traffic manipulation) or extend Istio using 
other languages and mechanisms (e.g., Lua, External Processing).



           








  
