

- [setup-karpenter-on-your-existing-eks-cluster](https://medium.com/@shadracktanui47/setup-karpenter-on-your-existing-eks-cluster-98bf6e959863)
- [eksworkshop](https://www.eksworkshop.com/docs/autoscaling/compute/karpenter/configure)
- [implementing-karpenter-on-eks-and-autoscaling-your-cluster-for-optimal-performance](https://dhruv-mavani.medium.com/implementing-karpenter-on-eks-and-autoscaling-your-cluster-for-optimal-performance-f01a507a8f70)



## Install Karpenter

helm upgrade --install karpenter oci://public.ecr.aws/karpenter/karpenter \
  --version "${KARPENTER_VERSION}" \
  --namespace "karpenter" --create-namespace \
  --set "settings.clusterName=${EKS_CLUSTER_NAME}" \
  --set "settings.interruptionQueue=${KARPENTER_SQS_QUEUE}" \
  --set controller.resources.requests.cpu=1 \
  --set controller.resources.requests.memory=1Gi \
  --set controller.resources.limits.cpu=1 \
  --set controller.resources.limits.memory=1Gi \
  --set replicas=1 \
  --wait

helm upgrade --install --namespace karpenter --create-namespace \
  karpenter oci://public.ecr.aws/karpenter/karpenter \
  --version ${KARPENTER_VERSION} \
  --set serviceAccount.annotations."eks\.amazonaws\.com/role-arn"="arn:${AWS_PARTITION}:iam::${AWS_ACCOUNT_ID}:role/KarpenterControllerRole-${CLUSTER_NAME}" \
  --set settings.clusterEndpoint=${CLUSTER_ENDPOINT} \
  --set settings.clusterName=${CLUSTER_NAME} \
  --wait
