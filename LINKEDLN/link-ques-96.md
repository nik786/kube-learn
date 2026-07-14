
5. Jenkins Master-Slave Architecture  
   Your team is using Jenkins for continuous integration and continuous deployment (CI/CD). Describe the master-slave architecture of Jenkins and how it enables distributed builds and deployments.

6. Implementing a CI/CD Pipeline  
   You are tasked with implementing a CI/CD pipeline from scratch for a web application. Describe the steps you would take to implement the pipeline, including how you would ensure zero downtime deployments and implement rollbacks.

7. Shift-Left in DevOps  
   Explain the concept of shift-left in DevOps and how it enables teams to detect and fix issues earlier in the development cycle.

8. ADD vs COPY in a Dockerfile  
   What is the difference between the ADD and COPY instructions in a Dockerfile?

9. Removing Sensitive Information from Git  
   You accidentally committed sensitive information to a Git repository. Describe the steps you would take to remove the sensitive information from the repository's history.
   ## Removing Sensitive Information from Git History

| Step | What to Do | Example Command |
|------|------------|-----------------|
| **1. Remove the sensitive file** | Delete the file or remove the secret from the code. | `git rm secrets.txt` |
| **2. Rewrite Git history** | Remove the file from all commits. | `git filter-repo --path secrets.txt --invert-paths` |
| **3. Force push the changes** | Update the remote repository with the cleaned history. | `git push --force origin main` |
| **4. Change the exposed secret** | Generate a new password, token, or API key immediately. | *(Rotate the secret in AWS, GitHub, etc.)* |
| **5. Ask team members to re-clone** | Tell everyone to clone the repository again to avoid using old history. | `git clone <repository-url>` |

### Easy to Remember

```text
Remove File
      ↓
Rewrite History
      ↓
Force Push
      ↓
Change Secret
      ↓
Re-clone Repository
```

Interview One-Line Answer:
"Remove the secret, rewrite the Git history, force push the cleaned repository, rotate the exposed secret, and ask the team to re-clone the repository."



11. Recovering a Deleted Git Branch  
    One of your team members accidentally deleted a critical branch in a Git repository. Describe the steps you would take to recover the deleted branch.

    ## Recovering a Deleted Git Branch

| Step | What to Do | Example Command |
|------|------------|-----------------|
| **1. Find the deleted branch commit** | Check the Git history to find the last commit of the deleted branch. | `git reflog` |
| **2. Copy the commit ID** | Note the commit hash (SHA) of the deleted branch. | `abc1234` |
| **3. Recreate the branch** | Create a new branch from the commit ID. | `git checkout -b feature-branch abc1234` |
| **4. Push the recovered branch** | Upload the restored branch to the remote repository. | `git push origin feature-branch` |
| **5. Verify the branch** | Check that the branch is available locally and remotely. | `git branch -a` |

### Easy to Remember

```text
Find Commit
      ↓
Copy Commit ID
      ↓
Recreate Branch
      ↓
Push Branch
      ↓
Verify
```

Find the deleted branch's commit using git reflog, recreate the branch from that commit, push it to the remote repository, and verify that it has been restored


