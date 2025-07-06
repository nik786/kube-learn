

- [setup-karpenter-on-your-existing-eks-cluster](https://medium.com/@shadracktanui47/setup-karpenter-on-your-existing-eks-cluster-98bf6e959863)
- [eksworkshop](https://www.eksworkshop.com/docs/autoscaling/compute/karpenter/configure)
- [implementing-karpenter-on-eks-and-autoscaling-your-cluster-for-optimal-performance](https://dhruv-mavani.medium.com/implementing-karpenter-on-eks-and-autoscaling-your-cluster-for-optimal-performance-f01a507a8f70)

```

## Install Karpenter

helm repo add karpenter https://charts.karpenter.sh
helm repo update




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



aws eks update-kubeconfig --region us-east-1 --name gl-dev


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




kubectl scale deployment inflate --replicas 5
kubectl logs -f -n karpenter -l app.kubernetes.io/name=karpenter -c controller

kubectl scale deployment nginx --replicas 0
kubectl logs -f -n karpenter -l app.kubernetes.io/name=karpenter -c controller

Key=karpenter.sh/discovery,Value=gl-dev



aws ec2 describe-images   --owners amazon   --filters "Name=name,Values=al2023-ami-*-arm64"            "Name=architecture,Values=arm64"            "Name=root-device-type,Values=ebs"            "Name=virtualization-type,Values=hvm"   --query "Images[*].{Name:Name,ImageId:ImageId,CreationDate:CreationDate}"   --output table


aws ec2 describe-images   --owners amazon   --filters "Name=name,Values=amzn2-ami-hvm-*-arm64-gp2"            "Name=architecture,Values=arm64"            "Name=virtualization-type,Values=hvm"   --query "Images[*].{Name:Name,ImageId:ImageId,CreationDate:CreationDate}"   --output table










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
