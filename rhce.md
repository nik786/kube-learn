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
