

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















