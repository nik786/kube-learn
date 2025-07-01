

```
terraform plan -var-file=dev.tfvars -out=devtfplan
terraform apply devtfplan
terraform plan
terraform workspace list
terraform workspace new stage
terraform workspace select stage

terraform workspace new sit; 
terraform workspace select sit 
terraform plan -var-file=sit.tfvars -out=sittfplan -input=false -lock=false

terraform workspace select sit
terraform plan -var-file=

terraform plan -var-file=vars_sit.tfvars

terraform plan  --var-file=vars_sit.tfvars -out=sittfplan
terraform apply --var-file=vars_sit.tfvars
terraform apply --var-file=vars_sit.tfvars -input=false

terraform apply --var-file=vars_sit.tfvars -input=false -var environment_name=sit

terraform init -backend-config=backend.hcl --reconfigure
terraform init -backend-config=backend.tfvars


terraform init -reconfigure -backend-config=backend.tfvars
terraform workspace select sit
terraform plan  --var-file=vars_sit.tfvars -out=sittfplan
terraform apply --var-file=vars_sit.tfvars -input=false


terraform apply --var-file=vars_$env.tfvars -auto-approve -input=false



terraform workspace select oat
terraform plan  --var-file=vars_oat.tfvars -out=oattfplan
terraform apply --var-file=vars_oat.tfvars -input=false
terraform plan -var-file=vars_sit.tfvars -out=sittfplan -input=false -lock=false
terraform apply -var-file=vars_sit.tfvars  -input=false -auto-approve
terraform graph | dot -Tpng -o /tmp/graph_02.png
terraform destroy -var-file=vars_sit.tfvars  -input=false -auto-approve
terraform graph | dot -Tpng > graph.png

terraform apply -var "cloudflare_email=service@email.com" -var "cloudflare_token=TOKEN_STRING" -var "do_token=${DO_PAT}" -var "token=TOKEN_string -var "email=another@email.com"



##eks-test

terraform init -configure -backend-config=backend.tfvars

terraform plan -var-file=dev.tfvars -out=devtfplan -input=false -lock=false

terraform plan -var-file=dev.tfvars -out=devtfplan -input=false -lock=false

terraform apply -var-file=dev.tfvars  -input=false

Once the EKS cluster is created, log in to the AWS Console as the eks-admin user and configure the access entry for the cluster.


https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html

curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.7/2025-04-17/bin/linux/amd64/kubectl

aws eks update-kubeconfig --region us-east-1 --name gl-dev


curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh


grep -rl "m6i.large" . | xargs sed -i 's/m6i\.large/t3.small/g'

grep -r "m6i.large" .




##tf-labs

terraform login

terraform plan

terraform apply



```


```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyLargeInstanceTypes",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "*",
      "Condition": {
        "StringNotEqualsIfExists": {
          "ec2:InstanceType": [
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium"
          ]
        }
      }
    }
  ]
}


```







