

```

Task 1: Terraform backend block
Task 2: Partial backend configuration via a file
Task 3: Partial backend configuration via command line
Task 4: Declare backend configuration via interactive prompt
Task 5: Specifying multiple partial backend configurations
Task 6: Backend configuration from multiple locations
Task 7: Change state backend configuration back to default

```

```

terraform init -backend-config="path=state_data/terraform.prod.tfstate" -migrate-state

terraform init -backend-config=state_configuration/s3-state-bucket.hcl \
-backend-config=state_configuration/prod-s3-state-key.hcl \
-migrate-state


```

```

terraform {
  backend "s3" {
    bucket = "my-terraform-state-ghm"
    key    = "dev/aws_infra"
    region = "us-east-1"
  }
}

```


 - [backend-config](https://github.com/btkrausen/hashicorp/blob/master/terraform/Hands-On%20Labs/Section%2008%20-%20Implement%20and%20Maintain%20State/08%20-%20Terraform_Backend_Configuration.md)
 
 - [backend-storage](https://github.com/btkrausen/hashicorp/blob/master/terraform/Hands-On%20Labs/Section%2008%20-%20Implement%20and%20Maintain%20State/04%20-%20Terraform_State_Backend_Storage.md) 

 - [enahnced-backend](https://github.com/btkrausen/hashicorp/blob/master/terraform/Hands-On%20Labs/Section%2008%20-%20Implement%20and%20Maintain%20State/05%20-%20Terraform_Remote_State_Enhanced_Backend.md)
 
 - [backend-auth](https://github.com/btkrausen/hashicorp/blob/master/terraform/Hands-On%20Labs/Section%2008%20-%20Implement%20and%20Maintain%20State/03%20-%20Terraform_State_Backend_Authentication.md) 



