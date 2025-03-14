
```

Task 1: Show current state (CLI Operation)
Task 2: Show state file location
Task 3: View/Update Terraform local backend configuration
Task 4: Modify, Plan and Execute Changes
Task 5: Show New State and State Backup


```


```

terraform state list
terraform state show aws_instance.web_server_2


terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}


```

- [local](https://github.com/btkrausen/hashicorp/blob/master/terraform/Hands-On%20Labs/Section%2008%20-%20Implement%20and%20Maintain%20State/01%20-%20Terraform_State_Default_Local_Backend.md)
