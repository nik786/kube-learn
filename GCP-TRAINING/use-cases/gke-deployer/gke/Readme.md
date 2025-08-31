
```
terraform init -upgrade
terraform plan --var-file=dev.tfvars
terraform apply --var-file=dev.tfvars

terraform plan --var-file=dev.tfvars
terraform apply --var-file=dev.tfvars

gcloud auth login
gcloud config set project gl-cloud-469513
gcloud config set compute/region asia-south1
gcloud container clusters get-credentials dev-gke-cluster --region asia-south1 --project gl-cloud-469513
gcloud auth activate-service-account --key-file=/home/nik/Desktop/keys/gl-cloud-469513-2cd390141205.json
gcloud components install gke-gcloud-auth-plugin
export USE_GKE_GCLOUD_AUTH_PLUGIN=True
kubectl get nodes
gcloud container clusters get-credentials dev-gke-cluster --region asia-south1 --project gl-cloud-469513
kubectl get nodes

```
