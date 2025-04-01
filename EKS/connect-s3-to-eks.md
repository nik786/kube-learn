
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

| Step                                  | Description                                                                                       |
|---------------------------------------|---------------------------------------------------------------------------------------------------|
| **Create an Amazon EKS Cluster**      | Set up an Amazon EKS cluster using the AWS Console, CLI, or `eksctl`.                             |
| **Create Amazon S3 Buckets**          | Create one or more Amazon S3 buckets where you want to store and access data from within your EKS cluster. |
| **Create an IAM Policy to Allow Access to S3 Buckets** | Create an IAM policy to grant permissions for accessing the S3 buckets. Use the `aws iam create-policy` command with a JSON file containing the necessary permissions. |
| **Create an IAM OIDC Provider for the EKS Cluster** | Get the OIDC issuer URL for your EKS cluster, associate the IAM OIDC provider, and confirm the provider ID using AWS CLI commands. |
| **Create an IAM Role and Service Account** | Create an IAM service account with the necessary policy attached to enable S3 access for the EKS pods. Use `eksctl` for this setup. |
| **Install Mountpoint for Amazon S3 CSI Driver** | Deploy the Mountpoint for Amazon S3 CSI driver to your EKS cluster to enable mounting S3 buckets to pods. |


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
