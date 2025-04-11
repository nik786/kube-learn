


# Terraform `required_version` Explanation

| Aspect | Description |
|--------|-------------|
| **Syntax** | `required_version = "~> 1.3.0"` |
| **Purpose** | Ensures that the Terraform CLI used is **compatible with version 1.3.x**, i.e., any version `>= 1.3.0 and < 1.4.0`. |
| **Version Constraint** | `~>` is a version constraint operator that allows updates that **do not change the leftmost non-zero digit**. So, `~> 1.3.0` allows versions like `1.3.1`, `1.3.5`, but **not** `1.4.0`. |
| **Does it download Terraform CLI?** | ❌ No, it does **not download the Terraform CLI itself**. You must install a compatible version manually or with tools like `tfenv`. |
| **Does it download providers, libraries, plugins?** | ✅ Yes, **once the correct Terraform CLI version is installed**, `terraform init` will download compatible provider plugins (e.g., AWS, Helm) based on `required_providers` block. |
| **Library/Provider Compatibility** | ✅ Ensures that the Terraform CLI version is compatible with the configuration code, but **each provider (e.g., AWS)** defines its own compatible Terraform versions via its internal metadata. |
| **How AWS provider determines compatibility?** | The AWS provider specifies its compatible Terraform versions using a `required_terraform_version` constraint in its provider manifest. Terraform checks this during `terraform init`. |
| **Error if mismatch?** | ❌ Yes, if the running Terraform CLI version does not satisfy the `required_version`, Terraform will **fail immediately** with an error: _"This configuration does not support Terraform version X..."_ |
| **Where is it used?** | Inside the root `terraform` block in `main.tf` or `versions.tf`: <br><br> ```hcl<br> terraform {<br>   required_version = "~> 1.3.0"<br>   required_providers {<br>     aws = {<br>       source  = "hashicorp/aws"<br>       version = ">= 4.0"<br>     }<br>   }<br> }<br> ``` |

