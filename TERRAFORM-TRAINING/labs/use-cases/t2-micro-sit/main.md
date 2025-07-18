## Write terraform code to deploy t2.micro instance when environment is sit and t2.small when environment is uat



```

# Define the environment variable
variable "environment" {
  description = "Environment where the EC2 instance will be deployed (sit or uat)"
  type        = string
  default     = "sit"  # Optional: You can remove this if you want to pass it during runtime
}

# AWS provider configuration (replace with your region)
provider "aws" {
  region = "us-east-1"  # Specify your region
}

# EC2 instance resource
resource "aws_instance" "example" {
  ami           = "ami-12345678"  # Replace with a valid AMI for your region
  instance_type = var.environment == "sit" ? "t2.micro" : "t2.small"

  # Other instance configuration
  tags = {
    Name = "example-instance-${var.environment}"
  }
}

# Outputs (Optional)
output "instance_type" {
  description = "The EC2 instance type used"
  value       = aws_instance.example.instance_type
}

terraform apply -var="environment=sit"

ternary conditional operator

```
