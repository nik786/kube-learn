1. How will it affect the state file and current resources if someone accidentally removes the remote backend from a Terraform configuration?

terraform apply command will error out. You need to reinitialize Terraform again, and it will prompt you to 
migrate the existing remote state to the local backend so that it can still manage resources managed by the remote state.


2. I'm giving you a configuration block and you need to suggest the value of X to get ami-b374d5a5 as the selected_ami output.


variable "ami_map" {
  type = map
  default = {
    "us-east-1" = "ami-b374d5a5"
    "us-west-2" = "ami-fc0b939c"
  }
}
 
output "selected_ami" {
  value = X
}


ans: var.ami_map["us-east-1"]

3.  What is input variables?
    Input variables in Terraform are parameters that let you pass dynamic values into your configuration so you can reuse the same code with different settings

   terraform apply -var="instance_type=t3.small"

   Input variables let you inject values into Terraform so you don’t hard-code anything and can reuse the same code for dev, staging, production, etc.

4. What is the purpose of the terraform state command?

   Advanced state management
   Modifying or updating the Terraform state.
   Moving items in or out of a Terraform state.


6. As given below, Glenn has created a variable of the boolean type. Select all accepted input from the options given below.

variable "set_password" {
  type = bool
  default = ?
}

which one you can put b/w  
false/"false"/none/both

Terraform language will automatically convert string values to bool values when needed, 
and vice-versa as long as the string contains a valid representation of a boolean value.


   

7. If you remove resources from the Terraform state, they will be physically destroyed from real-world infrastructure.

   Items removed from the Terraform state are not physically destroyed. Items removed from the Terraform state are only no longer managed by Terraform.
    terraform state rm 'aws_instance.vm'

9. What will be the value of the output lucky_user?

  variable "users" {
  type    = list(string)
  default = ["Peter", "Lois", "Brian", "Meg"]
}
 
output "lucky_user" {
  value = element(var.users, 4)
}
   

element retrieves a single element from a list. (zero-based index)

element(["a", "b", "c"], 1)
b

10. How can you export Terraform debug logs to the file?
    export TF_LOG_PATH="/var/log/terraform.log"


11. Which command can be used to inspect a plan file to ensure that the planned operations are expected?



 12. Does Child modules automatically inherit additional provider configurations?

    no
    Additional provider configurations (those with the alias argument set) are never inherited 
    automatically by child modules, and so must always be passed explicitly using the providers map.

    
     
        







   
