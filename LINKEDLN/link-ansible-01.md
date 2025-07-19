

# Ansible Interview Questions – Scenario-Based (with Answers)

| **#** | **Question** | **Answer** |
|------|--------------|------------|
| 1 | How would you configure a server differently based on its data center location? | Use group_vars or host_vars with inventory groups named after data center locations. Apply conditional logic using `when`. |
| 2 | How do you apply updates in a rolling fashion to 500 servers? | Use `serial` keyword in the playbook to update servers in batches, ensuring high availability. |
| 3 | Deploy only if checksum of deployment package changes? | Use `stat` and `checksum` to compare files and register a condition. Use `when` to control execution. |
| 4 | Validate web app post-deploy and roll back if down? | Use `uri` module to test endpoints, combine with `block/rescue` for rollback on failure. |
| 5 | Run a command on servers without Python? | Use the `raw` module, which doesn’t require Python, to bootstrap the required dependencies. |
| 6 | Assign roles based on hostname or tags? | Use `group_by` module or inventory patterns with conditions in playbooks. |
| 7 | Secure and reuse AWS keys across playbooks? | Store secrets in Ansible Vault and load via `vars_files`. Use encrypted variables in shared roles. |
| 8 | Structure for multi-team usage with RBAC? | Organize with role-based directories, separate inventories, and delegate access using Tower/AWX credentials. |
| 9 | Configure both Windows and Linux hosts? | Use `ansible_os_family` in `when` conditions. Write platform-specific tasks or use separate plays. |
| 10 | Store inventory in CMDB/database? | Use dynamic inventory plugins (e.g., script, YAML, or custom plugins for CMDB integration). |
| 11 | Run playbook as different user? | Use `ansible_user` in inventory or `--user` flag. Customize privilege escalation with `become_user`. |
| 12 | Run task only if a port is open? | Use `wait_for` module with `port` option and timeout; combine with `when` for conditional execution. |
| 13 | Execute command only if a process is not running? | Use `shell` or `ps` with `register` and conditionally run task using `when: result.stdout == ""`. |
| 14 | Ensure idempotency when copying config from Jinja2? | Use the `template` module and trigger a handler only when the file changes. |
| 15 | Add retry logic for transient task failures? | Use `retries` and `delay` with `until` loop to retry tasks until success. |
| 16 | Orchestrate multi-tier app deployment? | Use `serial`, `depends_on`, and roles in sequence; tag roles or use separate plays for each tier. |
| 17 | Enforce security baselines (SSH, perms)? | Create reusable Ansible roles for each security baseline and apply them using playbooks. |
| 18 | Handle different package managers across OS types? | Use `ansible_pkg_mgr` or `ansible_os_family` to conditionally run the appropriate package module. |
| 19 | Collect performance metrics and centralize? | Use `setup` or custom shell commands, register output, then write to a file or use centralized logging. |
| 20 | Create users with SSH keys based on environment? | Use environment-based group_vars and `with_items` to loop over users and insert corresponding keys. |
