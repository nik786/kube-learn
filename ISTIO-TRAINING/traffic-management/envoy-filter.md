

# EnvoyFilter

- EnvoyFilter allows customisation of envoy configuration within ISTIO
- Enables modifications to
     - Existing filters
     - Listeners and Clusters
     - Additional traffic Processing logic
- Should be used with caution to avoid destabilising the mesh
    

## How Envoy Filter works

- Filters applied at the root namespaces(istio-system) affect the entire mesh
- Filters applied at the namespace level only affect workloads in that namespace
- Modifications are incremental - they extend , not replace, ISTIOS default envoy configuration






Here’s an example of an EnvoyFilter that adds a header called api-version to the request.

```
apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  name: api-header-filter
  namespace: default
spec:
  workloadSelector:
    labels:
      app: web-frontend
  configPatches:
  - applyTo: HTTP_FILTER
    match:
      context: SIDECAR_INBOUND
      listener:
        portNumber: 8080
        filterChain:
          filter:
            name: "envoy.http_connection_manager"
            subFilter:
              name: "envoy.router"
    patch:
      operation: INSERT_BEFORE
      value:
        name: envoy.lua
        typed_config:
          "@type": "type.googleapis.com/envoy.config.filter.http.lua.v2.Lua"
          inlineCode: |
            function envoy_on_response(response_handle)
              response_handle:headers():add("api-version", "v1")
            end


```

If you send a request to the $GATEWAY_URL you can notice the api-version header is added, as shown below:


Verifying the custom Header
------------------------------

Run a curl request to check the injected header

curl -s -I -X HEAD  http://$GATEWAY_URL

HTTP/1.1 200 OK
x-powered-by: Express
content-type: text/html; charset=utf-8
content-length: 2471
etag: W/"9a7-hEXE7lJW5CDgD+e2FypGgChcgho"
date: Tue, 17 Nov 2020 00:40:16 GMT
x-envoy-upstream-service-time: 32
api-version: v1
server: istio-envoy


The api Version: v1 header confirms that the filter is working




Key Considerations
---------------------

- Use Minimal Changes: Avoid unnecessary modifications to envoy to prevent instability
- Test in Staging: Always test filters before deploying to production
- Namespace Scope:
    - Filters in istio-system apply to the entire mesh
    - Namespace specfic filters only affect workloads within that namespace


Common Use Cases
-----------------

- Adding or Modifying headers for tracing, debugging or monitoring
- Injecting custom Lua or Wasm filters for advanced processing
- Overriding istios default envoy configurations for specific workloads
- Implementing advanced rate limiting by modifying envoy setting



      



















```
