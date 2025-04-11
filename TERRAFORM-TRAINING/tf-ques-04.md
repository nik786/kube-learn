


# Terraform `required_version` Explanation

| Aspect | Description |
|--------|-------------|
| **Syntax** | `required_version = "~> 1.3.0"` |
| **Purpose** | Ensures that Terraform CLI used is **compatible with version 1.3.x**, i.e., any version `>= 1.3.0 and < 1.4.0`. |
| **Does it download Terraform?** | ❌ No, it does **not download** Terraform itself. You must install a compatible version manually or using a version manager like `tfenv`. |
| **Library/Provider Compatibility** | ✅ Ensures that Terraform CLI version is **compatible with the code**, but providers (like AWS) must specify their **own compatible Terraform versions**. |
| **How AWS provider determines compatibility?** | The AWS provider’s `required_terraform_version` in its own configuration (defined by the provider’s authors) specifies which Terraform versions it supports. Terraform will check this during `init`. |
| **Error if mismatch?** | If your installed Terraform version doesn't meet the required version, Terraform will **fail early** with an error like: _"This configuration does not support Terraform version..."_ |
| **Where is it used?** | Inside the `terraform` block in your root `main.tf` or equivalent module: <br> ```hcl<br> terraform {<br>   required_version = "~> 1.3.0"<br> }<br> ``` |

