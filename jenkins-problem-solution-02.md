# Jenkins and Kubernetes Integration Workflow

This workflow outlines the steps to integrate Jenkins with Kubernetes to enable Jenkins to deploy and manage workloads using Kubernetes.

---

### 1. **Create a Kubernetes Secret for Jenkins**

   - Create a secret to store the Jenkins service account token to authenticate Jenkins with Kubernetes:
     ```bash
     kubectl create secret generic jenkins-token
     ```

---

### 2. **Create a Service Account for Jenkins**

   - Create a service account for Jenkins that allows it to interact with Kubernetes:
     ```bash
     kubectl create serviceaccount jenkins
     ```

---

### 3. **Enable `automountServiceAccountToken` for the Jenkins Service Account**

   - Patch the Jenkins service account to enable automatic mounting of the service account token:
     ```bash
     kubectl patch serviceaccount jenkins -p '{"automountServiceAccountToken": true}'
     ```

---

### 4. **Patch the Secret to Associate it with the Jenkins Service Account**

   - Associate the `jenkins-token` secret with the Jenkins service account:
     ```bash
     kubectl patch secret jenkins-token -p '{"metadata": {"annotations": {"kubernetes.io/service-account.name": "jenkins"}}}'
     ```

---

### 5. **Retrieve the Secret Token**

   - Retrieve the secret token from the Kubernetes secret to use in Jenkins:
     ```bash
     kubectl get secret jenkins-token -o yaml
     ```

---

### 6. **Switch to Jenkins UI and Configure Credentials**

   - Log into Jenkins, navigate to **Credentials**, and follow these steps:
     - Go to **Jenkins > Manage Jenkins > Manage Credentials**.
     - Click **Add Credentials**, and select **Secret text**.
     - Paste the copied secret token into the **Secret** field.
     - Click **OK** to save the credentials.

---

### 7. **Install the Kubernetes Plugin in Jenkins**

   - Install the **Kubernetes Plugin** to enable Kubernetes integrations with Jenkins:
     - Navigate to **Jenkins > Manage Jenkins > Manage Plugins**.
     - Install the **Kubernetes Plugin** from the available plugins list.

---

### 8. **Configure Kubernetes Cloud in Jenkins**

   - Configure Jenkins to connect to your Kubernetes cluster:
     - Go to **Manage Jenkins > Configure System**.
     - Scroll to the **Cloud** section and click **Add a new cloud > Kubernetes**.
     - Set the following fields:
       - **Name**: Kubernetes
       - **Kubernetes URL**: `https://<K8S_API_SERVER_IP>:6443`
       - **Kubernetes Namespace**: `default` (or your preferred namespace)
       - **Credentials**: Select the credentials that were created using the `jenkins-token` secret.
       - **Use Pod Label to identify it**: Choose a label to identify Jenkins agents (pods).

---

### 9. **Save the Configuration**

   - Click **Save** to apply the configuration. Jenkins will now be able to deploy and manage workloads in Kubernetes.

---

With this workflow, Jenkins is now connected to Kubernetes, using a service account and token for secure authentication and the Kubernetes plugin to manage pods for building and deploying applications.



A stateless app does not retain any client session or data between requests, 
while a stateful app maintains client-specific data or session information across multiple interactions






How to connect S3 bucket in eks cluster

Create an Amazon EKS cluster
Create Amazon S3 buckets
Create an IAM policy to allow access to Amazon S3 buckets
Create an IAM OIDC provider for the EKS Cluster
Create an IAM role, Service Account and link them
Install Mountpoint for Amazon S3 CSI driver
Deploy a sample application and Test
Cleaning up


# Connecting Amazon S3 Bucket to EKS Cluster

This guide outlines the steps to connect an Amazon S3 bucket to an Amazon EKS cluster and mount it using the Mountpoint for Amazon S3 CSI driver.

---

### 1. **Create an Amazon EKS Cluster**

   - Set up an Amazon EKS cluster using the AWS Console, CLI, or `eksctl`.

---

### 2. **Create Amazon S3 Buckets**

   - Create one or more Amazon S3 buckets where you want to store and access data from within your EKS cluster.

---

### 3. **Create an IAM Policy to Allow Access to S3 Buckets**

   - Create an IAM policy to grant permissions for accessing the S3 buckets:
     ```bash
     aws iam create-policy --policy-name "aws-s3-mountpoint-policy" --policy-document file://iam-policy.json
     ```

   - The `iam-policy.json` file should contain the necessary permissions for accessing your S3 bucket.

---

### 4. **Create an IAM OIDC Provider for the EKS Cluster**

   - Get the OIDC issuer URL for your EKS cluster:
     ```bash
     aws eks describe-cluster --name <cluster_name> --query "cluster.identity.oidc.issuer" --output text
     ```

   - List the OIDC providers to confirm the provider ID:
     ```bash
     aws iam list-open-id-connect-providers | grep <EXAMPLE_ID>
     ```

   - Associate the IAM OIDC provider with your EKS cluster:
     ```bash
     eksctl utils associate-iam-oidc-provider --cluster <cluster_name> --approve
     ```

---

### 5. **Create an IAM Role and Service Account**

   - Create an IAM service account and attach the necessary policy for the S3 mount:
     ```bash
     eksctl create iamserviceaccount --name s3-mount-sa --namespace s3-mount --cluster <cluster_name> --role-name <role_name> --attach-policy-arn arn:aws:iam::<account-id>:policy/aws-s3-mountpoint-policy --approve
     ```

---

### 6. **Install Mountpoint for Amazon S3 CSI Driver**

   - Deploy the Mountpoint for Amazon S3 CSI driver to your cluster to allow mounting S3 buckets to EKS pods.

---

### 7. **Deploy a Sample Application with S3 Mount**

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

   - Mount the S3 bucket to the desired directory in your pod:
     ```bash
     mount-s3 aws-s3-mountpoint-eks-01 /s3-mountpoint
     ```

---

### 10. **Test the Setup**

   - Verify that the application running on the pod can successfully interact with the mounted S3 bucket by checking the output files.

---

### 11. **Cleaning Up**

   - After testing, delete the resources to clean up:
     - Delete the EKS cluster.
     - Remove the S3 bucket.
     - Delete IAM roles, policies, and service accounts.
