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







