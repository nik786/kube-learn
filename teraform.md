## What are the use cases of Terraform?
-----------------------------------------------

1. Multi-Tier Applications
2. Self-Service Cluster
3. Disposable Environment
4. Software Defined Networking
5. Resource Schedulers
6. Multi-Cloud Deployment


Terraform — 5 Ways To Create Infrastructure in Multiple Environments
-------------------------------------------------------------------------------

1. Using Folders — Method 1
2. Using Folders — Method 2
3. Workspaces
4. Modules
5. Terragrunt<br><br>


What is the Terraform State and what is its purpose?
------------------------------------------------------

It is a file which keeps track of the current state of infrastructure managed by Terraform. <br><br>
The state file is a JSON-formatted file that records information about the resources created and managed by Terraform, their attributes, dependencies, and other metadata.

# Terraform State File: Key Functions

| **Function**            | **Description**                                                                                                                             |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Resource Tracking**    | The state file maintains a record of all resources created and managed by Terraform, along with their current configurations and state.     |
| **Dependency Management**| Terraform uses the state file to understand the relationships and dependencies between different resources.                                 |
|                          | This ensures the correct order of resource creation, modification, and deletion.                                                          |
| **Preventing Resource Drift** | The state file helps detect and prevent resource drift, which occurs when the actual state of resources in the cloud deviates from the expected state. |
|                          | Terraform compares the desired state with the actual state and determines if any changes are necessary.                                   |
| **Concurrency Control**  | The state file provides a mechanism for Terraform to manage concurrency and coordinate operations when multiple users or automation processes are making changes. |



How do you constrain the provider version?
---------------------------------------------

To constrain the provider version as suggested, add a required_providers block inside a terraform block:

terraform {
  required_providers {
    aws = "~> 1.0"
  }
}


How do you configure Multiple Provider Instances?
---------------------------------------------------
alias



Why do we need Multiple Provider instances?
---------------------------------------------

Some of the example scenarios:a. multiple regions for a cloud platform
targeting multiple Docker hosts
multiple Consul hosts, etc.



 How do you configure Multiple Provider Instances?
 -----------------------------------------------------
```
provider "aws" {
  alias   = "aws1"
  region  = "us-west-1"
  access_key = "your_access_key"
  secret_key = "your_secret_key"
}

provider "aws" {
  alias   = "aws2"
  region  = "us-east-1"
  access_key = "your_access_key"
  secret_key = "your_secret_key"
}


resource "aws_instance" "web_instance_1" {
  provider = aws.aws1
  # other resource configurations
}

resource "aws_instance" "web_instance_2" {
  provider = aws.aws2
  # other resource configurations
}

```




How do you configure Multiple versions?
-----------------------------------------

Use Terraform Version Constraints:
In your Terraform configurations, you can specify a required Terraform version using the required_version block.

terraform {
  required_version = ">= 0.14, < 0.15"
}


Install tfenv
-------------------
git clone https://github.com/tfutils/tfenv.git ~/.tfenv

echo 'export PATH="$HOME/.tfenv/bin:$PATH"' >> ~/.bashrc

Install a specific version
------------------------------
tfenv install 0.14.7

**Use a specific version in your project directory**
------------------------------------------------------
tfenv use 0.14.7




What is Provider Plugin Cache?
--------------------------------
# Terraform Provider Plugin Cache

| **Concept**              | **Description**                                                                                                                                                          |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Provider Plugin Cache** | The Provider Plugin Cache is a mechanism in Terraform that caches and reuses provider plugins. These plugins are executable binaries responsible for interfacing with specific infrastructure platforms or services. |
| **Benefits**              | The cache improves efficiency by reducing the need to repeatedly download provider plugins, especially in environments with multiple users or CI/CD pipelines. It minimizes network requests and speeds up the initialization process. |




Define Terraform init?
------------------------
Terraform initializes the code using the command terraform init. 
This command is used to initialize the working directory containing Terraform configuration files. It is safe to run this command multiple times.

You can use the init command for:

Plugin Installation
Child Module Installation
Backend Initialization








How does Terraform help in discovering plugins?
-------------------------------------------------

The authority “Terraform init” helps Terraform interpret configuration files in the operational directory. Then, Terraform finds out the essential plugins and searches for installed plugins in 
diverse locations. In addition, Terraform also downloads extra plugins at times. Then, it decides the plugin versions to use and writes a security device file for ensuring that Terraform will employ the identical plugin versions


Define Modules in Terraform?
------------------------------
# Terraform Modules

| **Module Type**    | **Description**                                                                                                                                                           | **Example**                                                              |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Module**         | A module in Terraform is a collection of multiple resources that are used together. Modules help in organizing and reusing Terraform configurations.                        | `module "network" { source = "./modules/network" }`                      |
| **Root Module**    | The root module is the primary module where Terraform execution begins. It includes configuration files in the working directory and orchestrates infrastructure resources, potentially calling child modules. | The root module consists of the main configuration files such as `main.tf`, `variables.tf`, etc. |




| **Aspect**                | **Description**                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------|
| **Definition**            | The top-level module in a Terraform configuration, loaded by default from the working directory. |
| **Components**            | Consists of all `.tf` files in the working directory (e.g., `main.tf`, `variables.tf`, `outputs.tf`). |
| **Purpose**               | Serves as the starting point for `terraform plan` and `terraform apply` commands.                 |
| **Structure**             | - `main.tf`: Defines resources. <br> - `variables.tf`: Declares input variables. <br> - `outputs.tf`: Specifies output values. <br> - `provider.tf`: Configures providers. <br> - `backend.tf`: Configures state backend. |
| **Child Module Interaction** | Calls child modules using the `module` block to organize and modularize configurations.           |
| **Execution Context**     | The root module is the context where Terraform commands are executed.                             |
| **State Representation**  | Resources from the root module and its child modules are recorded in the Terraform state.         |
| **Example**               | ```hcl<br>provider "aws" { region = "us-east-1" }<br>resource "aws_instance" "example" {<br>  ami = "ami-12345678"<br>  instance_type = "t2.micro"<br>}<br>``` |
| **Best Practice**         | Keep the root module clean and delegate reusable or complex logic to child modules.               |



What are the ways to lock Terraform module versions?
-----------------------------------------------------
# Terraform Module Sources

| **Source**                   | **Description**                                                                                                                                                     | **Example**                                                                                                        |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Terraform Module Registry** | You can use the Terraform Module Registry as a source and specify the `version` attribute in your module configuration to fetch a specific version of the module.   | `module "example" { source = "terraform-module-registry/module-name" version = "1.0.0" }`                         |
| **GitHub Repository**         | If using a GitHub repository as a source, specify the branch, version, and query string using `?ref` to reference a specific commit, tag, or branch.                  | `module "example" { source = "github.com/user/repo?ref=branch-name" }`                                           |



# Terraform Concepts

| **Concept**                | **Description**                                                                                                                                                                                                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **State File Locking**      | State file locking is a mechanism in Terraform to avoid conflicts when multiple users attempt operations on the same state file. It blocks operations on the state file until the current lock is released. It helps prevent corruption of the state file. Locking happens in the backend, and if acquiring a lock takes too long, a status message will be shown. |
| **Tainted Resource**        | Tainted resources are those marked for destruction and recreation during the next apply command. The resource remains unchanged in the infrastructure, but the state file is updated to reflect the taint. After marking a resource as tainted, Terraform will show that it will be destroyed and recreated on the next apply.  |
| **Terraform Refresh**       | The `terraform refresh` command updates the state file with the most current information about the resources managed by Terraform. It doesn’t make any changes to infrastructure but ensures that the state file reflects the current state of the resources. It is used when the state file is out of sync with the actual infrastructure. |
| **Terraform Provider**      | A "provider" in Terraform is a configuration block that connects to specific cloud or service providers. It defines how resources will be created and managed in the target infrastructure. Providers are key components in Terraform configurations.                                                   |
| **Terraform Drift**         | Terraform drift refers to changes made outside of Terraform’s management, which causes a mismatch between the actual infrastructure state and the state tracked by Terraform. This results in drift between the current infrastructure and Terraform's state.                                                    |
| **Null Resource**           | The `null_resource` is a no-op resource in Terraform, meaning it doesn’t directly create or manage infrastructure. It can be used to run local provisioners like scripts or commands on the local machine where Terraform is executed, instead of on remote resources.                                                 |










What does the following command do?
--------------------------------------

| Command           | Description                                                          |
|-------------------|----------------------------------------------------------------------|
| `terraform version` | Check the installed version of Terraform                              |
| `terraform destroy` | Destroy the managed infrastructure in Terraform                      |
| `terraform fmt`    | Rewrites configuration files in a canonical style and format         |
| `terraform providers` | Displays information about the providers working in the current configuration |
| `terraform apply`  | Builds or changes infrastructure according to the plan               |
| `terraform console`| Interactive console for Terraform interpolations                      |
| `terraform destroy`| Destroy Terraform-managed infrastructure                             |
| `terraform env`    | Manages workspaces                                                    |
| `terraform get`    | Downloads and installs modules for the configuration                 |
| `terraform graph`  | Builds a visible graph of Terraform resources                        |
| `terraform import` | Imports existing infrastructure into Terraform                        |
| `terraform init`   | Initializes a Terraform working directory                            |
| `terraform output` | Reads output from a state file                                        |
| `terraform plan`   | Generates and shows an execution plan                                 |
| `terraform validate` | Validates the Terraform files                                       |
| `terraform version` | Prints the Terraform version                                          |
| `terraform workspace` | Manages workspaces                                                  |










Graphing - Its features of graphing that are built-in are helpful in visualizing the infrastructure.<br><br>
Custom Syntax - It's custom syntax is very friendly which aids in enhancing efficiency.<br><br>
Resource Relationships - A very beneficial feature of terraforming is that it is able to understand resource relationships.<br><br>
Updates - The updates and features are added by the Open Source Project. It does so with a group of lots of contributors.<br><br>
Improved Maintenance - It is capable of breaking down the configuration into small parts or chunks for improving the organization and the maintenance.<br><br>














DynamicBlock
----------------

A dynamic block is used inside resource or module blocks to dynamically construct nested configuration blocks. 

- [dynamic-block](https://github.com/infra-ops/aws-tr-repo/blob/master/aws-generic/as/dynamic-block.tf)


vault
------

- [vault-provider](https://github.com/infra-ops/aws-tr-repo/blob/master/aws-generic/as/vault.tf)

Local
------
| **#** | **Feature**                | **Description**                                                                                   |
|-------|----------------------------|---------------------------------------------------------------------------------------------------|
| **1** | Local Variables in Terraform | Simplify expressions and calculations within a module by defining intermediate values.            |
| **2** | Avoid Redundant Code        | Help eliminate repetitive code by reusing intermediate values in different parts of the configuration. |
| **3** | Enhance Code Clarity        | Keep complex expressions clear and manageable, improving overall readability.                     |
| **4** | Improve Maintainability     | Facilitate updates and modifications by centralizing logic in local variables.                    |















List
------
Definition: A list in Terraform is a sequence of values. It can contain multiple elements of the same type or different types. Lists are ordered, meaning the order of elements is significant, and you can access elements by their index.
Syntax: You can create a list using square brackets:
variable "my_list" {
          type = list(string)
          default = ["apple", "banana", "cherry"]
}

Element
--------
Definition: The element function in Terraform is used to retrieve a specific element from a list based on its index. 
It allows you to access an item in a list without directly using square bracket notation.

```tf
variable "zones"  { 
              type = list(string) 
              default = ["us-east-1a", "us-east-1b", "us-east-1c"] 
} 
output "first_zone" { 
             value = element(var.zones, 0) # Outputs "us-east-1a" }

```


List:
-------
An ordered collection of values.

Element:
----------

A function to retrieve a specific item from a list based on its index, which can wrap around if the index exceeds the list length.


 Count vs For_each
 ---------------------
 Basic Usage: count is a simpler way to specify the number of identical resources you want to create.



| Feature                          | `for_each`                                                                                       | `count`                                                   |
|----------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| **Definition**                   | Defined using a collection (list or map), creating an instance for each element in the collection.| Defined as a single integer, indicating the number of instances to create. |
| **Iteration Basis**              | Iterates over a collection, where each instance corresponds to an item in the collection.         | Iterates based on a fixed number specified by the count value. |
| **Indexing**                     | Accessed using `for_each.key` and `for_each.value`.                                               | Accessed using `count.index`, starting from 0.            |
| **Configuration**                | Allows each instance to have different configurations based on the collection item.               | All instances have the same configuration.                |
| **Resource Types**               | Can be used with resources of different types if structured in the iterable collection.           | Used only with resources of the same type and configuration. |
| **Use Case**                     | Dynamic set of inputs, where each instance may require different configurations.                  | Fixed number of identical resources.                      |


#### Flatten vs for_each
--------------------------


| Feature                | `flatten`                                                                                   | `for_each`                                                                                 |
|------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **Definition**         | Combines multiple lists into a single-level list, reducing nested lists.                    | Iterates over a collection (list or map) to create multiple resources with distinct configurations. |
| **Usage**              | Commonly used to flatten nested lists into a single list.                                   | Used in resource blocks to create multiple instances based on elements in the collection. |
| **Functionality**      | Accepts a variable number of arguments (lists) and concatenates them into a single list.    | Each instance can be accessed using `for_each.key` (for maps) or `for_each.value` (for lists). |
| **Result**             | Outputs a single list with all elements from input lists combined.                         | Each instance can have its own configuration based on the current item in the collection. |
| **Core Operation**     | Reduces nested lists.                                                                       | Iterates over a collection to create resources.                                           |


## Terraform vs Ansible
--------------------------


| Feature                         | Terraform                                                                                     | Ansible                                                                                     |
|---------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Primary Purpose**             | Infrastructure provisioning and management (e.g., provisioning a VPC, setting up an EC2 instance, configuring databases in the cloud). | Configuring and managing the software environment (e.g., installing packages, configuring web servers, ensuring correct firewall settings). |
| **Approach**                    | Declarative: Describes the desired state of infrastructure, and Terraform ensures it matches.| Imperative: Describes a series of tasks to execute in a specific order.                     |
| **State Management**            | Uses a state file (local or remote) to track infrastructure changes and manage drift detection.| No state file; relies on execution results from each run.                                   |
| **Idempotence**                 | Ensures infrastructure matches the desired state regardless of previous executions.          | Ensures repeated tasks result in the same outcome.                                          |
| **Agent Requirements**          | Agentless: Interacts directly with APIs of cloud providers or other services.                | Agentless: Uses SSH or WinRM for communication, with no agents required on target machines. |
| **Use Cases**                   | Provisioning infrastructure components like VPCs, EC2 instances, and cloud databases.        | Configuring systems, such as installing packages, setting up web servers, and managing firewalls. |



Terraform will execute up to 10 operations (such as creating, modifying, or destroying resources) simultaneously by default.

terraform apply -parallelism=20


| Feature               | `terraform fmt`                                       | `terraform validate`                                  |
|-----------------------|-------------------------------------------------------|------------------------------------------------------|
| **Purpose**           | Automatically formats Terraform configuration files to a standard style. | Validates the syntax and configuration of Terraform files. |
| **Effect on Files**   | Modifies files by reformatting the code (e.g., indentation, spacing). | Does not modify any files; it only checks for errors or issues. |
| **Error Detection**   | Does not check for logical errors; only checks formatting issues. | Checks for syntax errors, invalid references, and missing variables. |






# A client requests a Terraform setup where they can provision only specific subsets of resources on demand. How would you design such a solution?

| 01. Requirement                           | Solution                                                                                                                  |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| 01. Provision specific subsets of resources | Use **Terraform Modules** to group related resources logically. Modules allow clients to provision only the required subsets.|
| 02. Enable on-demand provisioning          | Implement `count` or `for_each` arguments in resources, enabling conditional creation based on user input variables.         |
| 03. Client-controlled selection            | Introduce **input variables** to allow clients to specify which resources (subsets) to provision, using flags or variable files. |
| 04. Example Setup                          | Create separate modules for resources (e.g., VPC, EC2, S3) and use conditionals: `count = var.enable_ec2 ? 1 : 0`.            |
| 05. Command to provision subsets           | Use Terraform commands like `terraform apply -var="enable_vpc=true" -var="enable_ec2=false"`, enabling selective provisioning.|





 # You’re tasked with deploying resources for a temporary project using Terraform. How would you ensure easy cleanup after the project ends?

| 01. Requirement                        | Solution                                                                                                             |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 01. Temporary resource deployment      | Use **Terraform workspaces** to isolate the resources for the project, making it easier to manage and clean up later.      |
| 02. Resource isolation                 | Organize resources within a dedicated **module** for the temporary project to keep them separate from other infrastructure.|
| 03. Ensure easy cleanup                | Apply `terraform destroy` in the specific workspace or directory to remove all resources associated with the temporary project.|
| 04. Command for cleanup                | Use `terraform workspace select <workspace_name>` to switch to the temporary project workspace, then run `terraform destroy`.|
| 05. Use of `-auto-approve` flag        | For automated cleanup, use `terraform destroy -auto-approve` to skip interactive approval during resource destruction.   |


# How would you prevent collaborators to accidentally overwriting each other’s changes. What strategies would you implement here?


| 01. Requirement                            | Solution                                                                                                                     |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 01. Prevent overwriting collaborators' changes | Use **Remote Backend** (e.g., S3 with state locking) to store the Terraform state file, ensuring that only one person modifies it at a time. |
| 02. Implement **State Locking**            | Enable state locking with backends like **DynamoDB** (for S3), preventing multiple users from making concurrent changes.    |
| 03. Use **Version Control**                | Store Terraform configuration in a **Git repository** and follow best practices for Git workflows (e.g., feature branches, pull requests). |
| 04. Collaborator Workflow                  | Establish a **clear Git branching model** (e.g., `main` for production, `dev` for development) to isolate changes and review before merging. |
| 05. Regular **Terraform Plan and Review**  | Encourage collaborators to run `terraform plan` and share outputs for review before applying changes, ensuring everyone is on the same page. |
| 06. Implement **Automated CI/CD**          | Set up **CI/CD pipelines** that run `terraform plan` automatically on pull requests to ensure changes are valid and won't conflict. |



# During a terraform apply, a resource failed to provision, but others succeeded. How would you roll back changes while maintaining consistency?

| 01. Requirement                              | Solution                                                                                                                   |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| 01. Rollback changes when resource fails     | Use **Terraform State Management** to manually remove the partially created resources using `terraform state rm <resource>`. |
| 02. Ensure consistency across resources      | Run `terraform plan` to check for inconsistencies and `terraform apply` to reapply changes, ensuring all resources are correctly provisioned. |
| 03. Use **Terraform Import** if necessary    | If a resource was partially created outside Terraform, use `terraform import` to import the resource back into the state file and manage it. |
| 04. Enable **Retry Mechanisms**              | Configure retry logic for provisioning resources that fail during `terraform apply` by using `timeouts` or manual retries for stability. |
| 05. Use **Terraform Workspaces** for isolation | Use different workspaces to isolate environments, making it easier to roll back changes and maintain consistency across environments. |
| 06. Apply incremental changes                | Make use of `-target` option with `terraform apply` to apply only the successful resources first, then address the failed ones in a separate run. |


# Your team wants to enforce compliance policies for resources deployed with Terraform (eg. tagging). How would you achieve this?

| 01. Requirement                                | Solution                                                                                                                       |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| 01. Enforce compliance policies                | Use **Terraform Sentinel** to enforce policies such as tagging, naming conventions, or other resource compliance rules.       |
| 02. Tagging enforcement                        | Implement a **policy as code** to enforce mandatory tags using Sentinel, ensuring every resource follows the required tag format. |
| 03. Centralized policy management             | Store compliance policies in a **shared repository** to ensure consistency across projects and teams.                        |
| 04. Validate compliance during Terraform plan | Use **Terraform Validate** in combination with Sentinel to check for policy violations before the actual deployment (e.g., missing tags). |
| 05. Monitor and report non-compliance         | Set up automated reports or use **Terraform Cloud** with Sentinel to track and notify teams of policy violations.             |
| 06. Custom compliance checks                  | Customize **Sentinel policies** based on your organization’s specific tagging or naming requirements to ensure compliance.      |



# How to handle a requirement to deploy the same infrastructure across multiple AWS regions using Terraform?

| **#** | **Requirement**                              | **Solution**                                                                                                                   |
|-------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **1** | Deploy same infrastructure across regions   | Use **Terraform Providers** with the `alias` argument to define multiple AWS regions in the configuration.                    |
| **2** | Create regional resources                   | Use `provider "aws"` blocks with different `region` values for each region where resources need to be deployed.               |
| **3** | Use modules for reusable infrastructure     | Encapsulate infrastructure components (like VPC, EC2, etc.) into **modules**, then call them for each region.                |
| **4** | Define region-specific variables            | Create region-specific variables (e.g., `vpc_name`, `instance_type`) and pass them to modules for dynamic infrastructure configuration. |
| **5** | Use `terraform plan` and `apply` separately | Execute `terraform plan` and `apply` per region to ensure the correct resources are deployed to the right regions.            |


Terragrunt 
-----------
It is a thin wrapper that provides extra tools for keeping configurations DRY, working with multiple Terraform modules, and managing remote state.

- [s3-bucket](https://github.com/infra-ops/aws-tr-repo/blob/master/terragrunt/s3/terragrunt.hcl)

```
cat /terragrunt/s3/terragrunt.hcl

terraform {
  source = "../../tg-modules/s3-bucket"
}


inputs = {
  bucket_name = "my-terragrunt-s3-bucket"
  tags = {
    Environment = "Dev"
    ManagedBy   = "Terragrunt"
  }


```



Use cases:
------------

| **#** | **Practice**                                   | **Description**                                                                                   |
|-------|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| **1** | **Keep Terraform code DRY**                   | Avoid repetition in Terraform configurations by using modules, variables, and locals to keep your code reusable and maintainable. |
| **2** | **Keep remote state configuration DRY**       | Centralize and manage remote state configuration in a separate Terraform configuration file to prevent duplication and ensure consistency across environments. |
| **3** | **Keep CLI flags DRY**                        | Use environment variables, `.tfvars` files, or wrapper scripts to minimize redundant use of CLI flags and standardize their usage across multiple Terraform commands. |
| **4** | **Execute Terraform commands on multiple modules at once** | Utilize `-target` or use a workspace management strategy to apply changes to multiple modules simultaneously, allowing for efficient management of your infrastructure. |
| **5** | **Work with multiple AWS accounts**           | Use different provider configurations for each AWS account, possibly through multiple provider blocks or by using `alias` to manage resources across different AWS environments. |





```

# Step 6: Create EC2 Instances
resource "aws_instance" "web" {
  count         = 2  # Create 2 EC2 instances
  ami           = "ami-0c55b159cbfafe1f0"  # Replace with a valid AMI ID for your region
  instance_type = "t2.micro"  # Choose the instance type

  subnet_id              = element(data.aws_subnets.public_subnets.ids, count.index)  # Place instances in public subnets
  security_groups        = [aws_security_group.alb_sg.name]  # Attach the security group created above
  associate_public_ip_address = true  # Assign a public IP address

  tags = {
    Name = "WebInstance${count.index + 1}"  # Tag instances uniquely
  }
}

# Step 7: Attach EC2 Instances to the Target Group using for_each
resource "aws_lb_target_group_attachment" "web" {
  for_each          = toset(aws_instance.web[*].id)  # Iterate over all EC2 instance IDs
  target_group_arn  = aws_lb_target_group.app_tg.arn
  target_id         = each.value
  port              = 80
}


# Attach the Load Balancer to the Auto Scaling Group
resource "aws_autoscaling_attachment" "example" {
  autoscaling_group_name = aws_autoscaling_group.example.name
  lb_target_group_arn   = aws_lb_target_group.example.arn
}

 ```

```

module "vpc" {
  source  = "./modules/vpc"
  
  vpc_cidr_block         = var.vpc_cidr_block
  public_subnet_cidr     = var.public_subnet_cidr
  private_subnet_cidr    = var.private_subnet_cidr
}

module "ec2_instances" {
  source = "./modules/ec2_instance"
  subnet_ids = module.vpc.private_subnet_ids
  ami            = var.ami
  security_group = ["sg-12345678"]
}

```
```

## Write terraform code to deploy t2.micro instance when environment
is sit and t2.small when environment is uat

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

```

```
## Create a terraform module that dynamically creates aws ec2 instances based on a 
variable input list that contains the instance type and number of instances of each type.


variable "instance_types" {
  description = "A map of instance types and their counts"
  type        = map(number)
  default     = {
    "t2.micro" = 1
    "t2.small" = 1
  }
}

resource "aws_instance" "example" {
  for_each = var.instance_types

  ami           = "ami-12345678"  # Replace with your AMI ID
  instance_type = each.key
  count         = each.value
}

output "instance_ids" {
  description = "The IDs of the created EC2 instances"
  value       = aws_instance.example[*].id
}

module "ec2_instances" {
  source = "./my_module"

  instance_types = {
    "t2.micro" = 2
    "t3.micro" = 3
    # Add more instance types as needed
  }
}

```

S3 Creation
-----------------------------
- [s3](https://github.com/infra-ops/aws-tr-repo/blob/master/aws-generic/as/s3-bucket.tf)
  
````
vim s3.tf

resource "aws_s3_bucket" "tf_course" {
   bucket = "hella-buckets"
   acl = "private"
}

````

## Setting up S3 Backend
-----------------------

cat backend.tf

```tf

terraform {
 backend "s3" {
   encrypt = true    bucket = "hella-buckets"
   dynamodb_table = "terraform-state-lock-dynamo"
   key    = "terraform.tfstate"
   region = "us-east-1"
 }
}
```


## DynamoDB Table
----------------------------
```tf
resource "aws_dynamodb_table" "dynamodb-terraform-state-lock" {
 name = "terraform-state-lock-dynamo"
 hash_key = "LockID"
 read_capacity = 20
 write_capacity = 20

 attribute {
   name = "LockID"
   type = "S"
 }
}

```

```
Dynamic Block
------------------
## Local Variable Example

locals {
    inbound_ports = [80, 443]
    outbound_ports = [443, 1433]
}

# Security Groups
resource "aws_security_group" "sg-webserver" {
    vpc_id              = aws_vpc.vpc.id
    name                = "webserver"
    description         = "Security Group for Web Servers"

    dynamic "ingress" {
        for_each = local.inbound_ports
        content {
            from_port   = ingress.value
            to_port     = ingress.value
            protocol    = "tcp"
            cidr_blocks = [ "0.0.0.0/0" ]
        }
    }

    dynamic "egress" {
        for_each = local.outbound_ports
        content {
            from_port   = egress.value
            to_port     = egress.value
            protocol    = "tcp"
            cidr_blocks = [ var.vpc-cidr ]
        }
    }
}




```
```


```

```
## Create three subnets if vpc is vpc_a , Create two subnets if vpc is vpc_b


# Data blocks to reference existing VPCs
data "aws_vpc" "vpc_a" {
  filter {
    name   = "cidr"
    values = ["10.0.1.0/16"]
  }
}

data "aws_vpc" "vpc_b" {
  filter {
    name   = "cidr"
    values = ["10.0.2.0/16"]
  }
}

# Define private subnets for each VPC
variable "vpc_a_private_subnets" {
  type    = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "vpc_b_private_subnets" {
  type    = list(string)
  default = ["10.0.4.0/24", "10.0.5.0/24"]
}

# Availability Zones
variable "azs" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

# Select VPC Type
variable "vpc_type" {
  type    = string
  default = "vpc_a"
}

# Conditional selection of private subnets based on VPC type
locals {
  selected_vpc_subnets = var.vpc_type == "vpc_a" ? var.vpc_a_private_subnets : var.vpc_b_private_subnets
  selected_vpc_id      = var.vpc_type == "vpc_a" ? data.aws_vpc.vpc_a.id : data.aws_vpc.vpc_b.id
}

# Create AWS Subnets based on the selected VPC type
resource "aws_subnet" "private_subnets" {
  count             = length(local.selected_vpc_subnets)
  vpc_id            = local.selected_vpc_id
  cidr_block        = local.selected_vpc_subnets[count.index]
  availability_zone = var.azs[count.index % length(var.azs)]
}

#terraform apply -var="vpc_type=vpc_a" -auto-approve "devtfplan"
#terraform plan -var-file="dev.tfvars" -out="devtfplan"

```


## Creating 10 EC2 instances with incremental values. Terminating 9 EC2 instances while keeping one running.
--------------------------------------------------------------------------------------------------------------



```tf
resource "aws_instance" "example" {
  for_each      = toset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  ami           = "ami-0c55b159cbfafe1f0"  # Replace with your AMI ID
  instance_type = "t2.micro"
  tags = {
    Name = "Instance-${each.key}"
  }
}



resource "aws_instance" "example" {
  for_each      = toset([1, 2, 3, 4, 5, 6, 7, 8, 10])  # Excludes 9
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = {
    Name = "Instance-${each.key}"
  }
}


terraform state rm aws_instance.example[8]
```


Give a configuration of for creating a single E2C instance in Amazon Web Services ( AWS ).
-----------------------------------------------------------------------------------------------

```
provider “aws”  { 
region = “ap-south-1” 
} 

resource “aws_instance” “example”  { 
ami = “ami-4fc58420” 
instance_type = “t2.micro” 
tags { 
     Name = “terraform-example” 
     
     } }
```

Terraform code to attach the new worker node to k8s cluster
------------------------------------------------------------

```
# Add Worker Nodes to EKS Cluster
resource "aws_eks_node_group" "worker_nodes" {
  cluster_name    = data.aws_eks_cluster.cluster.name
  node_group_name = "worker-node-group"
  node_role_arn   = aws_iam_role.worker_node_role.arn
  subnet_ids      = ["subnet-1", "subnet-2"] # Replace with your subnets

  scaling_config {
    desired_size = 2
    max_size     = 5
    min_size     = 1
  }
}



```


What happens if console resource values are changed and Terraform apply is executed?
----------------------------------------------------------------------------------------
# Impact of Changing Console Resource Values and Running `terraform apply`

| **Scenario**                                | **Description**                                                                                                     |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Manual Change in Console**                | If resource values are changed manually in the console (e.g., AWS Console), Terraform will not be aware of these changes unless the state is refreshed or imported.|
| **`terraform apply` after Console Changes**  | Running `terraform apply` will cause Terraform to compare the current state (which doesn't reflect the manual changes) with the configuration. It will attempt to revert or adjust the resources to match the configuration in the `.tf` files. |
| **Resource Drift Detection**                | Terraform detects drift (differences between actual infrastructure and the state file). If manual changes exist, Terraform may modify the resources to match the configuration defined in the code. |
| **Potential Impact**                        | Manual changes may be overwritten by Terraform, leading to potential loss of configurations not tracked in the `.tf` files, such as changes made directly in the console. |
| **Best Practice**                           | Always use Terraform to manage resources instead of making changes directly in the console to avoid discrepancies and resource drift. |





How do you handle an error stating that the resource already exists when creating resources with Terraform?
------------------------------------------------------------------------------------------------------------

# Handling "Resource Already Exists" Error in Terraform

| **Approach**                          | **Description**                                                                                                                                                    |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Check Resource State**              | Verify if the resource already exists outside of Terraform’s management. This can be done by inspecting the state with `terraform state list` or checking manually. |
| **Use `terraform import`**            | If the resource exists but isn't managed by Terraform, use `terraform import` to bring the resource into the Terraform state.                                       |
| **Delete or Recreate Resource**       | If the resource was created previously but is causing conflicts, you can delete it manually and re-run `terraform apply` or use `terraform taint` to force recreation. |
| **Check for Duplicate Resource Names** | Ensure that there are no duplicate resource definitions in your configuration that may conflict. Check for multiple modules or configurations attempting to create the same resource. |
| **Resource Lifecycle Management**     | In some cases, setting a `create_before_destroy` lifecycle rule can resolve conflicts if Terraform tries to create a new resource before destroying an existing one.    |




## If you delete the local Terraform state file and it’s not stored in S3 or DynamoDB, how can you recover it
-----------------------------------------------------------------------------------------------------------------


# Recovering Terraform State if Local File is Deleted

| **Scenario**                                  | **Description**                                                                                               |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Local State File Deleted**                  | If the local state file is deleted and it's not stored in a remote backend like S3 or DynamoDB, Terraform cannot directly access the previous state.|
| **Potential Recovery Methods**                | - **Recreate Resources**: If the resources are still present, you can manually import them into the state using `terraform import`. |
|                                               | - **Re-run `terraform plan` and `apply`**: Terraform will treat the infrastructure as unmanaged and recreate it according to the configuration, leading to resource destruction and recreation.|
| **Preventative Measures**                     | Always use a remote backend (e.g., S3, DynamoDB) to store the state file, preventing loss of state in case of local file deletion. |
| **Use `terraform import`**                    | Import existing resources back into the Terraform state to avoid recreating them. |




What is a private module registry in Terraform
------------------------------------------------

# Private Module Registry in Terraform

| **Concept**                            | **Description**                                                                                                               |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Private Module Registry**            | A private module registry in Terraform allows you to create, store, and manage Terraform modules within your organization, providing centralized access and control over reusable configurations. |
| **Usage**                              | It helps in maintaining security, versioning, and compliance by restricting module access to authorized users only. |
| **Example**                            | Suppose your organization has a custom VPC module that you want to reuse across multiple projects. You can upload this module to a private registry, and other teams can access and use it securely. |
| **Creating a Private Registry**        | You can host a private module registry using a solution like HashiCorp’s Terraform Cloud, or your own internal registry server. |
| **Accessing Modules**                  | Example of using a private module registry in a Terraform configuration file:                                               |
|                                        | ```                                                                                                                           |
|                                        | module "vpc" {                                                                                                               |
|                                        |   source  = "app.terraform.io/your-org/vpc/aws"                                                                                 |
|                                        |   version = "1.0.0"                                                                                                          |
|                                        | }                                                                                                                             |
|                                        | ```                                                                                                                           |
| **Benefits**                           | - Reusability of modules within the organization. <br> - Control over who can access and modify modules. <br> - Secure storage of sensitive modules. |



# How Terraform Refresh Works
---------------------------------

| **Concept**                    | **Description**                                                                                              |
|---------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Purpose of Terraform Refresh**| The `terraform refresh` command is used to update the state file with the most current information about the resources managed by Terraform. |
| **Action Taken**                | It retrieves the current state of resources from the infrastructure provider (e.g., AWS, Azure) and updates the state file accordingly, without making any changes to the infrastructure itself. |
| **When to Use**                 | It’s typically used when you suspect that the state file is out of sync with the actual infrastructure. It can also be useful after manual changes have been made outside of Terraform. |
| **Effect on Infrastructure**   | No actual changes are made to the infrastructure. The command only updates the state file to reflect the latest resource configurations. |
| **How It Works**                | Terraform communicates with the provider's API to fetch the latest status of resources and updates the local state file with any changes. |
| **Example**                     | Run `terraform refresh` to refresh the state file:                                                           |
|                                 | ```                                                                                                          |
|                                 | terraform refresh                                                                                             |
|                                 | ```                                                                                                          |
| **Best Practice**               | Use it to keep the state file synchronized when changes outside of Terraform are made to resources.           |



# How would you upgrade Terraform plugins?
----------------------------------------------


# Upgrading Terraform Plugins

| **Step**                         | **Description**                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Step 1: Check for Available Updates** | Run `terraform init -upgrade` to check for available updates for your provider plugins and modules.           |
| **Step 2: Run Terraform Init**   | Running `terraform init` without the `-upgrade` flag will initialize or reinitialize the working directory, but it may not upgrade plugins. Use the `-upgrade` flag to ensure plugins are upgraded to the latest compatible version. |
| **Step 3: Specify Plugin Version** | If you want to upgrade to a specific version, update the `version` attribute in the provider block of your Terraform configuration file. |
| **Step 4: Validate Configuration** | After upgrading plugins, run `terraform validate` to ensure that the configuration is valid and works with the updated provider. |
| **Step 5: Apply Changes**        | Once the plugins are upgraded and validated, you can run `terraform apply` to apply the changes and ensure everything is working as expected. |
| **Example Command**              | To upgrade all plugins to the latest compatible versions:                                                   |
|                                  | ```                                                                                                         |
|                                  | terraform init -upgrade                                                                                        |
|                                  | ```                                                                                                         |
| **Best Practice**                | Always test your configurations after upgrading plugins to avoid compatibility issues.                     |




The root module in Terraform is the top-level module that aggregates 
resources and other modules to define the infrastructure configuration.






## Reference Links
-----------------

- [UseCases](https://www.terraform.io/intro/use-cases.html)















































































