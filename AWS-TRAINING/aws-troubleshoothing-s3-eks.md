

An S3 bucket cross-region replication is not working. What could be wrong?

| Possible Issue                      | Explanation and Fix |
|--------------------------------------|---------------------|
| **Missing IAM Permissions**          | Ensure the IAM role used for replication has `s3:ReplicateObject`, `s3:ReplicateDelete`, and `s3:ReplicateTags` permissions. The role should be allowed in both source and destination buckets. |
| **Replication Not Enabled**          | Check if replication is enabled in the source bucket settings. Go to the AWS S3 console or verify via AWS CLI. |
| **Source Bucket Versioning Disabled** | S3 CRR requires versioning to be enabled on the source bucket. Enable it in the bucket properties. |
| **Destination Bucket Versioning Disabled** | The destination bucket must also have versioning enabled. Verify and enable it if necessary. |
| **Objects Already in Bucket**        | S3 CRR only applies to new objects after replication is set up. It does not replicate existing objects automatically. Use `s3 sync` to copy existing data. |
| **Wrong Destination Bucket Region**  | Ensure the destination bucket is in a different AWS region from the source bucket. CRR does not work within the same region. |
| **S3 Bucket Policy Issues**          | Check if the destination bucket policy allows replication access from the source bucket’s IAM role. |
| **KMS Encryption Issues**            | If the source bucket uses SSE-KMS encryption, the replication IAM role must have permission to decrypt using the KMS key. Update the KMS policy to allow access. |
| **Replication Rule Filtering Issues** | If using prefix or tag-based filtering, verify that objects meet the filter criteria. |
| **Replication Status Delayed**       | AWS S3 replication is not instantaneous. Check CloudWatch logs for replication status and any errors. |
| **Eventual Consistency Delays**      | Newly created objects may take time to appear in the destination bucket due to eventual consistency in S3. Wait and retry. |
| **S3 Object Lock Enabled**           | If Object Lock is enabled, replication might fail due to write restrictions on the destination bucket. |
| **Destination Bucket Does Not Exist** | Ensure the destination bucket exists and is accessible. |
| **AWS Service Quotas**               | Check if you’ve hit any AWS service quotas related to replication or API request limits. |



An EKS cluster node is not joining the cluster. How do you debug?

| Possible Issue                         | Debugging Steps & Fix |
|----------------------------------------|----------------------|
| **IAM Role Issues**                     | Ensure the node IAM role has `AmazonEKSWorkerNodePolicy`, `AmazonEC2ContainerRegistryReadOnly`, and `AmazonEKS_CNI_Policy`. Check with `aws iam get-role --role-name <role-name>`. |
| **Node Group Not Created Properly**     | Verify the managed or self-managed node group is created correctly. Use `aws eks describe-nodegroup --cluster-name <cluster-name> --nodegroup-name <nodegroup-name>`. |
| **Instance Profile Missing**            | Ensure the correct instance profile is attached to the worker nodes. Run `aws ec2 describe-instances --filters Name=tag:eks-nodegroup-name,Values=<nodegroup-name>`. |
| **Security Group Misconfiguration**     | Check if the node security group allows inbound/outbound traffic on required ports (443, 10250, 10255, 30000-32767 for services). |
| **Subnet Not Correctly Tagged**         | Ensure subnets have `kubernetes.io/role/elb=1` and `kubernetes.io/cluster/<cluster-name>=shared` tags. |
| **Cluster Autoscaler Issues**           | If using autoscaling, ensure the `ClusterAutoscaler` has permissions and is properly configured. |
| **Nodes Not in ‘Ready’ State**          | Run `kubectl get nodes` to check node status. If nodes are `NotReady`, check logs with `kubectl describe node <node-name>`. |
| **Kubelet Not Running**                 | SSH into the node and check kubelet logs: `sudo journalctl -u kubelet -f`. Restart if necessary. |
| **Bootstrap Script Issues**             | For self-managed nodes, check the `/var/log/bootstrap.log` file to see if the node bootstrapped correctly. |
| **Cluster API Server Not Reachable**     | Ensure worker nodes can reach the EKS API server. Run `curl -k https://<api-server-endpoint>` from the node. |
| **EC2 Instance Connectivity Issues**     | Ensure the EC2 instance has internet access or a NAT Gateway if needed. Test with `ping 8.8.8.8`. |
| **Amazon VPC CNI Not Working**          | Check CNI plugin logs using `kubectl logs -n kube-system -l k8s-app=aws-node`. |
| **Insufficient EC2 Instance Limits**    | Ensure you have not reached the AWS EC2 instance limits in your region. Check with `aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A`. |
| **Incorrect Kubernetes Version**        | Ensure the node AMI version is compatible with the cluster's Kubernetes version. Check `aws eks describe-cluster --name <cluster-name>`. |
| **CoreDNS Not Running**                 | Run `kubectl get pods -n kube-system` and ensure `coredns` is in `Running` state. If not, check logs with `kubectl logs -n kube-system -l k8s-app=kube-dns`. |
| **Incorrect User Data in Launch Template** | If using a custom launch template, check the `UserData` section for bootstrapping errors. |

