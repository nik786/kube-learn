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


Resource Tracking:
--------------------
The state file maintains a record of all resources created and managed by Terraform, along with their current configurations and state

Dependency Management:
-------------------------
Terraform uses the state file to understand the relationships and dependencies between different resources. <br><br>
This information is crucial for ensuring the correct order of resource creation, modification, and deletion.

Preventing Resource Drift:
----------------------------
The state file helps Terraform detect and prevent resource drift. <br><br>
Drift occurs when the actual state of resources in the cloud deviates from the expected state defined in your Terraform configuration. <br><br>
Terraform uses the state file to compare the desired state with the actual state and determine if any changes are necessary.<br><br>

Concurrency Control:
--------------------------

The state file provides a mechanism for Terraform to manage concurrency and coordinate operations when multiple users or automation processes are making changes to the infrastructure

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

How do you configure Multiple Provider Instances?
--------------------------------------------------

```

provider "aws" {
  region = "us-east-1"
  access_key = "your-aws-access-key"
  secret_key = "your-aws-secret-key"
}

provider "azurerm" {
  features = {}
}

provider "google" {
  credentials = file("path/to/google/credentials.json")
  project     = "your-google-project-id"
}

```

How do you configure Multiple Provider Instances?
---------------------------------------------------

```
# AWS resources
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}

# Azure resources
resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

```


How do you configure Multiple Provider Instances?
---------------------------------------------------

```
# Google Cloud resources
resource "google_compute_instance" "example" {
  name         = "example-instance"
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"
  }
}

```

How do you configure Multiple Provider Instances?
---------------------------------------------------

```
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
The Provider Plugin Cache in Terraform is a mechanism that allows Terraform to cache and reuse provider plugins, which are 
executable binaries responsible for interfacing with a specific infrastructure platform or service. Provider plugins are essential 
components in Terraform that enable it to communicate with various cloud providers, on-premises infrastructure, or other external systems

The Provider Plugin Cache is beneficial for efficiency, especially in environments where multiple Terraform users or CI/CD pipelines 
might be working with the same providers. It reduces the need to repeatedly download provider plugins, improving the overall Terraform experience by minimizing network requests and speeding up the initialization process.



Define Terraform init?
------------------------
Terraform initializes the code using the command terraform init. 
This command is used to initialize the working directory containing Terraform configuration files. It is safe to run this command multiple times.

You can use the init command for:

Plugin Installation
Child Module Installation
Backend Initialization


Define Terraform provider?
---------------------------

Terraform is used to manage and inform infrastructure resources such as bodily machines, VMs, network switches, containers, and more. A provider is 
accountable for thoughtful API interactions and revealing resources. Terraform supports a large number of cloud providers.





How does Terraform help in discovering plugins?
-------------------------------------------------

The authority “Terraform init” helps Terraform interpret configuration files in the operational directory. Then, Terraform finds out the essential plugins and searches for installed plugins in 
diverse locations. In addition, Terraform also downloads extra plugins at times. Then, it decides the plugin versions to use and writes a security device file for ensuring that Terraform will employ the identical plugin versions


Define Modules in Terraform?
------------------------------

A module in Terraform is collection of multiple resources that are used jointly. The root module is required for every Terraform that includes resources mentioned in the .tf files.


What are the ways to lock Terraform module versions?
-----------------------------------------------------

We can use the terraform module registry as a source and provide the attribute as ‘version’ in the module in a terraform configuration file. If you are using the GitHub repository as a source, then you need to specify the branch, 
version and query string with ‘? ref’.

What do you mean by Terragrunt, list some of its use cases?

Terragrunt 
-----------
It is a thin wrapper that provides extra tools for keeping configurations DRY, working with multiple Terraform modules, and managing remote state.

Use cases:
------------

1. **Keep Terraform code DRY**  
   - Avoid repetition in Terraform configurations by using modules, variables, and locals to keep your code reusable and maintainable.

2. **Keep remote state configuration DRY**  
   - Centralize and manage remote state configuration in a separate Terraform configuration file to prevent duplication and ensure consistency across environments.

3. **Keep CLI flags DRY**  
   - Use environment variables, `.tfvars` files, or wrapper scripts to minimize redundant use of CLI flags and standardize their usage across multiple Terraform commands.

4. **Execute Terraform commands on multiple modules at once**  
   - Utilize `-target` or use a workspace management strategy to apply changes to multiple modules simultaneously, allowing for efficient management of your infrastructure.

5. **Work with multiple AWS accounts**  
   - Use different provider configurations for each AWS account, possibly through multiple provider blocks or by using `alias` to manage resources across different AWS environments.



What is State File Locking?
---------------------------

State file locking is a mechanism in terraform where operation on a specific state file is blocked to avoid conflicts between multiple users performing the same operation. 
Once the lock from one user is released, then only any other user can operate on that state file after taking a lock on it. This helps in preventing any corruption of the state file. 
It is a backend operation, so the acquiring of lock on a state file in backend. If it takes more time than expected to acquire a lock on the state file, you will get a status message as an output.


What is a Tainted Resource?
---------------------------

Tainted resources are those resources that are forced to be destroyed and recreated on the next apply command. When you mark a resource as tainted, 
nothing changes on infrastructure but the state file is updated with this information(destroy and create). After marking a resource as tainted, terraform plan out will 
show that the resource will get destroyed and recreated, and when the next apply happens the changes will get implemented.


Terraform refresh
--------------------

The terraform refresh command is used to update the state file with the most current information about the resources managed by Terraform. It does not make any changes to the actual infrastructure or resources; instead, it retrieves the current state of those resources and updates the state file to reflect their current state.

The terraform refresh command is typically used in scenarios where you suspect that the state file has become out of sync with the actual infrastructure. It can help you bring the state file up to date without making any changes to the infrastructure itself.


Terraform Provider
-----------------------
In Terraform, a "provider" is a configuration block that defines and configures a specific cloud or service provider. Providers are essential components of Terraform configurations because they establish the connection to the target infrastructure or service where your resources will be created and managed.

Terraform Drift
--------------------
Terraform drift refers to the changes made to infrastructure resources outside of Terraform's management, causing a mismatch between the actual infrastructure state and the state tracked by Terraform.




## Null Resource
--------------
The null_resource is essentially a no-op or "null" resource, meaning that it doesn't directly create or manage any infrastructure, but it can be used for various purposes within the Terraform configuration.<br><br>
 The null_resource can be used to run local provisioners, which are scripts or commands executed on the machine where Terraform is running, rather than on a remote resource.



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

Graphing - Its features of graphing that are built-in are helpful in visualizing the infrastructure.<br><br>
Custom Syntax - It's custom syntax is very friendly which aids in enhancing efficiency.<br><br>
Resource Relationships - A very beneficial feature of terraforming is that it is able to understand resource relationships.<br><br>
Updates - The updates and features are added by the Open Source Project. It does so with a group of lots of contributors.<br><br>
Improved Maintenance - It is capable of breaking down the configuration into small parts or chunks for improving the organization and the maintenance.<br><br>



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

DynamicBlock
----------------

A dynamic block is used inside resource or module blocks to dynamically construct nested configuration blocks. 

https://github.com/infra-ops/aws-tr-repo/blob/master/aws-generic/as/dynamic-block.tf


vault
------

https://github.com/infra-ops/aws-tr-repo/blob/master/aws-generic/as/vault.tf

Local
------

Local variables in Terraform allows to simplify expressions and calculations within a module by defining intermediate values. 
They help avoid redundant code, keep complex expressions clear, and improve code readability.


https://github.com/infra-ops/aws-tr-repo/blob/master/aws-generic/as/vault.tf


With remote state, Terraform writes the state data to a remote data store, which can then be shared between all members of a team.

mkdir lockdown

Creating our S3 in Terraform
-----------------------------

````
vim s3.tf

provider "aws" {
 shared_credentials_file = "~/.aws/credentials"
 region     = "us-east-1"
}

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


## Creating our DynamoDB Table
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

| 01. Requirement                                | Solution                                                                                                                       |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| 01. Deploy same infrastructure across regions  | Use **Terraform Providers** with the `alias` argument to define multiple AWS regions in the configuration.                    |
| 02. Create regional resources                  | Use `provider "aws"` blocks with different `region` values for each region where resources need to be deployed.                |
| 03. Use modules for reusable infrastructure   | Encapsulate infrastructure components (like VPC, EC2, etc.) into **modules**, then call them for each region.                 |
| 04. Define region-specific variables           | Create region-specific variables (e.g., `vpc_name`, `instance_type`) and pass them to modules for dynamic infrastructure configuration. |
| 05. Use `terraform plan` and `apply` separately| Execute `terraform plan` and `apply` per region to ensure the correct resources are deployed to the right regions.            |
| 06. Example setup                             | ```hcl                                                                                                                        |
|                                                 | provider "aws" {                                                                                                              |
|                                                 |   region = "us-east-1"                                                                                                        |
|                                                 |   alias  = "us_east_1"                                                                                                        |
|                                                 | }                                                                                                                            |
|                                                 | provider "aws" {                                                                                                              |
|                                                 |   region = "us-west-2"                                                                                                        |
|                                                 |   alias  = "us_west_2"                                                                                                        |
|                                                 | }                                                                                                                            |
|                                                 | module "vpc_us_east" {                                                                                                        |
|                                                 |   source = "./vpc"                                                                                                            |
|                                                 |   providers = { aws = aws.us_east_1 }                                                                                         |
|                                                 | }                                                                                                                            |
|                                                 | module "vpc_us_west" {                                                                                                        |
|                                                 |   source = "./vpc"                                                                                                            |
|                                                 |   providers = { aws = aws.us_west_2 }                                                                                         |
|                                                 | }                                                                                                                            |
|                                                 | ```                                                                                                                           |






 




## Reference Links
-----------------

https://www.terraform.io/intro/use-cases.html















































































