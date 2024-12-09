What are the features of Ansible?
It has the following features:

| **Feature**            | **Description**                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| **Agentless**           | Unlike Puppet or Chef, Ansible does not require an agent to manage the nodes.                                   |
| **Python-Based**        | Built on Python, making it easy to learn and write scripts; Python is a robust and widely-used programming language. |
| **SSH-Based**           | Uses passwordless network authentication (SSH), ensuring secure and simple setup.                              |
| **Push Architecture**   | Pushes small configuration codes to client nodes to execute actions.                                           |
| **Easy Setup**          | Simple to set up with a low learning curve; it's open-source, allowing anyone to get hands-on experience.       |
| **Manage Inventory**    | Stores machine addresses in a simple text format and supports plugins like OpenStack and Rackspace to pull inventory. |


# Ansible Roles

| **Concept**                        | **Description**                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Role Framework**                  | Roles provide a framework for organizing variables, tasks, files, templates, and modules into independent or interdependent collections. |
| **Primary Mechanism for Playbooks** | In Ansible, roles are the primary way to break down complex playbooks into smaller, reusable components.                  |
| **Simplification**                  | Using roles simplifies writing complex playbooks and makes them easier to maintain and reuse.                             |
| **Reusability**                     | Breaking a playbook into roles allows logical separation and enhances the reusability of components across different playbooks. |
| **Functionality**                   | Each role focuses on a particular functionality or desired output, with all necessary steps either within the role or in dependencies. |
| **Role Dependencies**               | Roles can depend on other roles, which helps in organizing tasks that need to be executed in a particular order.           |




# How to Set Up a Jump Host to Access Servers Without Direct Access

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


cd group_vars/dev

cat dev.yml

ansible_ssh_user: deploy
ansible_password: "{{ vault_ansible_password }}"
gw_password: "{{ vault_gw_password }}"

cat gw.yml

ansible_ssh_common_args: "-o ProxyCommand=\"sshpass -p '{{gw_password}}' ssh -W %h:%p -t -q deploy@54.226.39.33\""

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


## Explanation:
-------------------

ProxyCommand: Specifies a command to use as a proxy for the connection.

-W %h:%p: Directs SSH to forward data to the specified host (%h) and port (%p).

-q: Enables quiet mode to suppress warnings or errors from the proxy host.

user@gateway.example.com: Specifies the user and jump host (gateway) through which the connection is established.


## How to automate the password input in playbook using encrypted files?

ansible-playbook launch.yml --vault-password-file ~/ .vault_pass.py


## What are callback plugins in Ansible?

## Callback Plugins in Ansible

Callback plugins in Ansible are used to control the output during the execution of commands and playbooks. They can enhance or modify the output behavior by adding additional functionality, such as logging or notifications.

### Common Callback Plugins:
- **log_plays**: Records playbook events to a log file. This is useful for tracking the progress and outcomes of playbook executions.
- **mail**: Sends email notifications on playbook failures. This is helpful for alerting users or administrators when something goes wrong during execution.

### Custom Callback Plugins:
Ansible also allows you to create and add your own custom callback plugins. To use a custom callback plugin, simply place the plugin file in the `callback_plugins` directory located adjacent to your playbook.

Callback plugins offer flexibility for extending the functionality of Ansible in terms of logging, notifications, and other custom behaviors during automation runs.



**What is the ad-hoc command in Ansible?**

 Ad-hoc commands are like one-line playbooks to perform a specific task only. The syntax for the ad-hoc command is

 ansible atlanta -a "/sbin/reboot"  -u username --become 



# Ansible Tower and Its Features

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
There’s a copy module that has a recursive parameter in it but there’s something called synchronize which is more efficient for large numbers of files. 

For example:

- synchronize:
   src: /first/absolute/path
   dest: /second/absolute/path
   delegate_to: "{{ inventory_hostname }}"

## How is the Ansible set_fact module different from vars, vars_file, or include_var?

In Ansible, set_fact is used to set new variable values on a host-by-host basis which is just like ansible facts, discovered by the setup module. 
These variables are available to subsequent plays in a playbook. 
In the case of vars, vars_file, or include_var we know the value beforehand whereas when using set_fact, we can store the value after preparing it on the fly using certain tasks like using filters or taking subparts of another variable.
We can also set a fact cache over it.


## A Jenkins executor is one of the basic building blocks which allow a build to run on a node/agent (e.g. build server). Think of an executor as a single “process ID”,
   or as the basic unit of resource that Jenkins executes on your machine to run a build.


## A good value to start with would be the number of CPU cores on the machine.". But of course, depends on environment like RAM, tmp space amount, etc.. We have 8 cores, but only 5 executors at master node.


| **Feature**                | **Description**                                                                                                      |
|----------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Async**                   | Specifies the total time or maximum runtime allowed for the task. It defines how long the task is permitted to run before being timed out.  |
| **Poll**                    | Defines how frequently Ansible should check if the command has completed. The default value is 10 seconds.              |
| **Poll: 0 (Fire and Forget)** | With `poll: 0`, Ansible does not wait for the task to complete. It starts the task, disconnects, and doesn't check the status. It's useful when the task can run in the background and completion isn't necessary to wait for. |
| **Ansible async_status**    | Allows checking the status of an asynchronous task at any time. This is useful to track the progress of long-running tasks. |
| **Long-running tasks**      | Examples of tasks that could benefit from async: <br> 1. Downloading a large file from a URL <br> 2. Running long scripts <br> 3. Rebooting servers and waiting for them to come back online. |
| **Timeout**                 | If the async time is insufficient, Ansible will fail the playbook and display a timeout message.                       |





become_user: user1 = Using sudo from become:yes and becoming user user1.

remote_user: user1 = Log in as foofoo on that remote server

On a s̲y̲n̲c̲h̲r̲o̲n̲o̲u̲s̲ request, you make the request and stop executing your program until you get a response from the HTTP server

On a̲s̲y̲n̲c̲h̲r̲o̲n̲o̲u̲s̲ requests, you "launch" the request, and you kind of "forget about it", meaning: The interpreter continues executing the code after the request is made without waiting for the request to be completed.

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

The async task parameter is interesting. It will cause Ansible to close the connection once the task is running. Ansible will re-establish a connection after a certain interval to see if the task has completed. This can be useful to get a large fleet all working on a task as quickly as possible. However, it can also increase the number of connections, as Ansible will connect back frequently to check on the status. If this frequency is made low, you could wind up with hosts sitting finished and idle, waiting for the frequency timer to run down for Ansible to check back in

**Use pull mode to check for changes**
------------------------------------

Pull mode is another strategy to increase efficiency. As I wrote above, one of the limitations I experienced was my Ansible control host's ability to manage more than 500 forks. Pull mode (Ansible-Pull plugin) is a way to spread the processing requirements across the fleet.


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
You can cache facts so they do not have to be gathered again in subsequent runs. There are several cache backends that you can configure. Using redis in your ansible.cfg would look like this:

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


Ec2 Autoscaling

[inventory]

enable_plugins = aws_ec2

inventory      = /opt/ansible/inventory/aws_ec2.yaml



ansible-inventory -i aws_ec2.yaml --list

ansible aws_region_us_west_2 -m ping

## Cat test.yml
```yaml
---
- name: Ansible Test Playbook
  gather_facts: false
  hosts: aws_region_us_east_1
  tasks:

    - name: Run Shell Command
      command: echo "Hello World"
```

# Ec2 Autoscaling
## Cat aws_ec2.yml

```yaml
---
plugin: aws_ec2
regions:
  - us-east-1
keyed_groups:
  - key: tags
    prefix: tag
```

```yaml
---
- hosts: sit
  tasks:
      - name: print hello
        shell: echo "hello world" 
        register: helo

      - name: Print helo
        debug:
          msg: "helo output: {{ helo.stdout }}"
```

Ansible commands - 01
-----------------------

1. `ansible -i ec2.py -u ubuntu us-east-1d -m ping`
2. `ansible -i ec2.py -u deploy -m ping tag_app_1_my_dev`
3. `ansible-playbook -i ec2.py test.yml -e "variable_host=tag_app_1_my_dev user=deploy"`
4. `ansible -i aws_ec2.yml tag_aws_autoscaling_groupName_test_asg -m shell -a "df -k" -u ec2-user --private-key=plato_key.pem`
5. `ansible-playbook -i aws_ec2.yml docker_handler.yml -u ec2-user --private-key=plato_key.pem --extra-vars "nodes=tag_aws_autoscaling_groupName_test_asg"`
6. `ansible-playbook -i aws_ec2.yml docker_handler.yml -u ec2-user --private-key=plato_key.pem --extra-vars "nodes=ec2-3-87-0-103.compute-1.amazonaws.com"`
7. `ansible all --list-hosts`
8. `ansible-inventory --graph`
9. `ansible-inventory --list`
10. `ansible all -m ping`
11. `ansible-inventory --list -i aws_ec2.yml`
12. `ansible -i aws_ec2.yml -m ping all`
13. `ansible -i aws_ec2.yml tag_aws_autoscaling_groupName_test_asg -m shell -a "df -k" -u ec2-user –-private-key=plato_key.pem`
14. `ansible -i aws_ec2.yml tag_OS_UBUNTU14  -m authorized_key -a "user=ec2-user key='{{ lookup('file', '/root/.ssh/id_rsa.pub') }}'"`
15. `ansible -i aws_ec2.yml tag_OS_UBUNTU14 -m shell -a "apt-get install nginx" -u ec2-user –private-key=plato-key.pem`
16. `ansible -i aws_ec2.yml -m ping aws_ec2`
17. `ansible -i ec2.py tag_OS_UBUNTU14 -m ping -u ubuntu – private-key=<keyfilename.pem>`
18. `ansible -i ec2.py tag_OS_UBUNTU14 -m shell -a "df -k" -u ubuntu – private-key=<keyfilename.pem>`


Ansible commands - 02
-----------------------

1. `ansible-playbook test.yml  -v -vvvv -u deploy -i ec2.py`
2. `./ec2.py --host ec2-12-12-12-12.compute-1.amazonaws.com`
3. `ansible -i ec2.py -m ping tag_app_1_my_dev -u deploy`
4. `ansible -i ec2.py -u ubuntu us-east-1d -m ping`
5. `ansible -i ec2.py -u deploy -m ping tag_app_1_my_dev`
6. `ansible -i ./ec2.py --limit`
7. `ansible -i ec2.py --limit "tag_app-1_my-dev:&tag_app-2_my-dev-2" -m ping all`
8. `ansible -i ec2.py --limit "tag_app-1_my-dev" -m ping all`
9. `"tag_app-1_my-dev"`
10. `ansible -i ec2.py -u ubuntu us-east-1d -m ping`
11. `./ec2.py --list --profile default --refresh-cache`
12. `./ec2.py –list`
13. `ansible -i inventory/ec2.py -u ec2-user us-east-1a -m ping --key-file=vpn41.pem`
14. `ANSIBLE_PYTHON_INTERPRETER=auto_silent ansible -i inventory/ec2.py -u ec2-user us-east-1a -m ping --key-file=vpn41.pem`
15. `ANSIBLE_PYTHON_INTERPRETER=auto_silent ansible -i inventory/ec2.py -u ec2-user 44.199.209.84 -m ping --key-file=vpn41.pem`
16. `ANSIBLE_PYTHON_INTERPRETER=auto_silent ansible-playbook -i inventory/ec2.py -u ec2-user helo.yml --key-file=vpn41.pem --extra-vars "host=us-east-1a"`
17. `ansible-role nginx -i 192.168.10.27`
18. `ansible-playbook -i  "192.168.10.27" --tags "nginx"`
19. `ansible-playbook nginx-v.1.0.1.yml --extra-vars "variable_host=192.168.10.27"`
20. `ansible-playbook nginx-v.1.0.1.yml -i /etc/ansible/infra --extra-vars "host=web"`
21. `ansible-playbook release.yml --extra-vars "hosts=vipers user=starbuck"`
22. `ansible-playbook nginx-v.1.0.1.yml -i /etc/ansible/inventory --extra-vars "host=web user=deploy"`
23. `ansible-playbook nik-zoo.yml --extra-vars "host=web user=deploy"`
24. `ansible-playbook nik-zoo.yml --extra-vars "nodes=sandbox user=deploy"`
25. `ansible-playbook -i local-inventory.yml nik-zoo.yml --extra-vars "nodes=sandbox user=deploy"`
26. `ansible-role  --verbose --gather --extra-vars "variable_host=192.168.10.27" -i /etc/ansible/infra --hosts web --become yes --user deploy roles/nginx`
27. `date +"%m-%d-%y"`
28. `ansible-playbook play.yml -i hosts/dev/inventory --extra-vars "nodes=web user=deploy"`
29. `ansible-playbook nginx-v.1.0.1.yml -i hosts/dev/inventory --extra-vars "nodes=web user=deploy"`
30. `ansible-playbook test.yml -i ec2.py --extra-vars "user=deploy"`
31. `ansible-playbook test.yml  -v -vvvv -u deploy -i ec2.py`
32. `./ec2.py --host ec2-12-12-12-12.compute-1.amazonaws.com`
33. `ansible -i ec2.py -m ping tag_app_1_my_dev -u deploy`
34. `ansible -i ec2.py -u ubuntu us-east-1d -m ping`
35. `ansible -i ec2.py -u deploy -m ping tag_app_1_my_dev`
36. `ansible-playbook -i ec2.py test.yml -e "variable_host=tag_app_1_my_dev user=deploy"`
37. `ansible-playbook test-1.yml -i aws_inventory-root.yml --extra-vars "nodes=web" -vvvv`
38. `ansible-playbook test.yml -i aws-inventory-sudo.yml --extra-vars "nodes=web" -vvvv`
39. `ansible -i aws_inventory-root.yml -u root -m ping web`
40. `ansible -i aws_inventory-sudo.yml -u deploy -m ping web`
41. `ansible -i inventory/default/aws-inventory-sudo.yml -u deploy -m ping web`
42. `ansible-playbook play.yml -i aws_inventory-root.yml --extra-vars "nodes=web" -vvvv`
43. `ansible -i aws_inventory-root.yml -u root -m shell -a 'free -m' web123`
44. `ansible -i aws_inventory-sudo.yml -u deploy -m shell -a 'free -m' web123`
45. `ansible-playbook test.yml -i aws-inventory-sudo.yml --extra-vars "nodes=web" -vvvv`
46. `ansible-playbook playbooks/sc/test.yml -i inventory/default/aws-inventory-sudo.yml --extra-vars "nodes=qa"`
47. `ansible -i ./ec2.py --limit`
48. `ansible -i ec2.py --limit "tag_app-1_my-dev:&tag_app-2_my-dev-2" -m ping all`
49. `ansible -i ec2.py --limit "tag_app-1_my-dev" -m ping all`
50. `"tag_app-1_my-dev"`
51. `ansible -i ec2.py -u ubuntu us-east-1d -m ping`
52. `./ec2.py --list --profile default --refresh-cache`
53. `./ec2.py –list`
54. `ansible-inventory -i aws_ec2.yml --list`
55. `ansible -i aws_ec2.yml all -m ping -u ec2-user --key-file=ag-key.pem`
56. `ansible -i aws_ec2.yml all -m shell -a 'free -m' -u ec2-user --key-file=ag-key.pem`
57. `ansible -i aws_ec2.yml tag_Name_bastion_jenkins -m shell -a 'free -m' -u ec2-user --key-file=ag-key.pem`
58. `ansible-playbook -i aws_ec2.yml mem.yml -e "nodes=ec2-15-206-81-141.ap-south-1.compute.amazonaws.com user=ec2-user ansible_ssh_private_key_file=/home/nik/Desktop/ansible/aws-connect/ag-key.pem"`
59. `ansible-playbook -i aws_ec2.yml mem.yml -e "nodes=tag_Name_bastion_jenkins user=ec2-user ansible_ssh_private_key_file=/home/nik/Desktop/ansible/aws-connect/ag-key.pem"`





```yaml

---
- name: Run Shell Command without Host Key Checking
  hosts: "{{ nodes }}"
  become: true
  gather_facts: false
  environment:
    ANSIBLE_HOST_KEY_CHECKING: "False"
  tasks:
    - name: Run Shell Command
      shell: "df -k"
      register: df_output

    - name: Print Output
      debug:
        var: df_output.stdout_lines

    - name: Check if ECS agent is running
      shell: "docker ps -q -f name=ecs-agent"
      register: ecs_agent_container_id
      ignore_errors: true

    - name: Start ECS agent if not running
      shell: "docker start ecs-agent"
      when: ecs_agent_container_id.stdout == ""

    - name: Pull the latest Docker image
      shell: "docker pull nik786/blue-flask:27"
      register: docker_pull_result

```



```yaml

---
- name: Set up a cron job
  hosts: your_hosts
  become: true
  tasks:
    - name: Add a cron job to run a script every day at 1 AM
      cron:
        name: "Run my script"
        minute: 0
        hour: 1
        job: "/path/to/your/script.sh"

```

**Idempotency**
--------------

Idempotency in Ansible means that when you run a task or playbook multiple times, it will not make unnecessary changes if the system is already in the desired state.<br><br>
Imagine you have a playbook that installs a software package on a server. If you run that playbook once and the software is installed, running it again won't reinstall the software unless it's been uninstalled or changed. <br><br>
Ansible checks if the software is already there, and if it is, it doesn't do anything.<br><br>
So, idempotency helps ensure that Ansible only makes changes when needed, which keeps your system consistent and avoids causing problems by making unnecessary changes.<br><br>


```yaml

- name: Example playbook with serial keyword
  hosts: all
  serial: 2   # This will run tasks on 2 hosts at a time
  tasks:
    - name: Ensure NTP service is running
      service:
        name: ntp
        state: started

```

```yaml
---
- name: Example playbook with set_fact
  hosts: all
  tasks:
    - name: Set custom fact
      set_fact:
        my_custom_fact: "Hello, world!"

    - name: Print custom fact
      debug:
        msg: "The custom fact is {{ my_custom_fact }}"
```

The block keyword is used to define a block of tasks that may succeed or fail as a group.<br><br>
Inside the block, we have a task that might fail (e.g., running a command).<br><br>
The rescue keyword is used to define a block of tasks that should be executed if any task inside the block fails. It catches and handles the failure.<br><br>
Inside the rescue, we have a task that handles the failure, printing information about the failed task (ansible_failed_result).<br><br>
The always keyword is used to define a block of tasks that should always be executed, regardless of whether the tasks inside the block succeed or fail.<br><br>
Inside the always, we have a task that cleans up after the previous tasks, such as logging or performing additional cleanup actions.<br><br>



```yaml

---
- name: Example playbook with block, rescue, and always
  hosts: all
  tasks:
    - block:
        - name: Task that might fail
          command: /path/to/some/command
          register: result

        - name: Print command output
          debug:
            msg: "Command output: {{ result.stdout }}"
      rescue:
        - name: Handle task failure
          debug:
            msg: "Task failed: {{ ansible_failed_result }}"
      always:
        - name: Clean up after task
          debug:
            msg: "Cleaning up..."

    - name: Another task
      debug:
        msg: "This task always runs regardless of the outcome of the previous block"

```


```yaml
- hosts: all
  tasks:
    - name: Run a long-running command asynchronously
      shell: /path/to/long_running_script.sh
      async: 3600  # Run the task asynchronously for up to 1 hour
      poll: 0  # Disable polling for completion

    - name: Wait for the asynchronous task to complete
      async_status:
        jid: "{{ ansible_job_id }}"  # Use the job ID from the asynchronous task
      register: job_result
      until: job_result.finished
      retries: 360  # Poll the status every 10 seconds for up to 1 hour
      delay: 10  # Wait 10 seconds between retries

```



## Handling Results: 
Once the asynchronous task completes, Ansible processes the results according to the specified poll interval. <br><br>
You can use the async_status module to retrieve the status of the asynchronous  task and gather any output or results generated by the task.
Timeout: 
You can also specify a timeout parameter to set a maximum time limit for the asynchronous task to complete. 
If the task does not complete within the specified timeout period, Ansible will stop polling and mark the task as failed


## Launching Asynchronous Tasks: 
When you specify async with a value greater than 0 for a task in your playbook, Ansible launches that task asynchronously and immediately moves on to the next 
task without waiting for the asynchronous task to complete.<br><br>
Polling for Completion: 
Ansible periodically polls the status of the asynchronous task to check if it has completed. You can specify the interval for polling using the poll parameter, which defaults to 10 seconds.


In Ansible, <br><br>
the async keyword is used to run tasks asynchronously, 
meaning that Ansible does not wait for the task to complete before moving on to the next task. 
This can be particularly useful for long-running tasks, such as running a script that may take a significant amount of time to complete or executing commands that involve waiting for external events


In summary, <br><br>
while both serial and forks control the parallelism of task execution in Ansible, serial operates at the playbook level to control the number of hosts targeted concurrently,
while forks operates at the command line or configuration level to control the overall parallelism of Ansible runs.

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



## Serial:

In Ansible playbook, the serial keyword is used to control the number of hosts that are acted upon at the same time during playbook execution. 

It allows you to define how many hosts should be targeted concurrently when running tasks across multiple hosts.

Default Behavior: 

By default, Ansible runs tasks on all hosts simultaneously. 

This can be efficient, but it can also overwhelm the target systems if too many tasks are executed at once, especially on large clusters.

Using serial Keyword: 

You can use the serial keyword to specify the maximum number of hosts to operate on concurrently. 

For example, if you set serial: 

1, Ansible will run tasks on hosts one at a time, serially

Parallel Execution: 
If you set serial to a value greater than 1, Ansible will execute tasks on multiple hosts concurrently, up to the specified number. <br><br>
This allows for faster execution while still controlling the load on the target systems.<br><br>

Use Cases: The serial keyword is often used when performing tasks that may have a high impact on system resources, such as software updates or configuration changes
































