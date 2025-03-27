Reference Links:


https://virtualcloud.medium.com/mount-aws-s3-on-kubernetes-pods-without-access-key-secret-key-b4f20440970e
https://medium.com/@biswanath.ita/unlock-high-speed-access-to-amazon-s3-objects-from-kubernetes-with-mountpoint-for-s3-csi-driver-4a5a450037a4

1. Create an Amazon EKS cluster
2. Create Amazon S3 buckets
3. Create an IAM policy to allow access to Amazon S3 buckets
4. Create an IAM OIDC provider for the EKS Cluster
5. Create an IAM role, Service Account and link them
6. Install Mountpoint for Amazon S3 CSI driver
7. Deploy a sample application and Test
8. Cleaning up


verify the iam oidc provider

aws eks describe-cluster --name cluster_name --query "cluster.identity.oidc.issuer" --output text

aws iam list-open-id-connect-providers | grep EXAMPLED539D4633E53DE1B716D3041E

if not there then we need to create
eksctl utils associate-iam-oidc-provider --cluster cluster_name --approve

create the policy  iam-policy.json s3 full access

aws iam create-policy --policy-name "aws-s3-mountpoint-policy" --policy-document file://iam-policy.json

Once the policy has been created, we need to create an IAM role and attach this policy

s3-role


After that, we need to create a Kubernetes service account and annotate the IAM role arn to the service account.

kubectl create ns s3-mount

eksctl create iamserviceaccount --name s3-mount-sa --namespace s3-mount --cluster <cluster_name> --role-name <s3 role name> --attach-policy-arn <arn of aws-s3-mountpoint-policy> --approve

as a best practice, we should restrict the permission to a specific pod, therefore we are using IRSA(IAM role for service account) here.


apiVersion: v1
kind: Pod
metadata:
  name: s3-mount-pod-02
  namespace: s3-mount
spec:
  serviceAccountName: s3-mount-sa
  hostNetwork: true
  containers:
    - name: app
      image: amazonlinux
      command: ["/bin/sh"]
      args: ["-c", "while true; do echo $(date -u) >> /example/out.txt; sleep 5; done"]
      securityContext:
        privileged: true





        mount-s3 aws-s3-mountpoint-eks-01 /s3-mountpoint



