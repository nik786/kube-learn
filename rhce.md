| **Aspect**              | **Zombie Process**                                         | **Orphan Process**                                   |
|-------------------------|-----------------------------------------------------------|----------------------------------------------------|
| **Definition**          | A process that has completed execution but still has an entry in the process table because its parent hasn’t read its exit status. | A process whose parent has terminated, making `init` (PID 1) or systemd its new parent. |
| **State**               | Exists in a `Z` (zombie) state in the process table.       | Continues to run normally under `init` or `systemd`.|
| **Impact**              | Consumes only a process table entry and no resources; can lead to resource exhaustion if too many zombies accumulate. | No negative impact, as `init`/`systemd` handles it effectively. |
| **Resolution**          | Requires the parent process to read the child's exit status or manual intervention (e.g., killing the parent). | No resolution needed; handled automatically by the system. |



| **Signal**    | **SIGTERM**                                        | **SIGKILL**                                      |
|---------------|----------------------------------------------------|-------------------------------------------------|
| **Definition**| A signal to terminate a process gracefully, allowing it to perform cleanup before exiting. | A signal to forcefully kill a process immediately without cleanup. |
| **Interceptable** | Can be caught or ignored by the process, allowing it to handle termination. | Cannot be intercepted, blocked, or ignored; ensures immediate termination. |






The TTL (Time to Live) in the context of networking is a field in the IP header that determines the maximum number 
of hops (routers) a packet can pass through before being discarded. Each time the packet is forwarded by a router, the TTL value is decremented by 1.


Meaning in ttl=64:
64 is the initial TTL value set by the operating system (common defaults are 64, 128, or 255).
This value indicates how many hops are left before the packet would expire. Since you're pinging 127.0.0.1 (localhost), 
the packet doesn't traverse any routers, so the TTL remains at its initial value.




# Zombie, Orphan, and Defunct Processes

### Comparison Table

| **Aspect**        | **Zombie Process**                                                                                                                                 | **Orphan Process**                                                                                                   | **Defunct Process**                                                                                                                                |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition**    | A process that has completed execution but remains in the process table because its parent hasn't read its exit status using `wait()`.            | A process whose parent has terminated, leaving it to be adopted by the `init` process (PID 1).                      | Essentially the same as a zombie process, a dead process whose exit status hasn’t been collected by the parent.                                   |
| **Key Feature**   | Consumes no CPU/memory but occupies a slot in the process table.                                                                                  | Continues to execute normally under the supervision of the `init` process.                                          | Marked as `<defunct>` in the process table.                                                                                                       |
| **State**         | Dead but not reaped by the parent.                                                                                                                | Running, adopted by the `init` process.                                                                             | Dead but not reaped (same as Zombie).                                                                                                             |
| **Handled By**    | Original parent process.                                                                                                                          | Adopted and handled by the `init` process.                                                                          | Original parent process.                                                                                                                          |
| **Command to Find** | `ps aux | grep Z`                                                                                                                                | `ps -eo pid,ppid,cmd | awk '$2 == 1 && $1 != 1'`                                                                    | `ps aux | grep '<defunct>'`                                                                                                                        |



# Difference Between Zombie and Defunct Processes

| **Aspect**         | **Zombie Process**                                                                               | **Defunct Process**                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Definition**     | A process that has completed execution but remains in the process table because its parent hasn't read its exit status. | A dead process whose exit status hasn’t been collected by its parent; essentially the same as a zombie process. |
| **State**          | Dead but waiting for the parent process to collect its exit status.                              | Dead, and appears as `<defunct>` in the process table.                                         |
| **Key Feature**    | Consumes no resources but occupies a slot in the process table.                                  | Same as Zombie but explicitly labeled `<defunct>` in the process list.                        |
| **Handled By**     | Original parent process must collect the exit status using `wait()`.                             | Original parent process; state persists until reaped.                                          |
| **Command to Find**| `ps aux  grep Z`                                                                                | `ps aux grep '<defunct>'`                                                                    |
| **Visibility**     | Marked as `Z` in the state column when listed in `ps`.                                           | Explicitly labeled as `<defunct>` in the command output.                                       |
