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

To configure a jump host, you need to use the `ansible_ssh_common_args` inventory variable. This variable allows you to specify arguments that are appended to the `sftp/scp/ssh` command when connecting to relevant hosts.

### Example Configuration

#### Inventory File:
ini
[gatewayed]
staging1 ansible_host=10.0.2.1
staging2 ansible_host=10.0.2.2


# Ansible Concepts

## 1. SSH ProxyCommand Configuration


ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q user@gateway.example.com"'

Explanation:
ProxyCommand: Specifies a command to use as a proxy for the connection.
-W %h:%p: Directs SSH to forward data to the specified host (%h) and port (%p).
-q: Enables quiet mode to suppress warnings or errors from the proxy host.
user@gateway.example.com: Specifies the user and jump host (gateway) through which the connection is established.


How to automate the password input in playbook using encrypted files?

To automate password input we can have a password file for all the passwords of encrypted files will be saved and ansible can make a call to fetch those when required.

ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q user@gateway.example.com"'
This can also be achieved by having a separate script that specifies the passwords. But in this case, we need to print a password to stdout to work without annoying errors.

ansible-playbook launch.yml --vault-password-file ~/ .vault_pass.py


What are callback plugins in Ansible?

Callback plugins basically control most of the output we see while running cmd programs. 
But it can also be used to add additional output. For example log_plays callback is used to record playbook events to a log file.
Mail callback is used to send email on playbook failures. We can also add custom callback plugins by dropping them into a callback_plugins directory adjacent to play.


What is the ad-hoc command in Ansible?
Ad-hoc commands are like one-line playbooks to perform a specific task only. The syntax for the ad-hoc command is

ansible [pattern] -m [module] -a "[module options]"
For example, we need to reboot all servers in the staging group

ansible atlanta -a "/sbin/reboot"  -u username --become [--ask-become-pass]

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



Explain how you will copy files recursively onto a target host?
There’s a copy module that has a recursive parameter in it but there’s something called synchronize which is more efficient for large numbers of files. 

For example:

- synchronize:
   src: /first/absolute/path
   dest: /second/absolute/path
   delegate_to: "{{ inventory_hostname }}"

How is the Ansible set_fact module different from vars, vars_file, or include_var?

In Ansible, set_fact is used to set new variable values on a host-by-host basis which is just like ansible facts, discovered by the setup module. 
These variables are available to subsequent plays in a playbook. 
In the case of vars, vars_file, or include_var we know the value beforehand whereas when using set_fact, we can store the value after preparing it on the fly using certain tasks like using filters or taking subparts of another variable.
We can also set a fact cache over it.


A Jenkins executor is one of the basic building blocks which allow a build to run on a node/agent (e.g. build server). Think of an executor as a single “process ID”,
or as the basic unit of resource that Jenkins executes on your machine to run a build.


A good value to start with would be the number of CPU cores on the machine.". But of course, depends on environment like RAM, tmp space amount, etc.. We have 8 cores, but only 5 executors at master node.


Async:
Async indicates the Total time to complete the task or its maximum runtime of the task.
Poll
poll indicates to Ansible, how often to poll to check if the command has been completed. or
how frequently you would like to poll for status. with poll we keep checking whether the job is completed or not. The default poll value is 10 seconds
poll: 0 Fire and forget
if you do not need to wait on the task to complete, you may run the task asynchronously by specifying a poll value of 0: In this mode ansible will connects to the client system, starts the process and disconnects. we don’t need to wait for completion task.



Ansible async_status
Ansible provides the option to get the task status in any time. Using ansible async_status we can get the status of async task at any time

Some of the long-running tasks could be
Downloading a Big File from URL
Running a Script known to run for a long time
Rebooting the remote server and waiting for it to comeback
 async keyword can tell Ansible how long the task should be allowed to run before Ansible gives it up and time out
 playbook would fail if the given async time is not suffcient and print the following timeout message



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



Enable SSH pipelining

By default, SSH establish connection to one target host multiple times for each task. 
Having multiple connections per task delays the process.
If the pipeline feature is enabled, it will setup a single connection to the target and remotely execute the module
It helps to reduce many connections to a single connection
It is not enabled by default, mainly because it requires extra configuration on the target host in order to make use of sudo


Forking Ansible

It operates in parallel across multiple hosts.
This parameter has a default of 5, which limit Ansible to operating on only five hosts at one time.
Setting forks at 500 and having a target of four hosts will result in four forks.

Do you need fact gathering?

Fact gathering is essentially an unwritten task. When it is turned on (the default) at the start of each play, each
host will get a task to gather facts from it. These facts will become hostvars. This is useful if you need the info, but it does take time.
I suggest you turn off fact gathering unless you depend on those facts. This is because gathering facts is resource-intensive and very, very slow; three seconds or more per host.
For example, if you have 100 hosts and 50 forks, that'll be 20*3s—or one minute—just to gather facts. This is wasted time if you're not using facts. You can set your playbook to not gather facts by adding the line gather_facts: no.


Concurrent tasks with async

The async task parameter is interesting. It will cause Ansible to close the connection once the task is running. Ansible will re-establish a connection after a certain interval to see if the task has completed. This can be useful to get a large fleet all working on a task as quickly as possible. However, it can also increase the number of connections, as Ansible will connect back frequently to check on the status. If this frequency is made low, you could wind up with hosts sitting finished and idle, waiting for the frequency timer to run down for Ansible to check back in

Use pull mode to check for changes

Pull mode is another strategy to increase efficiency. As I wrote above, one of the limitations I experienced was my Ansible control host's ability to manage more than 500 forks. Pull mode (Ansible-Pull plugin) is a way to spread the processing requirements across the fleet.


Mitogen

There is a strategy plugin for Ansible called Mitogen. This plugin is able to speed up the performance of your playbooks like magic.

There are some things to take into account, though. There might be conflicts with the current strategies configured in your playbooks and also some tasks my not work with the mitogen_linear strategy (i.e.: raw tasks).

To configure it you only have to download it from the Mitogen website, making sure to get the right version for your Ansible version and uncompress it wherever you want. Then you must add this to your configuration file in the defaults section.

[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear


[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear

Caching facts
You can cache facts so they do not have to be gathered again in subsequent runs. There are several cache backends that you can configure. Using redis in your ansible.cfg would look like this:

[defaults]
# Use 'redis' as backend
fact_caching = redis
# Prefix for 'redis' keys
fact_caching_prefix = ansible_facts_
# Connection to 'redis'
fact_caching_connection = localhost
# Cache for 6 hours
fact_caching_timeout = 21600


Smart gathering
You can configure Ansible to gather facts only once so if you include a different playbook they are not gathered again. You can do this by setting the gathering to smart in the Ansible configuration file.

Debugging
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

Cat test.yml

---
- name: Ansible Test Playbook
  gather_facts: false
  hosts: aws_region_us_east_1
  tasks:

    - name: Run Shell Command
      command: echo "Hello World"


Ec2 Autoscaling
Cat aws_ec2.yml
---
plugin: aws_ec2
regions:
  - us-east-1
keyed_groups:
  - key: tags
    prefix: tag


---
- hosts: sit
  tasks:
      - name: print hello
        shell: echo "hello world" 
        register: helo

      - name: Print helo
        debug:
          msg: "helo output: {{ helo.stdout }}"


Ec2 Autoscaling

ansible -i ec2.py -u ubuntu us-east-1d -m ping
ansible -i ec2.py -u deploy -m ping tag_app_1_my_dev 
ansible-playbook -i ec2.py test.yml -e "variable_host=tag_app_1_my_dev user=deploy"

ansible -i aws_ec2.yml tag_aws_autoscaling_groupName_test_asg -m shell -a "df -k" -u ec2-user --private-key=plato_key.pem

ansible-playbook -i aws_ec2.yml docker_handler.yml -u ec2-user --private-key=plato_key.pem --extra-vars "nodes=tag_aws_autoscaling_groupName_test_asg"


ansible-playbook -i aws_ec2.yml docker_handler.yml -u ec2-user --private-key=plato_key.pem --extra-vars "nodes=ec2-3-87-0-103.compute-1.amazonaws.com"


ansible all --list-hosts
ansible-inventory --graph
ansible-inventory --list
ansible all -m ping

ansible-inventory --list -i aws_ec2.yml
ansible -i aws_ec2.yml -m ping all
ansible -i aws_ec2.yml tag_aws_autoscaling_groupName_test_asg -m shell -a "df -k" -u ec2-user –-private-key=plato_key.pem
ansible -i aws_ec2.yml tag_OS_UBUNTU14  -m authorized_key -a "user=ec2-user key='{{ lookup('file', '/root/.ssh/id_rsa.pub') }}'"
ansible -i aws_ec2.yml tag_OS_UBUNTU14 -m shell -a "apt-get install nginx" -u ec2-user –private-key=plato-key.pem


ansible -i aws_ec2.yml -m ping aws_ec2
ansible -i ec2.py tag_OS_UBUNTU14 -m ping -u ubuntu – private-key=<keyfilename.pem>
ansible -i ec2.py tag_OS_UBUNTU14 -m shell -a "df -k" -u ubuntu – private-key=<keyfilename.pem>


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

Idempotency

Idempotency in Ansible means that when you run a task or playbook multiple times, it will not make unnecessary changes if the system is already in the desired state.
Imagine you have a playbook that installs a software package on a server. If you run that playbook once and the software is installed, running it again won't reinstall the software unless it's been uninstalled or changed. Ansible checks if the software is already there, and if it is, it doesn't do anything.
So, idempotency helps ensure that Ansible only makes changes when needed, which keeps your system consistent and avoids causing problems by making unnecessary changes.



- name: Example playbook with serial keyword
  hosts: all
  serial: 2   # This will run tasks on 2 hosts at a time
  tasks:
    - name: Ensure NTP service is running
      service:
        name: ntp
        state: started

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


The block keyword is used to define a block of tasks that may succeed or fail as a group.
Inside the block, we have a task that might fail (e.g., running a command).
The rescue keyword is used to define a block of tasks that should be executed if any task inside the block fails. It catches and handles the failure.
Inside the rescue, we have a task that handles the failure, printing information about the failed task (ansible_failed_result).
The always keyword is used to define a block of tasks that should always be executed, regardless of whether the tasks inside the block succeed or fail.
Inside the always, we have a task that cleans up after the previous tasks, such as logging or performing additional cleanup actions.


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



Handling Results: 
Once the asynchronous task completes, Ansible processes the results according to the specified poll interval. You can use the async_status module to retrieve the status of the asynchronous task and gather any output or results generated by the task.
Timeout: 
You can also specify a timeout parameter to set a maximum time limit for the asynchronous task to complete. If the task does not complete within the specified timeout period, Ansible will stop polling and mark the task as failed


Launching Asynchronous Tasks: 
When you specify async with a value greater than 0 for a task in your playbook, Ansible launches that task asynchronously and immediately moves on to the next task without waiting for the asynchronous task to complete.
Polling for Completion: 
Ansible periodically polls the status of the asynchronous task to check if it has completed. You can specify the interval for polling using the poll parameter, which defaults to 10 seconds.


In Ansible, 
the async keyword is used to run tasks asynchronously, 
meaning that Ansible does not wait for the task to complete before moving on to the next task. 
This can be particularly useful for long-running tasks, such as running a script that may take a significant amount of time to complete or executing commands that involve waiting for external events


In summary, while both serial and forks control the parallelism of task execution in Ansible, serial operates at the playbook level to control the number of hosts targeted concurrently,
while forks operates at the command line or configuration level to control the overall parallelism of Ansible runs.

forks:
Purpose: 
The forks setting is used to control the maximum number of parallel processes that Ansible can use when executing tasks across hosts.
Scope: 
It applies at the command line level or in the Ansible configuration file (ansible.cfg) and affects the entire Ansible run, including all playbooks and tasks.
Example: 
If forks: 10 is set in the Ansible configuration, Ansible can execute tasks on up to 10 hosts concurrently.
Typical Use Case: 
It's used to limit the overall system resource usage by restricting the number of parallel tasks Ansible can run, especially on systems with limited resources or when executing tasks across a large number of hosts.


serial:
Purpose: 
The serial keyword is used within a playbook to control how many hosts are targeted concurrently when running tasks across multiple hosts.
Scope: 
It applies at the playbook level and affects the execution of tasks defined within that playbook.
Example: 
If serial: 2 is set in a playbook, Ansible will execute tasks on hosts in batches of 2 at a time.
Typical Use Case: 
It's commonly used for tasks that need to be run sequentially on multiple hosts, such as rolling updates or configuration changes that should not overload the system


Serial:
In Ansible playbook, the serial keyword is used to control the number of hosts that are acted upon at the same time during playbook execution. It allows you to define how many hosts should be targeted concurrently when running tasks across multiple hosts.

Default Behavior: 
By default, Ansible runs tasks on all hosts simultaneously. This can be efficient, but it can also overwhelm the target systems if too many tasks are executed at once, especially on large clusters.

Using serial Keyword: 
You can use the serial keyword to specify the maximum number of hosts to operate on concurrently. For example, if you set serial: 1, Ansible will run tasks on hosts one at a time, serially

Parallel Execution: 
If you set serial to a value greater than 1, Ansible will execute tasks on multiple hosts concurrently, up to the specified number. This allows for faster execution while still controlling the load on the target systems.

Use Cases: The serial keyword is often used when performing tasks that may have a high impact on system resources, such as software updates or configuration changes
































