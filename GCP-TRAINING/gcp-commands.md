
```

gitlab-runner start

gcloud auth login


 gcloud config set project  cloud-base-001-457312 
 gcloud storage buckets create gs://prodwovenui.ardhanginidesigns.com   --project=cloud-base-001-457312   --location=asia
 
 gcloud domains list-user-verified

 gcloud auth activate-service-account  --key-file=/home/nik/Desktop/keys/cloud-base-001-457312-30cf611bf9f0.json
 gcloud components update

gcloud compute instances create my-instance
gcloud compute instances list
gcloud config list
gcloud compute zones list
gcloud compute regions list
gcloud compute machine-types list

gcloud compute machine-types list --filter="zone:us-cental1-b"




[gcloud installation]

export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
apt-get update && sudo apt-get install google-cloud-sdk




[gcloud basic commands]

gcloud compute images list | awk '{print $3}'  | awk '!a[$0]++'
gcloud iam service-accounts list


gcloud auth login --no-launch-browser
gcloud auth activate-service-account  --key-file=/opt/gcp-creation-playbook/connet.json
gcloud auth activate-service-account  --key-file=connector-2-31-Aug-2020.json
gcloud auth activate-service-account  --key-file=connector-2-31-Aug-2020-tf-admin.json

gcloud auth list
gcloud config set account conne@conn.iam.gserviceaccount.com

gcloud projects list
gcloud config set project conn
gcloud compute images list
gcloud compute regions list




gcloud init
gcloud config set project terra-test
gcloud config set region/us-east1
gcloud config set compute/zone us-east1-b/c
gcloud compute ssh compute-instance-0 --internal-ip





#export GCP_AUTH_KIND=serviceaccount
#export GCP_SERVICE_ACCOUNT_EMAIL='36@gmail.com'
export GCP_SERVICE_ACCOUNT_FILE='/opt/sa/con.json'
#export GCP_SCOPES='https://www.googleapis.com/auth/compute'
export GOOGLE_APPLICATION_CREDENTIALS='/opt/sa/con.json'





[ssh]

ssh-keygen -t rsa -f google_cloud_bastion -C 36



[Install Ruby 2.6]

apt-add-repository ppa:brightbox/ruby-ng
apt-get update
apt-get install ruby2.6 ruby2.6-dev

[Install landscape]

gem install terraform_landscape



[tf]
wget https://releases.hashicorp.com/terraform/0.11.8/terraform_0.11.8_linux_amd64.zip


terraform plan -out=tfplan.tfstate -lock=false
terraform destroy -target=google_compute_instance_group.web-nodes -lock=false
terraform destroy -target=module.gce-lb-http --auto-approve -lock=false && terraform apply --auto-approve -lock=false
terraform plan -out=tfplan.tfstate -lock=false
terraform force-unlock 1567779469142061
terraform init
terraform plan
terraform plan  -out=tfplan
terraform apply
terraform destroy
terraform output instance_ips
terraform output -json instance_ips | jq '.value[0]'
terraform apply \
 -var-file="secret.tfvars" \
 -var-file="production.tfvars"








provisioner "local-exec" {
   command = "ansible-playbook -u sudipta1436 -i '${self.network_interface.0.network_ip},' --private-key /opt/gcp-tera-ansible/google_cloud_bastion  file.yml"
}


provisioner "local-exec" {
   command = "ansible-playbook -u sudipta1436 -i ./gce.py file.yml --extra-vars node='${self.network_interface.0.network_ip}'"
}




boot_disk {
    initialize_params {
      image = "${var.os}"
    }
  }




root@controller:/opt/gcp-tera-ansible# cat output.tf 
output "public_instance_ip" {
  value = ["${google_compute_instance.bastion-instance.network_interface.0.access_config.0.nat_ip}"]
}


output "private_instance_ip" {
  value = ["${google_compute_instance.compute-instance.network_interface.0.network_ip}"]
}








gcloud source repos create helloworld-image-factory



output "private_instance_ip" { value = ["${google_compute_instance.pri-instance.network_interface.0.network_ip}"] }








Enable AppEngine Admin API/AppEngine Fexible API



[ansible]
export GCE_INI_PATH=/opt/gcp-tera-ansible/inventory/dynamic/gce.ini
./gce.py --list
ansible -i inventory.gcp.yml --private-key=/opt/gcp-tera-ansible/google_cloud_bastion -u su36 -m ping all
ansible -i ./gce.py --private-key=/opt/gcp-tera-ansible/google_cloud_bastion -u su36 -m ping 146.148.34.217
ansible -i ./gce.py --private-key=/opt/gcp-tera-ansible/google_cloud_bastion -u su36 -m ping bastion-instance
ansible-playbook -i ./gce.py --private-key=/opt/gcp-tera-ansible/google_cloud_bastion -u su36 helo.yml
ansible-playbook -i ./gce.py helo.yml --extra-vars "node=compute-instance-0"



[playbook]

---
- hosts: dev
  become: true
  become_user: root
  become_method: sudo
  tasks:
      - name: print tf output
        shell: terraform plan | landscape --no-color
        args:
          chdir: /etc/ansible/scripts/terraform-stack/gcp/gcp-without-lb
        register: tdata
      - debug: msg="{{ tdata.stdout }}"
      - name: terraform plan
        terraform:
          project_path: '/etc/ansible/scripts/terraform-stack/gcp/gcp-without-lb'
          plan_file: '/etc/ansible/scripts/terraform-stack/gcp/gcp-without-lb/tfplan'
          lock: true
          state: planned
          force_init: true
        register: tf
      #- debug: var=tf.stdout




[pip]

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install --upgrade requests
pip install --ignore-installed six
pip install launchpadlib
pip install apache-libcloud
pip install requests google-auth
pip install certifi


[GO] 
curl -O https://storage.googleapis.com/golang/go1.11.2.linux-amd64.tar.gz
export GOROOT=/opt/go
export GOPATH=$HOME/go
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin


/opt/bin/tf/1.3.5/terraform plan -var-file=dev.tfvars -out=devtfplan
/opt/bin/tf/1.3.5/terraform apply devtfplan
/opt/bin/tf/1.3.5/terraform plan
/opt/bin/tf/1.3.5/terraform workspace list
/opt/bin/tf/1.3.5/terraform workspace new stage
/opt/bin/tf/1.3.5/terraform workspace select stage

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






#aws elbv2 create-rule \
#    --listener-arn arn:aws:elasticloadbalancing:us-east-1:931471864539:listener/app/plato-sit-alb/0dffa8ccbffbb271/3a86e8bfffd30b55 \
#    --priority 100 \
#    --actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:931471864539:targetgroup/plato-sit-tg/b98c6a3666b14bb1 \
#    --conditions Field=path-pattern,Values=/v1/*



#aws autoscaling attach-load-balancer-target-groups --auto-scaling-group-name plato_sit_asg --target-group-arns arn:aws:elasticloadbalancing:us-east-1:931471864539:targetgroup/plato-sit-tg/b98c6a3666b14bb1




load_balancer_arn=$(aws elbv2 describe-load-balancers --query "LoadBalancers[0].LoadBalancerArn" --output text)

# Print the load balancer ARN
echo "$load_balancer_arn"

target_group_arn=$(aws elbv2 describe-target-groups --query "TargetGroups[0].TargetGroupArn" --output text)

# Print the target group ARN
echo "$target_group_arn"


aws elbv2 create-listener --load-balancer-arn $load_balancer_arn \
--protocol HTTP --port 80  \
--default-actions Type=forward,TargetGroupArn=$target_group_arn


terraform destroy -var-file=vars_oat.tfvars

vpc peering

route_table: plato_sit_public_rt
Destination     Target
0.0.0.0/0	igw-04fef28bcb60be028
10.0.0.0/16	local
10.1.0.0/16	pcx-06bb93bbae0e830d7


route_table: plato_oat_public_rt
Destination     Target
0.0.0.0/0	igw-055ce26e2ec8c5c66
10.0.0.0/16	pcx-06bb93bbae0e830d7
10.1.0.0/16	local



terraform import aws_s3_bucket.my_bucket connector-09


ubectl get configmap aws-auth -n kube-system -o yaml

aws configure --profile eks-admin-02
aws configure --profile plato_ai

aws eks update-kubeconfig --name plato-sit-cluster --region us-east-1 --profile eks-admin-01
aws eks update-kubeconfig --name plato-sit-cluster --region us-east-1 --profile eks-admin-02
aws eks update-kubeconfig --name t7 --region us-east-1 --profile eks-admin-02


./kubectl edit configmap aws-auth -n kube-system



https://931471864539.signin.aws.amazon.com/console

eks-admin-02




ssh -i pla ubuntu@34.201.5.42




aws eks update-kubeconfig --name plato-sit-cluster --region us-east-1 --profile eks-admin-02 --role-arn arn:aws:iam::931471864539:role/plato-sit-cluster-cluster-20240108152102362900000001

curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.23.6/bin/linux/amd64/kubectl


 

aws eks describe-cluster --name plato-sit-cluster --region us-east-1



kubectl get po



curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.3/2023-11-14/bin/darwin/amd64/kubectl

kubectl get po 








kubectl version --client

kubectl version


ssh -i plato_key.pem ec2-user@54.175.168.245

ssh -i plato_key.pem ubuntu@44.203.6.180



kubectl version --short --client


aws sts get-caller-identity
aws sts get-caller-identity --profile eks-admin-02


eksctl get iamidentitymapping --cluster plato-sit-cluster

aws iam get-user --user-name eks-admin-02


aws_auth_users = var.eks_aws_auth_users



tags = {
        Name                                                = "eks-node-group-instance-name"
        "k8s.io/cluster-autoscaler/node-template/label/env" = "test"
      }


 aws s3api list-buckets --query 'Buckets[?Name==`connector-09`].{ID:Name}' --output json
[
    {
        "ID": "connector-09"
    }
]


terraform import aws_instance.test3 i-058531f7573a7043b
terraform state rm aws_instance.test
terraform import module.vpc.aws_vpc.this <VPC ID>

terraform plan -generate-config-out=generated_resources.tf

terraformer import aws --resources=aws_instance,aws_s3_bucket,aws_db_instance

terraform graph | dot -Tpng > /tmp/graph.png


git checkout main
git merge --squash feature-branch
git commit -m "Feature: New functionality"



Squash merge is a type of merge strategy where all the changes from a feature branch are condensed 
into a single commit before merging into the target branch. This helps to keep the commit 
history clean and avoids a long list of small, incremental commits in the main branch



Rebasing is a different operation that involves moving or combining a sequence of 
commits to a new base commit. This can be used to integrate changes from one branch into another, 
often to create a linear, more readable commit history


git checkout feature-branch
git rebase main


Squash Merge: Primarily used to condense multiple commits into a single commit for the 
sake of cleanliness in the main branch's history.

Rebasing: Used to create a linear history by moving or combining commits from one branch onto another.

vault secrets enable -path=secret kv
vault kv put secret/myapp/config username=admin password=s3cr3t

provider "vault" {
  address = "http://127.0.0.1:8200"
  token   = "your_vault_token"
}


data "vault_generic_secret" "myapp_config" {
  path = "secret/myapp/config"
}

resource "some_resource" "example" {
  username = data.vault_generic_secret.myapp_config.data["username"]
  password = data.vault_generic_secret.myapp_config.data["password"]
  # Other resource configurations...
}


provider "vault" {
  address = "http://127.0.0.1:8200"
  token   = file("~/.vault-token")
}


export VAULT_TOKEN=my_secure_token


docker tag py_app_alpha:01 891377203384.dkr.ecr.ap-south-1.amazonaws.com/ag-ecr:01


aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 891377203384.dkr.ecr.ap-south-1.amazonaws.com

docker push 891377203384.dkr.ecr.ap-south-1.amazonaws.com/ag-ecr:01

```














