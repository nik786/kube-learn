/opt/bin/tf/1.3.5/terraform plan -var-file=dev.tfvars -out=devtfplan
terraform apply --var-file=dev.tfvars -auto-approve -input=false
