
## Vertical Scaling
---------------------

```
apiVersion: "autoscaling.k8s.io/v1"
kind: VerticalPodAutoscaler
metadata:
  name: stress-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: high-cpu-utilization-deployment
  updatePolicy:
    updateMode: Auto
  resourcePolicy:
    containerPolicies:
      - containerName: '*'
        minAllowed:
          cpu: 100m
          memory: 50Mi
        maxAllowed:
          cpu: 200m  #maximum vpa will be allocating this many cpus even if demand is higher.
          memory: 500Mi
        controlledResources: ["cpu", "memory"]

```
