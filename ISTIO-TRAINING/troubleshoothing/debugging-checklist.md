
## Debugging Checklist

## Important Note

- Applies primarily to sidecar mode
- Ambient Mode requires different debugging tools and steps


## Configuration Validation: Syntax

Use istioctl validate to check for YAML or api errors

```

istoctl validate -f myresource.yaml

```


## Example success

validation succeed

## Example error

unknown field "workloadselector" in v1.ServiceEntry

## Configuration Validation: Semantics

- Use istioctl to analyse deeper issues

  istioctl analyse --all-namespaces

## Example Errors:

Referenced host not found: "customers.default.svc.cluster.local"


## Namespaces and Selectors

- Ensure resources are in the correct namespace
- Check label selectors match your pods
- Mismatches lead to traffic not being routed as expected

  
## Runtime Checks: istioctl x describe

- Run istioctl x describe pod/pod for quick diagnostics
- Shows matched services, routes and potential config issues

## Example:

Warning: No destination match pod subsets
Route to customers.default.svc.cluster.local


## Runtime Checks: Proxy Sync

- Run istioctl proxy-status to check sync state be/w envoy and istiod
- Look for SYNCED. STALE or NOT SENT means problems


## Possible issues:
  
  - Network failure
  - Misconfiguration
  - Sidecar not injected


## Runtime Checks: Inspect Envoy Config


| Command                                                                 | Description                                                        |
|-------------------------------------------------------------------------|--------------------------------------------------------------------|
| `istioctl proxy-config cluster [pod] -n [namespace]`                    | Shows the Envoy cluster config (e.g., how DestinationRules manifest) |
| `istioctl proxy-config route [pod] -n [namespace]`                      | Shows the Envoy route config (mapping VirtualServices)             |
| `istioctl proxy-config listener [pod] -n [namespace]`                   | Shows which ports and filters Envoy is listening on                |
| `istioctl proxy-config endpoint [pod] -n [namespace]`                   | Shows the service endpoints each Envoy cluster sees                |
| `istioctl proxy-config bootstrap [pod] -n [namespace]`                  | Displays Envoy’s initial bootstrap configuration                   |


## Advanced Envoy Debugging

- Use istioctl pc log pod to view or adjust the log level
- Use istioctl admin log or port-forward to inspect the Envoy admin ui

```  
istioctl admin log [pod] --level debug
istioctl admin port-forward [pod] 15000
```

## Istiod Logs

- Check pilot logs for config rejection

   kubectl logs -f istiod-pod -n istio-system

- Look for errors like

  ACK ERROR .. Script load error



## Envoy Access Logs

- Inspect sidecar logs:

  kubectl logs pod -c istio-proxy -n istio-system

- Common error codes:

    NR: No Route
    UF: Up stream Faliure
    UH: No Healthy Upstream

   
## Ephermeral Containers(K8S 1.25+)
- Use for in-cluster debugging

  kubectl debug pod -n ns  --image=busybox --target=istio-proxy

- Run tools like curl,tcpdump, etc


## Adjusting Istiod Logs(Controlz)

- Run

   ```
    istioctl dashboard controlz $(kubectl -n istio-system get pods -l app=istiod -o jsonpath='{.items[0].metadata.name}').istio-system

   ```
- Adjust log level under Logging Scopes

  

























  






















  
