

State Management & Collaboration:

1. How do you manage Terraform state across environments? 
2. How do you handle remote state locking in team setups? 
3. What’s your strategy to recover from a corrupted state file? 
4. How do you inspect/modify state without affecting infra?


Modules & Reusability:

5. How do you build reusable Terraform modules across teams? 
6. How do you manage shared module versioning? 
7. How do you deal with module dependencies and nesting?


Advanced Logic & Operations:

8. Difference between `count`, `for_each`, and `dynamic`. 
9. When would you use `create_before_destroy` lifecycle rules? 
10. Explain `terraform import` which you have used in any project . 
11. Monorepo vs Polyrepo Terraform strategy – pros & cons.


Security & Secrets Management:

12. How do you secure secrets in Terraform without exposing them? 
13. How do you integrate Azure Key Vault/Vault with Terraform? 
14. How do you enforce RBAC for Terraform in CI/CD? 
15. Tools you use to ensure Terraform security compliance?


CI/CD & Automation: 
 
16. How do you implement Terraform with GitOps? 
17. How do you handle `terraform plan`/`apply` in pipelines? 
18. What’s your approach to approval gates in prod applies?


Debugging & Failures:

19. How do you troubleshoot apply failures across modules? 
20. How do you detect and resolve infra drift in Terraform? 
21. What’s your rollback strategy if an apply breaks midway?


Azure-Specific Scenarios: 

22. How do you manage Terraform across multiple Azure subscriptions? 
23. How do you create and secure AKS clusters with Terraform? 
24. How do you handle tagging, policies, and cost control via code? 
25. How do you use Service Principals vs Managed Identity with Terraform?



1. What is Terraform, and what is its primary purpose?
2.  How does Terraform differ from other IaC tools like CloudFormation or Ansible?
3.  What are the key Terraform commands, and what do they do?
4. What is a Terraform state file?
5. What are Terraform providers, and why are they important?
6. What are Terraform modules?
7. How does Terraform manage remote state?
8. What are Terraform workspaces, and when should you use them?
9. How does Terraform handle importing existing infrastructure, and what are the limitations?

10. What are Terraform provisioners, and when should you use them?
11. What is drift detection in Terraform, and how can it be addressed?
12. How would you implement a rolling update using Terraform for an application deployed in multiple instances?

13. How do you handle resource dependencies in Terraform, and what is the role of implicit and explicit dependencies?


| Concept | Explanation |
|---------|-------------|
| **Implicit Resource Dependencies** | Terraform automatically infers resource relationships when one resource uses attributes of another (e.g., referencing `aws_vpc.main.id` inside a subnet resource). No manual intervention needed. |
| **Explicit Resource Dependencies** | When Terraform cannot detect a relationship automatically, `depends_on` is used to manually define a dependency between resources to control their creation/destruction order. |
| **Version Constraint Operators** | In `required_providers` or `required_version` blocks, version constraint operators like `=`, `>=`, `<=`, `~>`, etc., are used to manage provider and Terraform versions (e.g., `>= 1.3.0, < 2.0.0`). |
| **terraform init** | `terraform init` installs the providers, modules, and sets up the backend. It ensures the correct versions are downloaded as per constraints. |
| **terraform.lock.hcl** | This file locks the exact versions of providers that were installed during `terraform init`. It ensures consistent builds across different environments and users. |
| **required_providers** | Defined inside the `terraform` block, it specifies the providers Terraform should use, along with version constraints, ensuring compatibility and stability. |
| **Module Dependencies** | Modules can depend on outputs of other modules. Terraform manages these using implicit references, but explicit `depends_on` can also be used between modules. |
| **Provider Dependencies** | Terraform tracks which resources depend on which providers. Changes in provider settings (like credentials, regions) can cause resource recreation if needed. |
| **Order of Operations** | Terraform's internal graph builds a dependency tree and automatically calculates the correct order to create, update, or destroy resources. |






14.  How do you manage complex multi-cloud deployments with Terraform?
15.  What are the taint and untaint commands in Terraform? How would you use them in a real-world scenario?

16. What are zero-downtime deployments, and how can Terraform achieve them?
17. How do you handle secrets management in Terraform, and what are the best practices?

18. Explain the concept of remote state locking in Terraform and its importance in team collaboration.


