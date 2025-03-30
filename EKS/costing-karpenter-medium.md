
# Cost Optimization in EKS using Karpenter

| Topic | Details |
|-------|---------|
| **Problem** | EKS with EC2 worker nodes running 24/7 in a non-production environment, with only ~70% utilization on average. |
| **Wasted Resources** | 20–30% of EC2 capacity was idle and underutilized. |
| **Goal** | Reduce costs and dynamically manage workloads based on real-time demand. |
| **Solution Implemented** | Used [**Karpenter**](https://karpenter.sh) to auto-scale EC2 resources based on actual workload needs. |
| **Cost Reduction Achieved** | 💰 **70%** savings on EC2 instance costs. |
| **Previous Setup** | Static provisioning of EC2 instances for workloads like applications, observability, gateways, and cronjobs. |
| **Challenge** | Avoid overprovisioning, right-size the nodes, and enable auto-scaling when load increased. |
| **What is Karpenter?** | An open-source tool by AWS that works with any Kubernetes cluster to dynamically provision compute resources. |
| **How Karpenter Works** | Monitors resource utilization and provisions/de-provisions EC2 instances based on actual usage and pending pod requirements. |
| **Benefits** | - **Auto-scaling** based on demand<br>- **Spot instance support** for lower costs<br>- **No need for manual node groups**<br>- **Cost-efficiency** through minimal idle capacity |
| **Install Karpenter** | Use [`eksdemo`](https://eksdemo.dev) to quickly install:<br>`eksdemo install karpenter --cluster <CLUSTER-NAME>` |
| **Getting Started** | Follow this guide to understand how [**eksdemo CLI**](https://eksdemo.dev/cli/) simplifies the setup. |

---

> ✅ By letting Karpenter handle the provisioning, I ensured the EKS cluster only used resources when they were truly needed — optimizing both **performance** and **costs**.


Create Karpenter NodeClass:
-----------------------------


```



# nodeClass.yaml
---
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: application-nodeclass
  namespace: karpenter
spec:
  amiFamily: AL2
  role: "KarpenterNodeRole-<CLUSTER-NAME>"
  subnetSelectorTerms:
    - tags:
        Name: "eksctl-<CLUSTER-NAME>-cluster/SubnetPrivate*"
  securityGroupSelectorTerms:
    - tags:
        aws:eks:cluster-name: "<CLUSTER-NAME>"
  amiSelectorTerms:
    - id: "ami-0dc0bbee757c82f5e"
  tags:
    component: application


```



## Karpenter Configuration Breakdown

| Configuration Key | Description |
|-------------------|-------------|
| **`amiFamily`** | Defines the Amazon Machine Image (AMI) family (e.g., AL2, Bottlerocket) that the nodes should use. It determines the OS and base image used for EC2 instances. |
| **`role`** | Specifies the IAM role to be attached to the EC2 instances provisioned by Karpenter. This role must have the necessary permissions for node operations. |
| **`subnetSelectorTerms`** | Determines which subnets Karpenter can use to launch EC2 instances. Subnets can be filtered using tags or conditions. |
| **`securityGroupSelectorTerms`** | Specifies the security groups that will be associated with the EC2 instances launched by Karpenter. Useful for controlling network access. |
| **`amiSelectorTerms`** | Allows you to define specific AMI IDs or use filters to select the desired AMI for the nodes. This gives precise control over the image used. |
| **`tags`** | Adds custom metadata tags to EC2 instances. These tags can be used for cost tracking, organization, automation, or other AWS tagging strategies. |


```






Create Karpenter NodePool:
# nodePool.yaml
---
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: application-nodepool
  namespace: karpenter
spec:
  template:
    metadata:
      labels:
        component: "application"
    spec:
      requirements:
        - key: kubernetes.io/arch
          operator: In
          # Nodes must be amd64 architecture.
          values: ["amd64"]
        - key: kubernetes.io/os
          operator: In
          # Nodes must run Linux.
          values: ["linux"]
        - key: karpenter.sh/capacity-type
          operator: In
          # Allows both on-demand and spot instances.
          # Karpenter will first attempt to provision spot instances for cost efficiency.
          # If spot instances are unavailable (e.g., due to capacity constraints or pricing changes),
          # Karpenter will automatically fall back to on-demand instances.
          values: ["on-demand", "spot"]
        - key: karpenter.k8s.aws/instance-family
          operator: In
          # Restricts nodes to instance families
          values: ["t3", "t3a"]
        - key: karpenter.k8s.aws/instance-generation
          operator: Gt
          # Ensures nodes are from generation greater than 2.
          values: ["2"]
        - key: topology.kubernetes.io/zone
          operator: In
          # Limits node provisioning to availability zones
          values: ["ap-southeast-1a", "ap-southeast-1b"]
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: application-nodeclass
      # Nodes older than 720 hours (30 days) are considered for termination.
      expireAfter: 720h
  limits:
    # Prevents the NodePool from provisioning nodes beyond the equivalent of 1000 CPU cores.
    # Useful for cost control and resource planning.
    cpu: 1000
  disruption:
    # Nodes are eligible for consolidation when they are empty or underutilized.
    consolidationPolicy: WhenEmptyOrUnderutilized
    # Karpenter waits 1 minute before consolidating nodes after they become eligible.
    consolidateAfter: 1m


```


## Karpenter Automatic Node Provisioning

| Configuration Key       | Description |
|-------------------------|-------------|
| **`labels`**            | Adds custom Kubernetes labels to all nodes provisioned by this `NodePool`. Useful for workload targeting and scheduling. |
| **`requirements`**      | Sets node constraints (e.g., instance types, architectures, zones) that guide what kind of nodes should be provisioned. |
| **`nodeClassRef`**      | Refers to an existing `EC2NodeClass` that defines detailed EC2 settings like AMI, IAM role, subnets, and more. |
| **`expireAfter`**       | Specifies the TTL (Time-To-Live) for nodes. After this duration, Karpenter can deprovision and replace the node. Useful for maintaining node freshness. |
| **`limits`**            | Defines resource limits, such as maximum vCPUs or memory, that this `NodePool` is allowed to provision. Prevents over-scaling. |
| **`disruption`**        | Controls node consolidation and interruption policies. Helps balance cost savings with application availability and stability. |



```


```




# deployment.yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: inflate
  namespace: default
spec:
  replicas: 10
  selector:
    matchLabels:
      app: "inflate"
      component: "application"
  template:
    metadata:
      labels:
        app: "inflate"
        component: "application"
    spec:
      terminationGracePeriodSeconds: 0
      securityContext:
        runAsUser: 1000
        runAsGroup: 3000
        fsGroup: 2000
      containers:
        - name: application
          image: public.ecr.aws/eks-distro/kubernetes/pause:3.7
          resources:
            requests:
              cpu: 0.25
              memory: 512Mi
            limits:
              cpu: 0.25
              memory: 512Mi
          securityContext:
            allowPrivilegeEscalation: false
      nodeSelector:
        component: "application"
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchLabels:
                  component: "application"
              topologyKey: "kubernetes.io/hostname"
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: "kubernetes.io/hostname"
          whenUnsatisfiable: DoNotSchedule
          labelSelector:
            matchLabels:
              component: "application"
The deployment above shows how Karpenter automatically provisions the right number of nodes based on the scaling needs.

In this case, Karpenter created 10 Spot instances, each running on a separate node.



```



Test Karpenter Node Consolidation
To test node consolidation, remove affinity.podAntiAffinity and update thetopologySpreadConstraints .

This will allow the pod containers to consolidate on the nodes and spread across Availability Zones (AZs).



```

# deployment.yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: inflate
  namespace: default
spec:
  replicas: 10
  selector:
    matchLabels:
      app: "inflate"
      component: "application"
  template:
    metadata:
      labels:
        app: "inflate"
        component: "application"
    spec:
      terminationGracePeriodSeconds: 0
      securityContext:
        runAsUser: 1000
        runAsGroup: 3000
        fsGroup: 2000
      containers:
        - name: application
          image: public.ecr.aws/eks-distro/kubernetes/pause:3.7
          resources:
            requests:
              cpu: 0.25
              memory: 512Mi
            limits:
              cpu: 0.25
              memory: 512Mi
          securityContext:
            allowPrivilegeEscalation: false
      nodeSelector:
        component: "application"
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: ScheduleAnyway
          labelSelector:
            matchLabels:
              app: "inflate"
              component: "application"

Wait a few minutes for Karpenter’s consolidation logic to figure out whether it needs to replace or terminate any nodes.

```

## Conclusion

| Key Takeaway | Description |
|--------------|-------------|
| **Dynamic Provisioning** | Karpenter provisions EC2 instances on-demand, based on real-time cluster usage, avoiding idle resources. |
| **Automatic Scaling** | It automatically scales nodes up or down as workloads change, without manual intervention. |
| **Spot Instance Utilization** | Supports AWS Spot Instances to reduce EC2 costs significantly compared to On-Demand pricing. |
| **Cost Optimization** | Helps reduce unnecessary spend by right-sizing and removing underutilized nodes. |
| **Seamless EKS Integration** | Works natively with AWS EKS, making it easy to deploy and manage within your existing Kubernetes environment. |
| **Ideal for Cloud Efficiency** | Perfect for teams aiming to improve workload efficiency, control costs, and enhance cloud-native operations. |


























