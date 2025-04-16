
```

How to connect S3 bucket in eks cluster
---------------------------------------

1. Create an Amazon EKS cluster
2. Create Amazon S3 buckets
3. Create an IAM policy to allow access to Amazon S3 buckets
4. Create an IAM OIDC provider for the EKS Cluster
5. Create an IAM role, Service Account and link them
6. Install Mountpoint for Amazon S3 CSI driver
7. Deploy a sample application and Test
8. Cleaning up

```

| **Step** | **Description** | **Commands** |
|---------|------------------|--------------|
| **Create an Amazon EKS Cluster** | Set up an Amazon EKS cluster. | eksctl create cluster --name my-cluster --region us-west-2 --nodes 2 --node-type t3.medium --with-oidc --managed |
| **Create Amazon S3 Buckets** | Create S3 buckets to access from the EKS cluster. | aws s3api create-bucket --bucket my-eks-s3-bucket --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2 |
| **Create an IAM Policy to Allow Access to S3 Buckets** | Define S3 access permissions. | 1. Create a file `s3-access-policy.json` with the S3 permissions.<br>2. aws iam create-policy --policy-name EKS_S3_Access_Policy --policy-document file://s3-access-policy.json |
| **Create an IAM OIDC Provider for the EKS Cluster** | Associate IAM OIDC provider with EKS. | aws eks describe-cluster --name my-cluster --query "cluster.identity.oidc.issuer" --output text<br>eksctl utils associate-iam-oidc-provider --cluster my-cluster --approve |
| **Create an IAM Role and Service Account** | Use IRSA to let pods access S3. | eksctl create iamserviceaccount --name s3-access-sa --namespace default --cluster my-cluster --attach-policy-arn arn:aws:iam::<ACCOUNT_ID>:policy/EKS_S3_Access_Policy --approve --override-existing-serviceaccounts |
| **Install Mountpoint for Amazon S3 CSI Driver** | Deploy CSI driver to EKS. | helm repo add aws-mountpoint-s3-csi-driver https://awslabs.github.io/mountpoint-s3-csi-driver<br>helm repo update<br>helm upgrade --install aws-mountpoint-s3-csi-driver aws-mountpoint-s3-csi-driver/aws-mountpoint-s3-csi-driver --namespace kube-system --set controller.serviceAccount.name=s3-access-sa |



---

### 7. **Deploy a Sample Application with S3 Mount**
-------------------------------------------------------

   - Create a sample pod configuration to mount the S3 bucket:
     ```yaml
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
     ```

---

### 8. **Install Required Packages in the Pod**
---------------------------------------------------

   - Install dependencies like `awscli` and the `mount-s3` RPM:
     ```bash
     yum install unzip -y
     yum install wget -y
     yum install util-linux-ng -y
     curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
     unzip awscliv2.zip
     ./aws/install
     wget https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.rpm
     yum install -y ./mount-s3.rpm
     ```

---

### 9. **Mount S3 Bucket to the Pod**
-------------------------------------------

   - Mount the S3 bucket to the desired directory in your pod:
     ```bash
     mount-s3 aws-s3-mountpoint-eks-01 /s3-mountpoint
     ```

---

### 10. **Test the Setup**
-----------------------------

   - Verify that the application running on the pod can successfully interact with the mounted S3 bucket by checking the output files.

---

### 11. **Cleaning Up**

   - After testing, delete the resources to clean up:
     - Delete the EKS cluster.
     - Remove the S3 bucket.
     - Delete IAM roles, policies, and service accounts.


```
