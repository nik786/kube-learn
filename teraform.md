What are the use cases of Terraform?

1. Multi-Tier Applications
2. Self-Service Cluster
3. Disposable Environment
4. Software Defined Networking
5. Resource Schedulers
6. Multi-Cloud Deployment


https://www.terraform.io/intro/use-cases.html


You have different environments and you want to deploy your infrastructure in 
all the environments such as dev, test, prod, etc. How do you achieve it?

Every Application goes through different environments before it is deployed into production. It’s always best practice to have similar environments for consistency purposes. It’s so easy to replicate the bugs and fix them easily. It’s not easy to replicate the same set of infrastructure in each environment if we do that manually. Terraform makes it easy to create infrastructure in a multi-cloud environment.
Please go through the below article for detailed explanation
Terraform — 5 Ways To Create Infrastructure in Multiple Environments
1) Using Folders — Method 1
2) Using Folders — Method 2
3) Workspaces
4) Modules
5) Terragrunt


What is the Terraform State and what is its purpose?

It is a file which keeps track of the current state of infrastructure managed by Terraform. 
The state file is a JSON-formatted file that records information about the resources created and managed by Terraform, their attributes, dependencies, and other metadata.


Resource Tracking:
The state file maintains a record of all resources created and managed by Terraform, along with their current configurations and state

Dependency Management:
Terraform uses the state file to understand the relationships and dependencies between different resources. This information is crucial for ensuring the correct order of resource creation, modification, and deletion.

Preventing Resource Drift:
The state file helps Terraform detect and prevent resource drift. Drift occurs when the actual state of resources in the cloud deviates from the expected state defined in your Terraform configuration. Terraform uses the state file to compare the desired state with the actual state and determine if any changes are necessary.

Concurrency Control:
The state file provides a mechanism for Terraform to manage concurrency and coordinate operations when multiple users or automation processes are making changes to the infrastructure

How do you constrain the provider version?

To constrain the provider version as suggested, add a required_providers block inside a terraform block:

terraform {
  required_providers {
    aws = "~> 1.0"
  }
}


How do you configure Multiple Provider Instances?
alias



Why do we need Multiple Provider instances?

Some of the example scenarios:a. multiple regions for a cloud platform
targeting multiple Docker hosts
 multiple Consul hosts, etc.



 How do you configure Multiple Provider Instances?

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



How do you configure Multiple Provider Instances?

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


How do you configure Multiple Provider Instances?

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




How do you configure Multiple Provider Instances?

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



How do you configure Multiple Provider Instances?

resource "aws_instance" "web_instance_1" {
  provider = aws.aws1
  # other resource configurations
}

resource "aws_instance" "web_instance_2" {
  provider = aws.aws2
  # other resource configurations
}



How do you configure Multiple versions?

Use Terraform Version Constraints:
In your Terraform configurations, you can specify a required Terraform version using the required_version block.

terraform {
  required_version = ">= 0.14, < 0.15"
}


# Install tfenv
git clone https://github.com/tfutils/tfenv.git ~/.tfenv
echo 'export PATH="$HOME/.tfenv/bin:$PATH"' >> ~/.bashrc

# Install a specific version
tfenv install 0.14.7

# Use a specific version in your project directory
tfenv use 0.14.7




What is Provider Plugin Cache?
The Provider Plugin Cache in Terraform is a mechanism that allows Terraform to cache and reuse provider plugins, which are 
executable binaries responsible for interfacing with a specific infrastructure platform or service. Provider plugins are essential 
components in Terraform that enable it to communicate with various cloud providers, on-premises infrastructure, or other external systems

The Provider Plugin Cache is beneficial for efficiency, especially in environments where multiple Terraform users or CI/CD pipelines 
might be working with the same providers. It reduces the need to repeatedly download provider plugins, improving the overall Terraform experience by minimizing network requests and speeding up the initialization process.



Define Terraform init?

Terraform initializes the code using the command terraform init. This command is used to initialize the working directory containing Terraform configuration files. It is safe to run this command multiple times.

You can use the init command for:

Plugin Installation
Child Module Installation
Backend Initialization


Define Terraform provider?

Terraform is used to manage and inform infrastructure resources such as bodily machines, VMs, network switches, containers, and more. A provider is 
accountable for thoughtful API interactions and revealing resources. Terraform supports a large number of cloud providers.


terraform init: Prepare your working directory for other commands
terraform validate: Check whether the configuration is valid
terraform plan: Show changes required by the current configuration
terraform apply: Create or update infrastructure
terraform destroy: Destroy previously-created infrastructure


How does Terraform help in discovering plugins?

The authority “Terraform init” helps Terraform interpret configuration files in the operational directory. Then, Terraform finds out the essential plugins and searches for installed plugins in 
diverse locations. In addition, Terraform also downloads extra plugins at times. Then, it decides the plugin versions to use and writes a security device file for ensuring that Terraform will employ the identical plugin versions


Define Modules in Terraform?

A module in Terraform is collection of multiple resources that are used jointly. The root module is required for every Terraform that includes resources mentioned in the .tf files.


What are the ways to lock Terraform module versions?

We can use the terraform module registry as a source and provide the attribute as ‘version’ in the module in a terraform configuration file. If you are using the GitHub repository as a source, then you need to specify the branch, 
version and query string with ‘? ref’.

What do you mean by Terragrunt, list some of its use cases?

Terragrunt is a thin wrapper that provides extra tools for keeping configurations DRY, working with multiple Terraform modules, and managing remote state.

Use cases:

Keep Terraform code DRY
Keep remote state configuration DRY
Keep CLI flags DRY
Execute Terraform commands on multiple modules at once
Work with multiple AWS accounts


What is State File Locking?

State file locking is a mechanism in terraform where operation on a specific state file is blocked to avoid conflicts between multiple users performing the same operation. 
Once the lock from one user is released, then only any other user can operate on that state file after taking a lock on it. This helps in preventing any corruption of the state file. 
It is a backend operation, so the acquiring of lock on a state file in backend. If it takes more time than expected to acquire a lock on the state file, you will get a status message as an output.


What is a Tainted Resource?

Tainted resources are those resources that are forced to be destroyed and recreated on the next apply command. When you mark a resource as tainted, 
nothing changes on infrastructure but the state file is updated with this information(destroy and create). After marking a resource as tainted, terraform plan out will 
show that the resource will get destroyed and recreated, and when the next apply happens the changes will get implemented.

What does the following command do?

Terraform -version – to check the installed version of terraform
Terraform destroys – to destroy the managed infrastructure of terraform.
Terraform fmt– it is used to rewrite configuration files in a canonical styles and format
Terraform providers – it gives information of providers working in the current configuration.

What is the use of fmt command in Terraform?

fmt tool will take care of formatting. TO validate our configuration formatting and make them neat by running


Apply: builds or changes infrastructure.
Console: Interactive console for Terraform interpolations.
destroy: Destroy Terraform-managed infrastructure.
env: Workspace management
fmt: Rewrites config files to canonical format
get: Download and install modules for the configuration
graph: Build a visible graph of Terraform resources Import: existing infrastructure into Terraform
Init: Initialize a Terraform working directory
output: Read output from a state file plan: Generate and show an execution plan validate: Validates the Terraform files
version: Prints the Terraform version
Workspace: Workspace management

Give a configuration of for creating a single E2C instance in Amazon Web Services ( AWS ).

provider “aws” { region = “ap-south-1” } 
resource “aws_instance” “example” 
{ ami = “ami-4fc58420” instance_type = “t2.micro” tags { Name = “terraform-example” } }


Graphing - Its features of graphing that are built-in are helpful in visualizing the infrastructure.
Custom Syntax - It's custom syntax is very friendly which aids in enhancing efficiency.
Resource Relationships - A very beneficial feature of terraforming is that it is able to understand resource relationships.
Updates - The updates and features are added by the Open Source Project. It does so with a group of lots of contributors.
Improved Maintenance - It is capable of breaking down the configuration into small parts or chunks for improving the organization and the maintenance.























































































