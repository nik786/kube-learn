

| **Command**               | **Description**                                                                                                                                                             | **Use Case**                                                                                                  |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Git Reset**              | Remove file from the staging area, but leave the working directory unchanged.                                                                                               | Apply changes to the current branch without affecting the working directory.                                 |
| **Git Reset --hard**       | Reset staging area and working directory to match the most recent commit, overwriting all changes in the working directory.                                                  | Use to discard all uncommitted changes and reset the working directory and staging area to the last commit.  |
| **Git Reset commitId**     | Move the current branch tip backward to a specific commit, reset the staging area to match, but leave the working directory alone.                                          | Use to undo commits, but leave changes in the working directory without modifying them.                       |
| **Git Revert**             | Create a new commit that undoes all of the changes made in a specific commit and applies it to the current branch.                                                           | Use when you need to undo a commit but retain the history.                                                   |
| **Git Clean**              | Shows which files would be removed from the working directory.                                                                                                              | Use to check which untracked files will be removed.                                                         |
| **Git Checkout**           | Creates a new branch or checks out an existing branch.                                                                                                                        | Use to switch branches or create a new one.                                                                  |
| **Git Merge**              | Combines changes from one branch into another branch while maintaining the history of commits.                                                                               | Use when merging feature branches into the main branch.                                                      |
| **Git Rebase**             | Rewrites commits from one branch onto another branch, maintaining a linear history by rewriting commit history.                                                              | Use to maintain a linear commit history by rebasing changes onto the target branch.                          |
| **Git Fetch**              | Downloads the latest changes from the remote repository into the local repository, without changing the working directory or staging area.                                    | Use to download changes for review without affecting your working directory.                                  |
| **Git Pull**               | Downloads the latest changes and automatically merges them into the working directory.                                                                                      | Use when you want to both fetch and merge changes in one step.                                               |
| **Git Squash Merge**       | Combines multiple commits into a single commit when merging a feature branch into the main branch. Keeps the history clean by merging only one commit per feature.            | Use when you want to keep the main branch clean with a single commit representing a feature.                 |
| **Git Squash Rebase**      | Rewrites commit history interactively, combining multiple commits into one on the same branch before merging.                                                                | Use when refining the history on a feature branch before merging it into the main branch.                    |
| **Git Cherry Pick**        | Picks a particular commit from one branch and applies it to another branch.                                                                                                  | Use to apply specific commits from one branch to another, rather than merging all changes.                    |
| **Git Stash**              | Temporarily stores uncommitted changes locally in the stash area. Allows switching branches without losing work.                                                              | Use to temporarily store changes and switch branches without losing your work.                               |
| **Git Stash List**         | Lists all uncommitted changes in the stash area.                                                                                                                              | Use to view a list of stashed changes.                                                                       |
| **Git Stash Pop**          | Applies stashed changes to the working directory and removes them from the stash area.                                                                                       | Use to retrieve changes from the stash and apply them to the local repository.                               |
| **Git Stash Apply**        | Applies stashed changes to the working directory but does not remove them from the stash area.                                                                               | Use to retrieve changes from the stash without removing them.                                                 |
| **Git Reflog**             | Displays a history of changes to the tips of branches and other references (e.g., HEAD). It helps recover lost commits and track branch movements.                           | Use to view changes to `HEAD` and recover lost commits or previous states of your branches.                   |
| **Git Reset --HEAD**       | Resets the current `HEAD` to a specified commit or state. This can be used to undo commits and changes in the working directory.                                             | Use when you need to reset `HEAD` to a specific commit, without affecting the working directory.               |
| **Git Amend**              | Modifies the most recent commit. This allows changes to the commit message or the commit content itself.                                                                     | Use to fix or update the last commit without creating a new one.                                               |
| **Git Quickfix**           | A quick approach to amend the last commit with small adjustments, often used for fixing a single file or mistake.                                                             | Use to make small corrections to the last commit, such as fixing a typo or adding forgotten files.            |
| **Git Fix**                | A shorthand for making a small fix to the last commit, combining multiple minor fixes or adjustments in one commit.                                                           | Use to bundle fixes into a single commit, like fixing small issues across different files in one go.          |
| **Git Diff HEAD**          | Shows the difference between the working directory and the last commit.                                                                                                      | Use to view changes in the working directory compared to the last commit.                                    |
| **Git Diff --cached**      | Shows the difference between the staged changes and the last commit.                                                                                                         | Use to see the differences between the staged changes and the last commit.                                    |

### Git Workflow
- **Working Directory** → **Staging Area** → **Stash Area** → **Local Repository**



| **Term**      | **Definition**                                                                                     |
|---------------|---------------------------------------------------------------------------------------------------|
| **Submodule** | A Git repository embedded inside another repository, enabling version tracking of external projects. |


| **Branch**   | **Description**                                                                                   |
|--------------|---------------------------------------------------------------------------------------------------|
| **main**     | The default branch name for new repositories since October 2020, introduced to replace `master`.   |
| **master**   | The traditional default branch name in Git repositories, widely used before `main` became standard.|


| **Step**                              | **Command**/Description                                                                                   | **Example**                                                                                      |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **1. Add a Submodule**                | Add a submodule to your repository.                                                                       | `git submodule add https://github.com/example/lib-example.git libs/lib-example`                 |
| **2. Initialize and Update Submodule**| Initialize and update submodules after cloning a repository containing them.                              | `git submodule init` <br> `git submodule update` <br> Or use: `git clone --recurse-submodules <repository-url>` |
| **3. Update Submodule to Latest Commit** | Pull the latest changes from the submodule's remote repository.                                           | `cd libs/lib-example` <br> `git pull origin main`                                               |
| **4. Commit Changes to Submodule**    | Make changes in the submodule and commit them. Push changes to the submodule repository.                  | `git add <files>` <br> `git commit -m "Updated submodule"` <br> `git push origin main`          |
| **5. Update Submodule Reference in Parent Repository** | Stage and commit submodule updates in the parent repository.                                              | `cd <parent-repo>` <br> `git add libs/lib-example` <br> `git commit -m "Updated submodule reference"` <br> `git push origin main` |
| **6. Remove a Submodule**             | Remove a submodule from the parent repository.                                                            | 1. Remove entry from `.gitmodules`: `git rm --cached <submodule-path>` <br> 2. Remove files: `rm -rf <submodule-path>` <br> 3. Remove `.git/modules` entry: `rm -rf .git/modules/<submodule-path>` <br> 4. Commit: `git commit -m "Removed submodule"` |


| **Benefit**                         | **Description**                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| **Code Reusability**                | Allows sharing and reusing code across multiple projects by linking a shared repository as a submodule. |
| **Independent Version Control**     | Submodules maintain their own commit history, enabling independent versioning and updates.        |
| **Modular Development**             | Facilitates modular project design by managing separate repositories for different components or libraries. |
| **Consistent Dependency Management**| Ensures a consistent version of the submodule is used across team members and CI/CD pipelines.    |
| **Separation of Concerns**          | Keeps the main project repository clean and focused by isolating third-party libraries or tools.  |
| **Fine-Grained Updates**            | You can control and test updates to submodules without affecting the main repository immediately. |
| **Collaboration**                   | Teams can work independently on the submodule repository, fostering better collaboration.         |



What is a branch in Git, and why is it important?

A branch in Git is a lightweight pointer to a specific commit. Branching allows
developers to work on features or bug fixes independently without affecting the
main codebase.


What are the different types of Git merges?
1. Fast-Forward Merge: Occurs when there’s no divergence in the branches.
2. Three-Way Merge: Happens when there’s divergence, and Git creates a new merge
commit


How do you resolve merge conflicts?

Example Scenario: Two developers modify the same line in a file. Steps:


1. Identify conflicting files:
git status
2. Open the file, and locate conflict markers:
<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> branch-name
3. Edit the file to keep the desired changes.
4. Mark the conflict as resolved:
git add conflicted-file
5. Commit the merge:
git commit


What is Git Rebase, and how does it differ from Git Merge?
o Git Rebase: Reapplies commits from one branch onto another. It results in a linear
history.
o Git Merge: Combines branches and retains the commit history.

When should you use rebase instead of merge?
o Use rebase for maintaining a clean, linear commit history in private branches.
o Avoid rebasing shared branches to prevent rewriting history.




What is the Gitflow Workflow?
o Gitflow is a branching model that uses feature, release, hotfix, and develop
branches.
o Commands:
1. Start a feature:
git checkout -b feature/my-feature develop
2. Merge the feature:
git checkout develop

git merge feature/my-feature

Describe a scenario where you would use git cherry-pick.
o
Scenario: A bug fix commit needs to be applied to multiple branches.
git cherry-pick <commit-hash>




What if you commit sensitive data accidentally?
o
Steps to remove sensitive data:
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch <file-path>' \
--prune-empty --tag-name-filter cat -- --all
git push origin --force --all



You accidentally deleted a branch. How do you recover it?
o
If the branch was merged:
git checkout -b branch-name <commit-hash>



How do you handle detached HEAD?
o
Commands:
git checkout -b new-branch


Scenario: How do you recover a deleted file in Git?
•
If the file was deleted in the working directory but exists in a previous commit:
git checkout HEAD -- <file-path>
•
If it was deleted and committed:
1. Find the commit:
git log -- <file-path>
2. Restore the file:
git checkout <commit-hash> -- <file-path>


How do you revert a commit that was already pushed to the remote?
o
Use git revert to create a new commit that undoes the changes:
git revert <commit-hash>

git push origin <branch-name>



What is the purpose of the .gitignore file?
o .gitignore specifies intentionally untracked files that Git should ignore.
o Example .gitignore file:
# Ignore all .log files
*.log
# Ignore node_modules directory
node_modules


| **Feature**               | **GitHub**                                                                 | **GitLab**                                                                 |
|---------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **CI/CD Integration**     | Requires third-party tools like GitHub Actions for CI/CD pipelines.        | Built-in CI/CD integration with extensive pipeline configuration options.  |
| **Project Management**    | Basic project management tools with issues, milestones, and project boards.| Advanced project management features, including epics and burndown charts. |
| **Self-Hosting**          | Self-hosting available through GitHub Enterprise Server.                   | Free self-hosting available with GitLab CE, along with a paid EE version.  |
| **Permissions Model**     | Granular permissions at the repository level.                              | More flexible permissions with group-level and project-level granularity.  |
| **Pricing**               | Free plan with limited features; advanced features in paid plans.          | More features in the free plan; competitive pricing for premium features.  |




How do you delete a branch locally and remotely?
o
Locally:
git branch -d branch-name
o
Remotely:
git push origin --delete branch-name


Scenario: You need to rename a branch. How do you do it?
o
On local:
git branch -m old-branch-name new-branch-name
o
On remote:
1. Delete the old branch:
git push origin --delete old-branch-name
2. Push the new branch:
git push origin new-branch-name


How do you avoid automatic merges for specific files?

Use .gitattributes to enforce merge strategies:
*.config merge=ours
Configure:
bash
Copy code
git config --global merge.ours.driver true



How do you abort a merge in progress?

Run:
git merge --abort


What happens if a rebase fails?
Resolve conflicts as prompted.

Continue the rebase:
git rebase --continue

Abort if necessary:
git rebase --abort


What is a detached HEAD in Git, and how do you fix it?
o A detached HEAD occurs when you checkout a commit directly instead of a branch.
o Fix by creating a new branch:

git checkout -b new-branch-name



How do you tag a commit and push the tag to a remote?

git tag -a v1.0 -m "Version 1.0"

git push origin v1.0

How do you handle a hotfix in production using Gitflow?

1. Create a hotfix branch:
git checkout -b hotfix/fix-bug master
2. Apply and commit changes.
3. Merge back to master and develop:
git checkout master
git merge hotfix/fix-bug
git checkout develop
git merge hotfix/fix-bug


How do you review and test a PR locally?
o
Fetch the PR:
git fetch origin pull/<PR-number>/head:<local-branch-name>
o
Check out the branch:
git checkout <local-branch-name>



Scenario: How do you globally ignore files in Git?
o
Add patterns to a global ignore file:
git config --global core.excludesfile ~/.gitignore_global
o
Example ~/.gitignore_global:
.DS_Store



How do you enable colorized output in Git?
o
Command:
git config --global color.ui auto


What if you accidentally dropped a stash?
o
Recover using the reflog:
git reflog
git stash apply stash@{<index>}


How do you configure Git hooks?

Create a hook script in .git/hooks/. Example for pre-commit:
#!/bin/sh
echo "Running pre-commit hook"


What if you accidentally committed to the wrong branch?

Steps to move the commit to the correct branch:
1. Create a new branch:
git checkout -b correct-branch
2. Cherry-pick the commit:
hgit cherry-pick <commit-hash>
3. Remove the commit from the wrong branch:
git checkout wrong-branch
git reset --hard HEAD~1

How do you identify the author of a specific line in a file?
o
Use git blame:
git blame <file-path>


What is the difference between git clone and git fork?
o git clone: Creates a local copy of a remote repository.
o git fork: Duplicates a repository on platforms like GitHub, creating a separate copy
under your account.



What are the different states in Git?
o Untracked: Files not tracked by Git.
o Staged: Files added to the staging area.
o Committed: Changes saved to the repository


How do you undo the last commit?
o
Without removing changes:
git reset --soft HEAD~1
o
With removing changes:
git reset --hard HEAD~1


What is the difference between git branch and git checkout?
o git branch: Creates, lists, or deletes branches.
o git checkout: Switches branches or checks out files.



What is the difference between merge conflict markers and resolved files?
o
Merge conflict markers:
<<<<<<< HEAD
Code from current branch
=======
Code from other branch
>>>>>>> branch-name
o Resolved files: After editing the conflict markers and staging the file, it is considered
resolved.



How do you ensure a branch is up to date before merging?

Steps:
1. Fetch latest changes:
git fetch origin
2. Rebase onto the target branch:
git rebase origin/branch-name



What is an "interactive rebase," and why is it useful?
 Interactive rebase allows you to edit, reorder, or squash commits before applying
them.
 Command:
git rebase -i HEAD~n

Use cases:
▪ Cleaning up commit history before pushing.
▪ Merging related commits into one


Scenario: How do you handle rebase conflicts?
o
Steps:
1. Resolve the conflict in the affected files.
2. Stage the resolved files:
git add <file>
3.
Continue the rebase:
git rebase –continue


Scenario: How do you switch branches and keep your current work?
o
Use git stash to save changes:
git stash
git checkout new-branch
git stash apply



What are Git hooks, and how are they used in workflows?
o Git hooks are scripts that execute at specific events like commits or merges.
o Example: Pre-commit hook:
▪
Create .git/hooks/pre-commit and add:
#!/bin/sh
echo "Checking code quality..."


How do you pull changes from a specific branch of a remote repository?
o
Command:
git pull origin branch-name
58. How do you set up a remote repository?
o
Add a remote:
git remote add origin <repository-url>
o
Push the repository:
git push -u origin main



What is a Git upstream branch?
o
An upstream branch is the branch your local branch tracks.
Example:
git branch --set-upstream-to=origin/main main



How do you configure aliases in Git?
o
Example:
git config --global alias.co checkout
git config --global alias.br branch

git co <branch-name>
git br



How do you list all stashes?
o
Command:
git stash list


How do you drop a specific stash?
o
Command:
git stash drop stash@{index}






