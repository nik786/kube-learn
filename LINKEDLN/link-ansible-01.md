

You need to configure a server differently based on its data center location. How would you dynamically apply different configurations using Ansible?

2. You are tasked with patching 500 servers, but you need to ensure high availability. How do you apply updates in a rolling fashion using Ansible?

3. You want to deploy an application only if the checksum of the deployment package has changed. How would you implement this in Ansible?

4. How would you use Ansible to validate that a web application is accessible after deployment, and roll back automatically if it’s not?

5. You need to run a command on 100 servers, but not all of them have Python installed (so Ansible can’t connect). How would you handle this?

6. You are provisioning new servers and need to apply different roles depending on their hostnames or tags. How would you dynamically assign roles?

7. How would you secure sensitive variables like AWS access keys and reuse them across multiple playbooks?

8. You have multiple teams working with Ansible. How would you structure your playbooks, roles, and inventories to manage RBAC and minimize conflicts?

9. You need to write a playbook that can configure both Windows and Linux hosts. How would you handle cross-platform tasks in Ansible?

10. You want to store Ansible inventory in a CMDB or database instead of static files. How do you implement this using dynamic inventory plugins?

11. You need to run a playbook as a different user on some servers (not the default SSH user). How would you implement this in Ansible?

12. A task must only run if a specific port is open on a remote host. How can this condition be enforced using Ansible modules?

13. You need to execute a shell command but only if a specific process is not running. How would you use Ansible to do this check and act accordingly?

14. You want to ensure idempotency when copying a configuration file generated from a Jinja2 template. How would you implement change detection and handlers?

15. Your deployment is failing randomly on certain hosts due to transient issues. How can you add retry logic in Ansible for such tasks?

16. You need to deploy a multi-tier application (DB > App > Web). How can you orchestrate dependencies and sequencing between the roles?

17. You want to enforce security baselines on servers like SSH settings, file permissions, and package restrictions. How would you manage this with Ansible?

18. Some servers have different package managers (e.g., yum, dnf, apt). How do you write a common playbook that handles all OS types?

19. You need to collect custom performance metrics like CPU or memory usage across all servers and store them in a centralized location. How would you do this with Ansible?

20. How would you use Ansible to create users with different SSH keys based on the environment (dev, staging, prod)?
