

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



| **Question**                                   | **Answer**                                                                                                                                                                                   |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What is Git Rebase, and how does it differ from Git Merge?** | **Git Rebase**: Reapplies commits from one branch onto another, resulting in a linear history. <br> **Git Merge**: Combines branches and retains the commit history.                          |
| **When should you use rebase instead of merge?** | Use rebase for maintaining a clean, linear commit history in private branches. <br> Avoid rebasing shared branches to prevent rewriting history.                                              |
| **What is the Gitflow Workflow?**              | Gitflow is a branching model using feature, release, hotfix, and develop branches. <br> **Commands**: <br> Start a feature: `git checkout -b feature/my-feature develop` <br> Merge the feature: `git checkout develop && git merge feature/my-feature` |
| **Describe a scenario where you would use git cherry-pick.** | **Scenario**: A bug fix commit needs to be applied to multiple branches. <br> **Command**: `git cherry-pick <commit-hash>`                                                                    |
| **What if you commit sensitive data accidentally?** | **Steps to remove sensitive data**: <br> `git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch <file-path>' --prune-empty --tag-name-filter cat -- --all` <br> `git push origin --force --all` |
| **You accidentally deleted a branch. How do you recover it?** | If the branch was merged: <br> `git checkout -b branch-name <commit-hash>`                                                                                                                    |
| **How do you handle detached HEAD?**           | **Command**: `git checkout -b new-branch`                                                                                                                                                    |
| **Scenario: How do you recover a deleted file in Git?** | If the file was deleted in the working directory but exists in a previous commit: <br> `git checkout HEAD -- <file-path>` <br> If deleted and committed: <br> 1. Find the commit: `git log -- <file-path>` <br> 2. Restore the file: `git checkout <commit-hash> -- <file-path>` |
| **How do you revert a commit that was already pushed to the remote?** | Use `git revert` to create a new commit that undoes the changes: <br> `git revert <commit-hash>` <br> `git push origin <branch-name>`                                                          |
| **What is the purpose of the .gitignore file?** | **Purpose**: Specifies intentionally untracked files that Git should ignore. <br> **Example .gitignore**: <br> `# Ignore all .log files` <br> `*.log` <br> `# Ignore node_modules directory` <br> `node_modules` |






| **Feature**               | **GitHub**                                                                 | **GitLab**                                                                 |
|---------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **CI/CD Integration**     | Requires third-party tools like GitHub Actions for CI/CD pipelines.        | Built-in CI/CD integration with extensive pipeline configuration options.  |
| **Project Management**    | Basic project management tools with issues, milestones, and project boards.| Advanced project management features, including epics and burndown charts. |
| **Self-Hosting**          | Self-hosting available through GitHub Enterprise Server.                   | Free self-hosting available with GitLab CE, along with a paid EE version.  |
| **Permissions Model**     | Granular permissions at the repository level.                              | More flexible permissions with group-level and project-level granularity.  |
| **Pricing**               | Free plan with limited features; advanced features in paid plans.          | More features in the free plan; competitive pricing for premium features.  |



| **Question**                                  | **Answer**                                                                                                                                           |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **How do you delete a branch locally and remotely?** | **Locally**: `git branch -d branch-name` <br> **Remotely**: `git push origin --delete branch-name`                                                     |
| **Scenario: You need to rename a branch. How do you do it?** | **On local**: `git branch -m old-branch-name new-branch-name` <br> **On remote**: <br> 1. Delete the old branch: `git push origin --delete old-branch-name` <br> 2. Push the new branch: `git push origin new-branch-name` |
| **How do you avoid automatic merges for specific files?** | Use `.gitattributes` to enforce merge strategies: <br> `*.config merge=ours` <br> **Configure**: <br> `git config --global merge.ours.driver true`     |
| **How do you abort a merge in progress?**     | Run: `git merge --abort`                                                                                                                             |
| **What happens if a rebase fails?**           | Resolve conflicts as prompted. <br> Continue the rebase: `git rebase --continue` <br> Abort if necessary: `git rebase --abort`                        |
| **What is a detached HEAD in Git, and how do you fix it?** | A detached HEAD occurs when you checkout a commit directly instead of a branch. <br> **Fix**: `git checkout -b new-branch-name`                       |
| **How do you tag a commit and push the tag to a remote?** | **Commands**: <br> `git tag -a v1.0 -m "Version 1.0"` <br> `git push origin v1.0`                                                                      |
| **How do you handle a hotfix in production using Gitflow?** | 1. Create a hotfix branch: `git checkout -b hotfix/fix-bug master` <br> 2. Apply and commit changes. <br> 3. Merge back to master and develop: <br> `git checkout master && git merge hotfix/fix-bug` <br> `git checkout develop && git merge hotfix/fix-bug` |
| **How do you review and test a PR locally?**  | Fetch the PR: `git fetch origin pull/<PR-number>/head:<local-branch-name>` <br> Check out the branch: `git checkout <local-branch-name>`               |
| **Scenario: How do you globally ignore files in Git?** | Add patterns to a global ignore file: <br> `git config --global core.excludesfile ~/.gitignore_global` <br> **Example `.gitignore_global`**: <br> `.DS_Store` |
| **How do you enable colorized output in Git?** | **Command**: `git config --global color.ui auto`                                                                                                      |
| **What if you accidentally dropped a stash?** | Recover using the reflog: <br> `git reflog` <br> `git stash apply stash@{<index>}`                                                                     |


| **Question**                                  | **Answer**                                                                                                                                           |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **How do you configure Git hooks?**          | Create a hook script in `.git/hooks/`. Example for pre-commit: <br> ```#!/bin/sh``` <br> ```echo "Running pre-commit hook"```                         |
| **What if you accidentally committed to the wrong branch?** | **Steps**: <br> 1. Create a new branch: `git checkout -b correct-branch` <br> 2. Cherry-pick the commit: `git cherry-pick <commit-hash>` <br> 3. Remove the commit from the wrong branch: <br> `git checkout wrong-branch` <br> `git reset --hard HEAD~1` |
| **How do you identify the author of a specific line in a file?** | Use `git blame`: <br> `git blame <file-path>`                                                                                                         |
| **What is the difference between git clone and git fork?** | **git clone**: Creates a local copy of a remote repository. <br> **git fork**: Duplicates a repository on platforms like GitHub, creating a separate copy under your account. |
| **What are the different states in Git?**    | **Untracked**: Files not tracked by Git. <br> **Staged**: Files added to the staging area. <br> **Committed**: Changes saved to the repository.       |
| **How do you undo the last commit?**         | **Without removing changes**: `git reset --soft HEAD~1` <br> **With removing changes**: `git reset --hard HEAD~1`                                     |
| **What is the difference between git branch and git checkout?** | **git branch**: Creates, lists, or deletes branches. <br> **git checkout**: Switches branches or checks out files.                                    |
| **What is the difference between merge conflict markers and resolved files?** | **Merge conflict markers**: <br> ```<<<<<<< HEAD``` <br> Code from current branch <br> ```=======``` <br> Code from other branch <br> ```>>>>>>> branch-name``` <br> **Resolved files**: After editing the conflict markers and staging the file, it is considered resolved. |
| **How do you ensure a branch is up to date before merging?** | **Steps**: <br> 1. Fetch latest changes: `git fetch origin` <br> 2. Rebase onto the target branch: `git rebase origin/branch-name`                     |
| **What is an "interactive rebase," and why is it useful?** | Interactive rebase allows you to edit, reorder, or squash commits before applying them. <br> **Command**: `git rebase -i HEAD~n` <br> **Use cases**: <br> ▪ Cleaning up commit history before pushing. <br> ▪ Merging related commits into one. |
| **Scenario: How do you handle rebase conflicts?** | **Steps**: <br> 1. Resolve the conflict in the affected files. <br> 2. Stage the resolved files: `git add <file>` <br> 3. Continue the rebase: `git rebase --continue` |
| **Scenario: How do you switch branches and keep your current work?** | Use `git stash` to save changes: <br> `git stash` <br> `git checkout new-branch` <br> `git stash apply`                                               |
| **What are Git hooks, and how are they used in workflows?** | Git hooks are scripts that execute at specific events like commits or merges. <br> **Example: Pre-commit hook**: <br> Create `.git/hooks/pre-commit` and add: <br> ```#!/bin/sh``` <br> ```echo "Checking code quality..."``` |
| **How do you pull changes from a specific branch of a remote repository?** | **Command**: `git pull origin branch-name`                                                                                                            |
| **How do you set up a remote repository?**   | Add a remote: `git remote add origin <repository-url>` <br> Push the repository: `git push -u origin main`                                            |
| **What is a Git upstream branch?**           | An upstream branch is the branch your local branch tracks. <br> **Example**: `git branch --set-upstream-to=origin/main main`                          |
| **How do you configure aliases in Git?**     | **Example**: <br> `git config --global alias.co checkout` <br> `git config --global alias.br branch` <br> Use: `git co <branch-name>` or `git br`     |
| **How do you list all stashes?**             | **Command**: `git stash list`                                                                                                                         |
| **How do you drop a specific stash?**        | **Command**: `git stash drop stash@{index}`                                                                                                           |
| **How do you perform a shallow clone?**      | **Command**: `git clone --depth 1 <repository-url>`                                                                                                   |

| **Question**                                           | **Answer**                                                                                             |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **What is Git bisect, and how is it used?**            | Git bisect helps find the commit that introduced a bug.<br>**Steps:**<br>1. Start bisect:<br>`git bisect start`<br>`git bisect bad`<br>`git bisect good <commit-hash>`<br>2. Test commits and mark them:<br>`git bisect good/bad`<br>3. End bisect:<br>`git bisect reset` |
| **How do you view the contents of a previous commit?** | Command:<br>`git show <commit-hash>`                                                                  |
| **What do you do if a git push fails because of a non-fast-forward update?** | This happens when the remote has commits that your local branch does not.<br>**Steps:**<br>1. Pull changes:<br>`git pull origin branch-name`<br>2. Resolve conflicts if any.<br>3. Push again:<br>`git push origin branch-name` |
| **How do you recover from an accidental `git reset --hard`?** | Use the reflog to find the lost commits:<br>`git reflog`<br>Checkout the commit:<br>`git checkout <commit-hash>` |
| **What is the difference between `git log` and `git reflog`?** | `git log`: Shows the commit history of a branch.<br>`git reflog`: Shows a history of all actions performed in the repository (including resets, checkouts). |
| **How do you create a branch from a specific commit?** | Command:<br>`git checkout -b new-branch-name <commit-hash>`                                            |
| **What is the difference between `git branch -d` and `git branch -D`?** | `git branch -d`: Deletes the branch only if it has been merged.<br>`git branch -D`: Force deletes the branch even if it has not been merged. |
| **How do you prevent Git from creating a merge commit during `git pull`?** | Use the `--rebase` flag:<br>`git pull --rebase`                                                       |
| **What are merge strategies in Git?**                 | **Recursive**: Default strategy for merging two branches.<br>**Ours**: Keeps changes from the current branch.<br>**Octopus**: Used for merging more than two branches. |
| **How do you edit a commit message after rebasing?**  | Use interactive rebase:<br>`git rebase -i HEAD~n`<br>Replace `pick` with `reword` for the desired commit. |
| **How do you abandon a rebase in progress?**          | Command:<br>`git rebase --abort`                                                                      |
| **How do you integrate a feature branch into the main branch?** | **Steps:**<br>1. Switch to the main branch:<br>`git checkout main`<br>2. Merge the feature branch:<br>`git merge feature-branch` |
| **What if you want to merge only specific commits from another branch?** | Use `git cherry-pick`:<br>`git cherry-pick <commit-hash>`                                             |
| **What is the purpose of the `git reset` command?**   | **Soft Reset**: Moves the HEAD pointer but keeps changes staged.<br>**Mixed Reset (default)**: Moves the HEAD pointer and unstages changes.<br>**Hard Reset**: Moves the HEAD pointer and deletes changes in the working directory. |
| **How do you check the differences between your branch and a remote branch?** | Command:<br>`git diff branch-name origin/branch-name`                                                 |
| **How do you apply a stash and drop it in one command?** | Command:<br>`git stash pop`                                                                           |
| **How do you create and track a Git submodule?**      | **Steps:**<br>1. Add the submodule:<br>`git submodule add <repository-url> <path>`<br>2. Initialize the submodule:<br>`git submodule init`<br>3. Update the submodule:<br>`git submodule update` |
| **What is Git sparse checkout?**                      | Sparse checkout allows you to check out only specific files or directories from a repository.<br>**Steps:**<br>`git sparse-checkout init`<br>`git sparse-checkout set <directory>` |
| **How do you resolve conflicts in binary files?**     | Use an external merge tool configured with Git:<br>`git mergetool`                                    |
| **How do you handle a history rewrite on a shared branch?** | Communicate with the team and force-push:<br>`git push --force`                                       |




| **Question**                                                             | **Answer**                                                                                                                                                                         |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **How do you fix a detached HEAD state?**                                | Create a new branch from the current state:<br>`git checkout -b new-branch`                                                                                                       |
| **How do you undo a pushed commit without removing it from history?**    | 1. Use `git revert` to create a new commit that undoes the changes:<br>`git revert <commit-hash>`<br>2. Push the revert commit:<br>`git push origin branch-name`                   |
| **What if your git pull results in many unnecessary merge commits?**     | Use `git pull` with the `--rebase` flag to maintain a linear history:<br>`git pull --rebase`                                                                                      |
| **How do you troubleshoot when your changes are not visible after pushing?** | 1. Possible cause: Pushed to the wrong branch:<br>`git branch`<br>`git push origin correct-branch`<br>2. Remote tracking branch not updated:<br>`git fetch origin`                |
| **How do you resolve "detected a conflict during cherry-pick"?**         | 1. Resolve the conflict manually in the affected files.<br>2. Stage the resolved files:<br>`git add <file>`<br>3. Continue the cherry-pick:<br>`git cherry-pick --continue`       |
| **What is the difference between HEAD and ORIG_HEAD?**                   | `HEAD`: Refers to the current commit or branch.<br>`ORIG_HEAD`: Refers to the previous state of `HEAD`, usually before a destructive action like a reset or rebase.                |
| **How do you track a remote branch locally?**                            | Command:<br>`git checkout --track origin/branch-name`                                                                                                                             |
| **What is the difference between git merge --squash and git merge --no-ff?** | `--squash`: Combines all commits into a single commit without creating a merge commit.<br>`--no-ff`: Creates a merge commit even if a fast-forward merge is possible.              |
| **How do you rebase a branch while ignoring certain commits?**           | Use an interactive rebase:<br>`git rebase -i branch-name`<br>Mark commits to be ignored as `drop`.                                                                                |
| **What if a rebase rewrites history you need to recover?**               | Use the reflog to recover the previous state:<br>`git reflog`<br>`git checkout <previous-commit-hash>`                                                                            |
| **How do you handle multiple developers working on the same file?**      | 1. Pull frequently to minimize conflicts:<br>`git pull origin branch-name`<br>2. Communicate changes to the team.<br>3. Resolve conflicts collaboratively during merge or rebase.  |
| **How do you create a temporary branch to test a specific feature?**     | Command:<br>`git checkout -b temp-branch <commit-hash>`                                                                                                                           |
| **How do you fetch and check out a pull request from GitHub?**           | Command:<br>`git fetch origin pull/<PR-number>/head:<local-branch-name>`<br>`git checkout <local-branch-name>`                                                                    |
| **What do you do if you accidentally push sensitive information to a public repository?** | 1. Remove the sensitive information:<br>`git filter-branch --force --index-filter 'git rm --cached <file>' --prune-empty -- --all`<br>2. Force-push the changes:<br>`git push origin --force --all` |
| **How do you stash changes but keep them in the working directory?**     | Use the `--keep-index` flag:<br>`git stash push --keep-index`                                                                                                                     |
| **How do you drop all stashes?**                                         | Command:<br>`git stash clear`                                                                                                                                                     |













How do you stash changes and switch branches safely?
Steps:
1. Stash the changes:
git stash
2. Switch branches:
git checkout branch-name
3. Reapply the stashed changes:
git stash pop


What is the difference between git stash apply and git stash pop?
• git stash apply: Reapplies the stash but keeps it in the stash list.
• git stash pop: Reapplies the stash and removes it from the stash list


What is Git rerere, and how is it useful?
• Git rerere (reuse recorded resolution) remembers how you resolved a conflict so it can
automatically resolve the same conflict in the future.
• Enable rerere:
git config --global rerere.enabled true


How do you view changes in a submodule?
Use:
git diff –submodule


How do you resolve the error "fatal: refusing to merge unrelated
histories"?
• This error occurs when merging two branches that do not share a common commit history.
• Solution:
1. Use the --allow-unrelated-histories flag:
git merge branch-name --allow-unrelated-histories


What do you do if Git shows the error "Your local changes would be
overwritten by merge"?
• This error happens when you have uncommitted changes that conflict with the changes
being pulled or merged.
• Solution:

Stash your changes:
git stash
2. Perform the merge or pull:
git pull origin branch-name
3. Reapply your changes:
git stash pop



How do you recover a branch that was accidentally deleted locally and
remotely?
•
Steps:
1. Check the reflog for the branch’s last commit:
git reflog
2. Create a new branch from the commit:
git checkout -b branch-name <commit-hash>
3. Push the branch back to the remote repository:
git push origin branch-name


What do you do if a git fetch or git pull is stuck?
Possible solutions:
1. Check your network connection.
2. Add the --verbose flag to debug:
git fetch --verbose
3. Use shallow fetch to minimize data transfer:
git fetch --depth=1


What is the purpose of git ls-tree?
• git ls-tree is used to view the contents of a tree object (e.g., a commit or branch). It lists files
and directories along with their types and SHA-1 hashes.
• Example:
git ls-tree HEAD


How do you compare two commits in Git?
Use the git diff command with the two commit hashes:
git diff <commit1> <commit2>


How do you find a specific file in the commit history?
Use git log with the file name

git log -- <file-path>

What is the purpose of git archive?
• git archive is used to create a tar or zip archive of a repository at a specific commit or branch.
• Example:
git archive --format=zip HEAD > archive.zip



How do you set up a branch to track a remote branch?
Use the --set-upstream-to flag:
git branch --set-upstream-to=origin/branch-name

What is the difference between a tracking branch and a local branch?
• A tracking branch is a local branch linked to a remote branch, which makes it easier to pull
and push changes.
• A local branch is any branch that exists only in your local repository


What is the difference between a fast-forward merge and a three-way merge?
• Fast-forward merge: Occurs when the branch being merged has not diverged, and Git can
simply move the HEAD pointer forward.
• Three-way merge: Used when branches have diverged, requiring Git to create a new merge
commit.

How do you perform a no-commit merge?
Use the --no-commit flag:
git merge --no-commit branch-name

What are the risks of rebasing a public branch?
Rebasing rewrites history, which can lead to conflicts and issues for collaborators who are
also working on the same branch. It should only be done on private branches



How do you edit an old commit message during a rebase?
Steps:
1. Start an interactive rebase:
git rebase -i HEAD~n
2. Replace pick with reword for the desired commit.
3. Edit the message when prompted


How do you perform a rebase and automatically resolve conflicts in favor of one
branch?
•
Use the --strategy-option=theirs flag:
git rebase -s recursive -X theirs branch-name


How do you revert changes in a specific commit while keeping later
changes intact?
•
Use git revert:
git revert <commit-hash>

How do you handle a force-push on a shared branch?


Fetch the latest changes:
git fetch origin
2. Reset your local branch:

git reset --hard origin/branch-name


How do you fetch changes for a single file from a remote branch?
Use git checkout with the branch and file path:
git checkout origin/branch-name -- <file-path>


How do you create multiple stashes with custom messages?
Use the git stash save command with a message:
git stash save "Stash message 1"
git stash save "Stash message 2"


How do you apply a stash without removing it from the stash list?
•
Use:
git stash apply stash@{n}


How do you split a repository into two smaller repositories?
Use git filter-repo:
1. Install the tool:
pip install git-filter-repo
2. Split the repository:
git filter-repo --path subfolder-name --force


What is the purpose of the git worktree command?
• The git worktree command allows you to work on multiple branches in the same repository
without switching branches.
• Example:
git worktree add ../new-worktree branch-name



Scenario: How do you fix "fatal: Authentication failed" when using HTTPS?
• This error often occurs due to incorrect credentials or token expiration.
• Solutions:
1. Update your credentials:
git credential-cache exit
Then re-enter your credentials on the next pull or push.
2. Use a personal access token (PAT) instead of a password if the service requires it:
164.
▪ Generate a PAT from your Git hosting platform (e.g., GitHub, GitLab).
▪ Use the PAT as the password when prompted.



How do you fix "index.lock" errors when performing Git operations?

This error occurs if a Git process was interrupted, leaving a lock file behind.
• Solution:
1. Verify no Git processes are running:
ps aux | grep git
2. Remove the lock file:
rm -f .git/index.lock


What do you do if a commit has the wrong author information?
Use git commit --amend to correct the author for the last commit:
git commit --amend --author="Name <email@example.com>"
•
For multiple commits, use:
git rebase -i HEAD~n
Then edit each commit’s author.


How do you troubleshoot "detected inconsistent line endings in file"?
Configure Git to handle line endings:
1. Set core.autocrlf for your platform:
▪
On Windows:
git config --global core.autocrlf true
▪
On Linux/macOS:
git config --global core.autocrlf input
2. Normalize the file’s line endings:
git add --renormalize .
git commit -m "Normalize line endings


What does git reflog do, and how can it help recover lost commits?
• git reflog tracks changes to HEAD, allowing you to recover commits that are no longer
reachable via branches.
• Example:
1. List the reflog:
git reflog
2. Recover a lost commit:
git checkout <commit-hash>



What is the purpose of git cherry-pick?

git cherry-pick applies a specific commit from one branch to another without merging the
entire branch.
• Example:
git cherry-pick <commit-hash>

How do you view all files in a specific commit?
Use:
git show --name-only <commit-hash>


What is the difference between git log and git show?
• git log: Shows a history of commits.
• git show: Displays detailed information about a specific commit, including changes made.

How do you merge changes from a specific branch into your branch
without a full merge?
•
Use git cherry-pick to apply specific commits:
git cherry-pick <commit-hash>


What is the difference between git branch and git rev-parse?
• git branch: Lists, creates, or deletes branches.
• git rev-parse: Converts branch names or references into their SHA-1 hashes


How do you avoid creating a merge commit for trivial changes?
Use a fast-forward merge by ensuring the branch has no divergent changes:
git merge --ff-only branch-name

How do you force a merge commit even when a fast-forward merge is
possible?
•
Use the --no-ff flag:
git merge --no-ff branch-name


How do you merge only specific files from another branch?

git checkout branch-name -- file-path
2. Stage and commit the changes:
git add file-path
git commit -m "Merged specific file from branch-name"


How do you interactively rebase to reorder commits?
Steps:
1. Start the interactive rebase:
git rebase -i HEAD~n
2. Change the order of the commits in the editor.
3. Save and exit.

What do you do if a rebase introduces a bug?
Abort the rebase and return to the pre-rebase state:
git rebase --abort

Rebasing: Reapplies a series of commits onto a new base, modifying commit history.
• Cherry-picking: Applies specific commits to another branch without altering history.


How do you work on a hotfix in Gitflow?

Create a hotfix branch:
git checkout -b hotfix/fix-name main
2. Make changes and commit them.
3. Merge the hotfix into main and develop:
git checkout main
git merge hotfix/fix-name
git checkout develop
git merge hotfix/fix-name


What are Git tags used for in workflows?
• Tags mark specific points in history, often for releases.
• Example:
git tag -a v1.0 -m "Version 1.0"
git push origin v1.0


How do you resolve conflicts when merging a pull request?

Pull the PR locally:
git fetch origin pull/<PR-number>/head:pr-branch
2. Switch to the branch and resolve conflicts manually.
3. Push the resolved branch:
git push origin pr-branch

How do you preview what a stash contains before applying it?
Command:
git stash show stash@{n} --patch

How do you stash changes for a specific file only?
Command:
git stash push <file-path>

How do you manage submodules in a large repository?
Add a submodule:
git submodule add <repo-url> <path>
•
Update submodules:
git submodule update --init --recursive


What is the purpose of the git fsck command?
• git fsck checks the integrity of a Git repository.
• Example:
git fsck


How do you handle the "detached HEAD" state after checking out a
commit directly?
•
If you want to create a new branch from this state:
git checkout -b new-branch
•
If you want to return to an existing branch:
git checkout branch-name


What do you do if you accidentally staged changes to the wrong file?
Unstage the file:
git reset <file-path>
•
Make the necessary adjustments and restage the correct file(s):
git add correct-file-path


How do you resolve "fatal: origin does not appear to be a Git
repository"?
• This error occurs when the remote URL is missing or incorrect.
• Solution:
1. Verify the remote:
git remote -v
2. Add or correct the remote URL:
git remote add origin <repository-url>


How do you fix the "merge failed" error when rebasing?
Steps:
1. Identify conflicting files:
git status
2. Resolve conflicts manually.
3. Stage the resolved files:
git add <file>
4. Continue the rebase:
git rebase --continue



How do you count the number of commits in a branch?
Command:
git rev-list --count branch-name


What does the HEAD^ and HEAD~n syntax mean?
• HEAD^: Refers to the immediate parent of the current commit.
• HEAD~n: Refers to the nth parent commit from the current commit.

How do you display the current branch name?
git branch --show-current


How do you display detailed information about a specific commit?
Command:
git show <commit-hash>


How do you ensure no one pushes directly to main?
• Set up branch protection rules on your Git hosting platform (e.g., GitHub or GitLab).
• Alternatively, you can create a server-side pre-receive hook:
#!/bin/sh
if [ "$GIT_BRANCH" = "main" ]; then
echo "Direct pushes to main are not allowed!"
exit 1
fi


How do you identify and merge only the commits that add a specific file
or feature?
•
Use git log to identify the commits:
git log -- <file-path>
•
Cherry-pick those commits:
git cherry-pick <commit-hash>

How do you merge branches when there are too many conflicts?


1. Perform a merge:
git merge branch-name
2. Use a merge tool to simplify conflict resolution:

3. git mergetool
3. Resolve the conflicts manually if necessary and commit:
git commit

How do you track changes made to Git submodules?

Commands:
1. Update the submodule:
git submodule update --remote
2. Commit the submodule changes:
git add <submodule-path>
git commit -m "Updated submodule"




























