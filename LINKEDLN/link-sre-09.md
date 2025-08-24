

Advanced kubernetes Knowledge every Devops guy worth it’s salt should be able to answer

👉 1. If you have a Pod with initContainers that fail, but the main container has restartPolicy: Never, what happens to the Pod status?

👉 2. When using a StatefulSet with 3 replicas and you delete replica-1, will replica-2 and replica-3 be renamed to maintain sequential ordering?

👉 3. Can a DaemonSet Pod be scheduled on a master node that has NoSchedule taint without explicitly adding tolerations?

👉 4. If you update a Deployment's image while a rolling update is in progress, will K8s wait for the current rollout to complete or start a new one immediately?

👉 5. When a node becomes NotReady, how long does it take for Pods to be evicted, and can this be controlled per Pod?

👉 6. Is it possible for a Pod to have multiple containers sharing the same port on localhost, and what happens if they try to bind simultaneously?

👉 7. If you create a PVC with ReadWriteOnce access mode, can multiple Pods on the same node access it simultaneously?

👉 8. When using Horizontal Pod Autoscaler with custom metrics, what happens if the metrics server becomes unavailable during high load?

👉 9. Can you run kubectl port-forward to a Pod that's in CrashLoopBackOff state, and will it work?

👉 10. If a ServiceAccount is deleted while Pods using it are still running, what happens to the mounted tokens and API access?

👉 11. When using anti-affinity rules, is it possible to create a "deadlock" where no new Pods can be scheduled?

👉 12. If you have a Job with parallelism: 3 and one Pod fails with restartPolicy: Never, will the Job create a replacement Pod?

👉 13. Can a Pod's resource requests be modified after creation, and what's the difference between requests and limits during OOM scenarios?

👉 14. When using network policies, if you don't specify egress rules, are outbound connections blocked by default?

👉 15. If a Persistent Volume gets corrupted, can multiple PVCs bound to it cause cascading failures across different namespaces?

How many can you answer without checking the docs?
Drop your answers in the comments!

🍀 Consider a repost if you found it useful.

P.S> You can find all the answers in this blog post. 
