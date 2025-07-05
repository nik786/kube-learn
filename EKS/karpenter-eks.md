

- [setup-karpenter-on-your-existing-eks-cluster](https://medium.com/@shadracktanui47/setup-karpenter-on-your-existing-eks-cluster-98bf6e959863)
- [eksworkshop](https://www.eksworkshop.com/docs/autoscaling/compute/karpenter/configure)
- [implementing-karpenter-on-eks-and-autoscaling-your-cluster-for-optimal-performance](https://dhruv-mavani.medium.com/implementing-karpenter-on-eks-and-autoscaling-your-cluster-for-optimal-performance-f01a507a8f70)

```

## Install Karpenter

helm repo add karpenter https://charts.karpenter.sh
helm repo update

helm upgrade --install karpenter karpenter/karpenter \
  --namespace karpenter \
  --create-namespace \
  --version "0.33.0" \
  --set serviceAccount.annotations."eks\.amazonaws\.com/role-arn"="arn:aws:iam::359994326874:role/KarpenterControllerRole-gl-dev" \
  --set settings.clusterEndpoint="https://AE0A2304EB571BEDB5906A71EAD4C1B9.gr7.us-east-1.eks.amazonaws.com" \
  --set settings.clusterName="gl-dev" \
  --wait


helm search repo karpenter/karpenter --versions


aws ecr-public get-login-password \
  --region us-east-1 | helm registry login \
  --username AWS \
  --password-stdin public.ecr.aws


helm upgrade --install karpenter oci://public.ecr.aws/karpenter/karpenter \
  --version "1.5.2" \
  --namespace karpenter \
  --create-namespace \
  --set settings.clusterName=gl-dev \
  --set controller.resources.requests.cpu=1 \
  --set controller.resources.requests.memory=1Gi \
  --set controller.resources.limits.cpu=1 \
  --set controller.resources.limits.memory=1Gi \
  --set replicas=1 \
  --set settings.aws.defaultInstanceProfile=KarpenterNodeInstanceProfile \
  --wait



{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowPricingAndEC2Lookups",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeSpotPriceHistory",
        "ec2:DescribeInstanceTypeOfferings",
        "pricing:GetProducts"
      ],
      "Resource": "*"
    }
  ]
}










```






```

resource "aws_iam_role" "karpenter_eks_node_role" {
  name = "karpenter-eks-node-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

  inline_policy {
    name = "KarpenterNodeEC2PricingPermissions"
    policy = jsonencode({
      Version = "2012-10-17",
      Statement = [
        {
          Sid    = "AllowPricingAndEC2Lookups",
          Effect = "Allow",
          Action = [
            "ec2:DescribeSpotPriceHistory",
            "ec2:DescribeInstanceTypeOfferings",
            "pricing:GetProducts"
          ],
          Resource = "*"
        }
      ]
    })
  }
}
```
