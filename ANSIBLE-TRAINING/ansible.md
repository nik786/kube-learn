


Playbooks
-----------

- [install-packages](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/playbooks/install.yml.md)
- [role](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/roles/nik-zoo.yml)
- [helo](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/helo.yml)
- [set-fact](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/set_fact.md)
- [copy-synchronise-uri](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/copy-synchronise-uri.md)
- [docker-pull](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/docker-pull.md)
- [serial](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/serial.md)
- [cron](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/cron.md)
- [async](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/async.md)
- [block](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/block-rescue-always.md)
- [set-facts-runbook](https://techsemicolon.github.io/blog/2019/07/07/ansible-everything-you-need-to-know-about-set-facts/)
- [ec2-scale](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/ec2-scale.md)
- [adhoc-commands](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/adhoc-commands.md)
- [puppet-script](https://github.com/infra-ops/cloud-ops/blob/master/ansible-1/puppet.md)




## Autoscaling By Ansible
--------------------------

# AWS EC2 Automation Playbooks (Ansible)

## 1. Build and Launch from Latest AMI
- Find the latest AMI with name starting with `test`.
- Build the AMI.
- Wait for AMI creation to complete.
- Launch a new EC2 instance.
- Add the new instance to the host group.
- Uses **local inventory**.

🔗 [build-ami-ami.yml](https://github.com/nik786/kube-learn/blob/master/build-ami-ami.yml)

---

## 2. Deploy App on New Instance
- Application will be deployed on a newly launched EC2 instance.
- Uses **dynamic inventory** to fetch instance details.

---

## 3. Create AMI from Running Instance (Tagged `env=dev`)
- Find a running EC2 instance with tag `env=dev`.
- Create an AMI from that instance.
- Wait for AMI creation to complete.
- Launch a new EC2 instance using the created AMI.
- Add the new instance to the host group.
- Uses **local inventory**.

🔗 [build-ami-instance.yml](https://github.com/nik786/kube-learn/blob/master/build-ami-instance.yml)

---

## 4. Auto Scaling with Launch Template and Alarms
- Find the latest AMI with name starting with `test`.
- Update Launch Template with the new AMI.
- Configure the Auto Scaling Group (ASG).
- Perform a rolling deployment.
- Configure scaling policies.
- Define and configure CloudWatch metric alarms.
- Link metric alarms to the scaling policies.
- Uses **local inventory**.

🔗 [scale-lt-as-alarm.yml](https://github.com/nik786/kube-learn/blob/master/scale-lt-as-alarm.yml)









What are the features of Ansible?
-----------------------------------


| **Feature**            | **Description**                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| **Agentless**           | Unlike Puppet or Chef, Ansible does not require an agent to manage the nodes.                                   |
| **Python-Based**        | Built on Python, making it easy to learn and write scripts; Python is a robust and widely-used programming language. |
| **SSH-Based**           | Uses passwordless network authentication (SSH), ensuring secure and simple setup.                              |
| **Push Architecture**   | Pushes small configuration codes to client nodes to execute actions.                                           |
| **Easy Setup**          | Simple to set up with a low learning curve; it's open-source, allowing anyone to get hands-on experience.       |
| **Manage Inventory**    | Stores machine addresses in a simple text format and supports plugins like OpenStack and Rackspace to pull inventory. |


# Ansible Roles
------------------

Roles are a way to organize Ansible playbooks into reusable and modular
components. They separate tasks, variables, files, and templates into a standardized
directory structure, making playbooks more maintainable and scalable.


```

---
- hosts: "{{ nodes }}"
  roles:
   - nik-zookeeper-2
  remote_user: "{{ user }}" 
  become: true
  become_method: sudo

```




  

| **Concept**                        | **Description**                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Role Framework**                  | Roles provide a framework for organizing variables, tasks, files, templates, and modules into independent or interdependent collections. |
| **Primary Mechanism for Playbooks** | In Ansible, roles are the primary way to break down complex playbooks into smaller, reusable components.                  |
| **Simplification**                  | Using roles simplifies writing complex playbooks and makes them easier to maintain and reuse.                             |
| **Reusability**                     | Breaking a playbook into roles allows logical separation and enhances the reusability of components across different playbooks. |
| **Functionality**                   | Each role focuses on a particular functionality or desired output, with all necessary steps either within the role or in dependencies. |
| **Role Dependencies**               | Roles can depend on other roles, which helps in organizing tasks that need to be executed in a particular order.           |



## Can you explain the difference between vars, defaults, and set_fact?
---------------------------------------------------------------------------

1. vars: Variables defined in playbooks, inventories, or roles.
2. defaults: Default variables for roles, overridden by other variable sources.
3. set_fact: Sets variables dynamically during task execution, overriding other variable sources temporarily


 How do you use include_role and import_role? What is the difference?
 -----------------------------------------------------------------------

1. include_role: Dynamically includes a role at runtime, allowing for conditional execution.
2. import_role: Statically includes a role at parse time, making it part of the playbook structure.


What are some use cases for block and rescue in playbooks?
------------------------------------------------------------

block allows grouping tasks, while rescue provides error handling for tasks in the block. 
For example, using block for service deployment and rescue to revert changes if deployment fails.


 How do you optimize Ansible playbook performance?
------------------------------------------------------

1. Use free strategy for parallelism.
2. Avoid unnecessary gather_facts.
3. Cache facts using fact_caching.
4. Limit tasks to specific hosts with when conditions.


How would you handle rolling updates using Ansible?
----------------------------------------------------
Use the serial keyword to limit the number of hosts updated simultaneously, ensuring minimal downtime.




# How to Set Up a Jump Host to Access Servers Without Direct Access
---------------------------------------------------------------------

To configure a jump host, we need to use the `ansible_ssh_common_args` in inventory variable. 
This variable allows you to specify arguments that are appended to the `sftp/scp/ssh` command when connecting to relevant hosts.

## Example Configuration

## Inventory File:
cat inv.yml
-----------
[dev]

10.0.1.195


# Ansible Concepts
-----------------------

## 1. SSH ProxyCommand Configuration

```
cd group_vars/dev

cat dev.yml

ansible_ssh_user: deploy
ansible_password: "{{ vault_ansible_password }}"
gw_password: "{{ vault_gw_password }}"

cat gw.yml

ansible_ssh_common_args: "-o ProxyCommand=\"sshpass -p '{{gw_password}}' ssh -W %h:%p -t -q deploy@54.226.39.33\""

cat vault.yml
ansible_password: "pass1234"
gw_password: "pass1234"


| Parameter            | Description                                                                                                                                                  |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. `-o`             | Used to pass SSH options directly to the `ssh` command. It allows configuring specific behavior or settings for the SSH connection.                         |
| 2. `ProxyCommand`    | Specifies a command that is used as an intermediary to connect to the target host. In this case, it runs `sshpass` and then `ssh` for forwarding connections.|
| 3. `sshpass -p '{{gw_password}}'` | Supplies the password (`{{gw_password}}`) non-interactively using the `sshpass` utility for authentication.                                     |
| 4. `ssh -W %h:%p`    | The `-W` option forwards the standard input/output to the target host (`%h`) on the target port (`%p`). This is used to create a direct TCP connection.      |
| 5. `%h`              | Represents the target host's hostname or IP address as passed by Ansible.                                                                                    |
| 6. `%p`              | Represents the port number of the target SSH connection (default is 22).                                                                                     |
| 7. `-t`              | Forces a pseudo-terminal allocation. It is required for interactive processes that need a terminal, even if no terminal exists.                             |
| 8. `-q`              | Enables "quiet mode," suppressing most of the SSH output messages and reducing verbosity for cleaner output.                                                 |
| 9. `deploy@54.226.39.33` | Specifies the username (`deploy`) and gateway host (`54.226.39.33`) that will act as the SSH proxy/jump host.                                           |


                                                |

### Summary:
This command establishes an SSH connection to a target host through an intermediary gateway (`54.226.39.33`).
The `ProxyCommand` uses `sshpass` for password authentication and forwards the connection to the target
host and port (`%h:%p`) using the `-W` option. The `-t` ensures terminal allocation, and `-q`
suppresses unnecessary SSH output for clean execution.


```


cat vault.yml

cat hello.yml

Below is a sample `hello.yml` file:

```yaml

- hosts: dev
  tasks:
    - name: print hello
      shell: echo "hello world"
      register: helo

    - name: Print helo
      debug:
        msg: "helo output: {{ helo.stdout }}"
```

ansible -i ./inventory dev -m debug -a "msg={{host_var}}" --ask-vault-pass

ansible -i ./inventory dev -m debug -a "msg={{host_var}}" --vault-password-file /opt/apps/secret/.vault





## How to automate the password input in playbook using encrypted files?

ansible-playbook launch.yml --vault-password-file ~/ .vault_pass.py


## What are callback plugins in Ansible?

## Callback Plugins in Ansible
--------------------------------

Callback plugins in Ansible are used to control the output during the execution of commands and playbooks. They can enhance or modify 
the output behavior by adding additional functionality, such as logging or notifications.

### Common Callback Plugins:
-----------------------------
- **log_plays**: Records playbook events to a log file. This is useful for tracking the progress and outcomes of playbook executions.
- **mail**: Sends email notifications on playbook failures. This is helpful for alerting users or administrators when something goes wrong during execution.

### Custom Callback Plugins:
-----------------------------
Ansible also allows you to create and add your own custom callback plugins. To use a custom callback plugin, simply place the 
plugin file in the `callback_plugins` directory located adjacent to your playbook.

Callback plugins offer flexibility for extending the functionality of Ansible in terms of logging, notifications, 
and other custom behaviors during automation runs.



**What is the ad-hoc command in Ansible?**
-------------------------------------------

 Ad-hoc commands are like one-line playbooks to perform a specific task only. The syntax for the ad-hoc command is

 ansible atlanta -a "/sbin/reboot"  -u username --become 



# Ansible Tower and Its Features
----------------------------------

Ansible Tower is an enterprise-level solution by RedHat that provides a web-based console and REST API to manage Ansible across teams in an organization.

| **Feature**             | **Description**                                                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------------------------|
| **Workflow Editor**      | Allows setting up dependencies among playbooks, or running multiple playbooks maintained by different teams at once. |
| **Real-Time Analysis**   | Monitors the status of playbooks and tasks, and allows checking what's going to run next.                       |
| **Audit Trail**          | Tracks logs, making it easier to revert to a functional state if something goes wrong.                          |
| **Execute Commands Remotely** | Enables running commands on hosts or groups of hosts in the inventory.                                       |
| **Job Scheduling**       | Allows scheduling tasks to run at specified times.                                                             |
| **Notification Integration** | Integrates with various notification systems to alert users on job status or failures.                       |
| **CLI**                  | Provides a Command Line Interface for managing Ansible Tower from the terminal.                                |



## Explain how you will copy files recursively onto a target host?
--------------------------------------------------------------------
There’s a copy module that has a recursive parameter in it but there’s something called 
synchronize which is more efficient for large numbers of files. 



## How is the Ansible set_fact module different from vars, vars_file, or include_var?
-------------------------------------------------------------------------------------------

In Ansible, set_fact is used to set new variable values on a host-by-host basis which is just like ansible facts, discovered by the setup module. <br><br>
These variables are available to subsequent plays in a playbook. 






| **Feature**                | **Description**                                                                                                      |
|----------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Async**                   | Specifies the total time or maximum runtime allowed for the task. It defines how long the task is permitted to run before being timed out.  |
| **Poll**                    | Defines how frequently Ansible should check if the command has completed. The default value is 10 seconds.              |
| **Poll: 0 (Fire and Forget)** | With `poll: 0`, Ansible does not wait for the task to complete. It starts the task, disconnects, and doesn't check the status. 
It's useful when the task can run in the background and completion isn't necessary to wait for. |
| **Ansible async_status**    | Allows checking the status of an asynchronous task at any time. This is useful to track the progress of long-running tasks. |
| **Long-running tasks**      | Examples of tasks that could benefit from async: <br> 1. Downloading a large file from a URL <br> 2. Running long scripts <br> 3. Rebooting servers and waiting for them to come back online. |
| **Timeout**                 | If the async time is insufficient, Ansible will fail the playbook and display a timeout message.                       |



| No. | Type of Request   | Description                                                                                                                                 |
|-----|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Synchronous       | The request is made, and the program execution stops until a response is received from the HTTP server.                                      |
| 2   | Asynchronous      | The request is launched, and the program continues executing the code without waiting for the request to be completed.                      |







# Using SSH for Multiplexing in Ansible

| **Concept**                       | **Description**                                                                                                       |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **SSH Connection Delay**           | SSH connections take time to establish, and delays can accumulate across tasks if multiple connections are needed.      |
| **Ansible Task SSH Connections**   | Each task in Ansible creates a new SSH connection to the host, and delays in establishing connections can slow down execution. |
| **SSH Control Socket**             | SSH control sockets allow for multiplexing, meaning once a connection is established, subsequent connections can reuse the socket, reducing connection time. |
| **ControlPersist**                 | A feature in SSH that keeps an established control socket open for a period after its last use, reducing latency for future connections. |
| **Ansible Configuration**          | Changes to `ssh_connection` and `ControlPersist` settings can be made in the global Ansible configuration file to enable SSH multiplexing. |



## Enable SSH pipelining

| **Feature**                | **Description**                                                                                                      |
|----------------------------|----------------------------------------------------------------------------------------------------------------------|
| **SSH Pipelining**          | By default, SSH establishes a new connection to the target host for each task, which can slow down the process.       |
| **Single Connection**      | Enabling pipelining allows Ansible to use a single connection for executing multiple tasks on the target, reducing overhead. |
| **Impact on Performance**  | Reduces the number of SSH connections, which helps improve performance by avoiding delays caused by establishing multiple connections. |
| **Configuration Required** | SSH pipelining is not enabled by default. It requires extra configuration on the target host, particularly to allow sudo without a password. |



## Forking Ansible

| **Feature**           | **Description**                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------|
| **Parallel Execution** | Ansible operates in parallel across multiple hosts, executing tasks concurrently.                             |
| **Default Forks**     | The default value for forks is 5, which limits Ansible to operating on a maximum of five hosts at once.       |
| **Custom Forks**      | The number of forks can be adjusted (e.g., setting forks to 500), and it will respect the number of target hosts (e.g., four hosts will result in four forks). |


## Do you need fact gathering?
--------------------------------

| **Feature**             | **Description**                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------|
| **Fact Gathering**      | Fact gathering is enabled by default at the start of each play, collecting information from each host.         |
| **Hostvars**            | Facts gathered are stored as `hostvars`, which can be used in playbooks if needed.                             |
| **Impact on Performance** | Fact gathering is resource-intensive and slow, taking up to 3+ seconds per host, impacting overall execution time. |
| **Recommendation**      | It is recommended to disable fact gathering if not needed to save time and resources. Use `gather_facts: no` to disable. |



**Concurrent tasks with async**
--------------------------------

The async task parameter is interesting. It will cause Ansible to close the connection once the task is running. Ansible will 
re-establish a connection after a certain interval to see if the task has completed. This can be useful to get a large fleet 
all working on a task as quickly as possible. However, it can also increase the number of connections, as Ansible will connect back 
frequently to check on the status. If this frequency is made low, you could wind up with hosts sitting finished and idle, 
waiting for the frequency timer to run down for Ansible to check back in

**Use pull mode to check for changes**
------------------------------------

Pull mode is another strategy to increase efficiency. As I wrote above, one of the limitations I experienced was my Ansible control 
host's ability to manage more than 500 forks. Pull mode (Ansible-Pull plugin) is a way to spread the processing requirements across the fleet.


**Ansible Mitogen Strategy Plugin**
----------------------------------------

1. Mitogen is a strategy plugin for Ansible that significantly speeds up the performance of playbooks.

2. **Considerations**:  
   - There might be conflicts with the current strategies configured in your playbooks.  
   - Some tasks (e.g., raw tasks) may not work with the `mitogen_linear` strategy.  

3. **Configuration Steps**:  
   - Download the Mitogen plugin from its official website.  
   - Ensure you get the correct version compatible with your Ansible version.  
   - Uncompress the downloaded file to a location of your choice.  
   - Add the required configuration to your Ansible configuration file under the `defaults` section.


[defaults]

strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy

strategy = mitogen_linear


[defaults]

strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy

strategy = mitogen_linear

**Caching facts**
--------------------
You can cache facts so they do not have to be gathered again in subsequent runs. There are several cache backends that you can configure.
Using redis in your ansible.cfg would look like this:

[defaults]


fact_caching = redis
fact_caching_prefix = ansible_facts_
fact_caching_connection = localhost
fact_caching_timeout = 21600


Smart gathering
------------------
You can configure Ansible to gather facts only once so if you include a different playbook they are not gathered again. 
You can do this by setting the gathering to smart in the Ansible configuration file.

Debugging
------------
If you want to know which tasks take more time and have a nice summary, you can add this to your configuration.


[defaults]
callback_whitelist = profile_tasks
stdout_callback = debug


# set plugin path directories here, separate with colons
action_plugins     = /usr/share/ansible/plugins/action
#become_plugins     = /usr/share/ansible/plugins/become
#cache_plugins      = /usr/share/ansible/plugins/cache
callback_plugins   = /usr/share/ansible/plugins/callback
connection_plugins = /usr/share/ansible/plugins/connection
lookup_plugins     = /usr/share/ansible/plugins/lookup
inventory_plugins  = /usr/share/ansible/plugins/inventory
vars_plugins       = /usr/share/ansible/plugins/vars
filter_plugins     = /usr/share/ansible/plugins/filter
#test_plugins       = /usr/share/ansible/plugins/test
#terminal_plugins   = /usr/share/ansible/plugins/terminal
#strategy_plugins   = /usr/share/ansible/plugins/strategy




**Idempotency**
--------------
| No. | Aspect                        | Description                                                                                                                                             |
|-----|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Definition                    | Idempotency in Ansible ensures that running a task or playbook multiple times does not cause unnecessary changes if the system is already in the desired state. |
| 2   | Example                       | If a playbook installs a software package, running it again won't reinstall the software unless it has been uninstalled or changed.                      |
| 3   | Behavior                      | Ansible checks if the desired state is already achieved, and if so, it makes no changes.                                                                |
| 4   | Benefit                       | Helps maintain system consistency and prevents unnecessary changes, ensuring that only needed modifications are made.                                      |








| No. | Keyword   | Description                                                                                                                                     |
|-----|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | block     | 1. Used to define a block of tasks that may succeed or fail as a group.                                                                         |
|     |           | 2. Inside the block, there is a task that might fail (e.g., running a command).                                                                 |
| 2   | rescue    | 1. Defines a block of tasks executed if any task inside the block fails. It catches and handles the failure.                                    |
|     |           | 2. Inside the rescue block:                                                                                                                     |
|     |           |    - 1. A task handles the failure, such as printing information about the failed task (`ansible_failed_result`).                               |
| 3   | always    | 1. Defines a block of tasks that are always executed, regardless of whether the tasks inside the block succeed or fail.                         |
|     |           | 2. Inside the always block:                                                                                                                     |
|     |           |    - 1. A task cleans up after the previous tasks, such as logging or performing additional cleanup actions.                                    |








| No. | Aspect                          | Description                                                                                                                                          |
|-----|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Handling Results                | Once the asynchronous task completes, Ansible processes the results according to the specified poll interval.                                         |
| 2   | async_status Module             | Used to retrieve the status of the asynchronous task and gather any output or results generated by the task.                                          |
| 3   | Timeout                         | A timeout parameter can be specified to set a maximum time limit for the task to complete. If the task exceeds this limit, it is marked as failed.    |
| 4   | Launching Asynchronous Tasks    | Specifying `async` with a value greater than 0 launches a task asynchronously, allowing Ansible to move on to the next task immediately.               |
| 5   | Polling for Completion          | Ansible periodically polls the status of the asynchronous task to check completion. The `poll` parameter (default: 10 seconds) controls the interval. |
| 6   | Purpose of `async`              | The `async` keyword allows tasks to run asynchronously, useful for long-running tasks or commands that wait for external events to complete.           |



| No. | Aspect                      | Description                                                                                                                   |
|-----|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| 1   | Purpose                     | The `serial` keyword is used to control the number of hosts acted upon simultaneously during playbook execution.              |
| 2   | Default Behavior            | By default, Ansible runs tasks on all hosts concurrently, which can overwhelm target systems on large clusters.              |
| 3   | Using `serial`              | Specifies the maximum number of hosts to operate on concurrently. For example, `serial: 1` runs tasks on hosts one at a time. |
| 4   | Parallel Execution          | Setting `serial` to a value greater than 1 allows tasks to run on multiple hosts concurrently, up to the specified number.    |
| 5   | Use Cases                   | Useful for tasks with high system impact, such as software updates or configuration changes, to control resource usage.       |






| No. | Parameter | Description                                                                                                                  |
|-----|-----------|------------------------------------------------------------------------------------------------------------------------------|
| 1   | serial    | Controls the number of hosts targeted concurrently at the playbook level.                                                    |
| 2   | forks     | Controls the overall parallelism of Ansible runs at the command line or configuration level.                                 |


## forks:

| **Aspect**          | **Details**                                                                                                  |
|----------------------|------------------------------------------------------------------------------------------------------------|
| **Purpose**          | The `forks` setting is used to control the maximum number of parallel processes that Ansible can use when executing tasks across hosts. |
| **Scope**            | It applies at the command line level or in the Ansible configuration file (`ansible.cfg`) and affects the entire Ansible run, including all playbooks and tasks. |
| **Example**          | If `forks: 10` is set in the Ansible configuration, Ansible can execute tasks on up to 10 hosts concurrently. |
| **Typical Use Case** | Used to limit the overall system resource usage by restricting the number of parallel tasks Ansible can run, especially on systems with limited resources or when executing tasks across a large number of hosts. |



## serial:

| **Aspect**       | **Details**                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------|
| **Purpose**       | The `serial` keyword is used within a playbook to control how many hosts are targeted concurrently when running tasks across multiple hosts. |
| **Scope**         | It applies at the playbook level and affects the execution of tasks defined within that playbook. |
| **Example**       | If `serial: 2` is set in a playbook, Ansible will execute tasks on hosts in batches of 2 at a time. |
| **Typical Use Case** | Commonly used for tasks that need to be run sequentially on multiple hosts, such as rolling updates or configuration changes that should not overload the system. |


| **Aspect**               | **Ansible Serial**                                   | **Ansible Forking**                                |
|---------------------------|-----------------------------------------------------|---------------------------------------------------|
| **Definition**            | Controls how many hosts are processed in sequence.  | Defines the number of parallel tasks across hosts. |
| **Execution Model**       | Processes hosts in batches sequentially.            | Executes tasks concurrently on multiple hosts.    |
| **Use Case**              | Useful for gradual deployments or rolling updates.  | Ideal for speeding up operations on large inventories. |
| **Control**               | Defined in the playbook using `serial`.             | Configured in `ansible.cfg` with the `forks` option. |
| **Default Behavior**      | Defaults to processing all hosts unless specified.  | Default `forks` value is 5, configurable.         |








| **Aspect**          | **Remote User**                                          | **Become User**                                |
|----------------------|---------------------------------------------------------|-----------------------------------------------|
| **Definition**       | The user used to connect to the remote host.            | The user to switch to for executing privileged tasks. |
| **Configuration**    | Specified using `ansible_user` or `-u` CLI option.      | Enabled using `become: yes` and `become_user`. |



| **Aspect**             | **Command Module**                                      | **Shell Module**                                         |
|-------------------------|--------------------------------------------------------|---------------------------------------------------------|
| **Execution**           | Executes commands without invoking a shell.            | Executes commands through a shell (e.g., `/bin/sh`).     |
| **Features**            | Does not support shell features like pipes, redirects. | Supports shell features like pipes (`|`) and redirects. |
| **Security**            | Safer as it avoids shell injection vulnerabilities.     | Prone to shell injection if input is not sanitized.     |



| **Aspect**             | **sudo -i**                                            | **sudo su -**                                          |
|-------------------------|-------------------------------------------------------|-------------------------------------------------------|
| **Primary Purpose**     | Simulates a login shell for the target user.           | Switches to the target user with a login shell.       |
| **Environment Handling**| Clears the environment and initializes as a login.     | Inherits some environment variables from the caller.  |
| **Preferred Usage**     | Directly uses the target user’s shell and environment. | Runs an intermediary `su` command before switching.  |






## Examples

### System Variable
```bash
echo $PATH
# Output: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```







## Terraform vs Ansible
--------------------------


| Feature                         | Terraform                                                                                     | Ansible                                                                                     |
|---------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Primary Purpose**             | Infrastructure provisioning and management (e.g., provisioning a VPC, setting up an EC2 instance, configuring databases in the cloud). | Configuring and managing the software environment (e.g., installing packages, configuring web servers, ensuring correct firewall settings). |
| **Approach**                    | Declarative: Describes the desired state of infrastructure, and Terraform ensures it matches.| Imperative: Describes a series of tasks to execute in a specific order.                     |
| **State Management**            | Uses a state file (local or remote) to track infrastructure changes and manage drift detection.| No state file; relies on execution results from each run.                                   |
| **Idempotence**                 | Ensures infrastructure matches the desired state regardless of previous executions.          | Ensures repeated tasks result in the same outcome.                                          |
| **Agent Requirements**          | Agentless: Interacts directly with APIs of cloud providers or other services.                | Agentless: Uses SSH or WinRM for communication, with no agents required on target machines. |
| **Use Cases**                   | Provisioning infrastructure components like VPCs, EC2 instances, and cloud databases.        | Configuring systems, such as installing packages, setting up web servers, and managing firewalls. |



| **Advantage**                   | **Description**                                                                                                                                                          |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Automated Inventory Management** | Automatically generates and updates inventory, reducing the need for manual intervention and minimizing errors in environments where hosts frequently change.         |
| **Scalability**                 | Supports seamless scaling of infrastructure by automatically adding or removing hosts in environments like cloud platforms.                                             |
| **Flexibility**                 | Works with various systems such as cloud providers, virtualization platforms, and configuration management databases, allowing integration with existing infrastructure. |
| **Reduced Complexity**          | Simplifies inventory management by removing the need for manual updates, enabling teams to focus on building playbooks and automating tasks.                             |
| **Better Integration**          | Integrates with tools like monitoring and logging systems to provide a complete view of infrastructure, improving management, reducing downtime, and enhancing availability. |














                                          










