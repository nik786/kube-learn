
8. Entry point vs CMD in a Dockerfile.
| **Attribute**                             | **ENTRYPOINT**                                          | **CMD**                                               |
|-------------------------------------------|---------------------------------------------------------|-------------------------------------------------------|
| **Purpose**                               | Invoke executable service when the container is started. | Specifies the arguments which get passed to the ENTRYPOINT. |
| **Command Line Overwrite**                | Command and parameters will not be overwritten from the command line. | Default command and/or parameters, which can be overwritten from the command line. |
| **Syntax Example**                        | `ENTRYPOINT ["executable"]`                             | `CMD ["executable", "arg1", "arg2"]`                   |

   
10. Add vs Copy in Dockerfile.

| **Attribute**         | **COPY**                                        | **ADD**                                          |
|-----------------------|-------------------------------------------------|--------------------------------------------------|
| **Basic Function**     | Only supports basic copying of local files into the container. | Supports local tar file auto extraction and remote URL support. |
| **Use Case**           | Simple file copying from host to container.    | Can copy files and also handle tar extraction and fetching from remote URLs. |
    
11. Describe Kubernetes architecture.

    [kubernetes architecture](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/k8s-docker.md)
    
13. Do you know Ansible?  
14. Difference between Secrets and ConfigMap in Kubernetes.  
15. Docker lifecycle.  
16. What is a ReplicaSet?  
17. Running Kubernetes in a single-node local environment.  
