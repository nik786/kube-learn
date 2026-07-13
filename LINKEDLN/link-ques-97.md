
11. Origin vs Upstream in Git  
    Explain the difference between the origin and upstream remotes in a Git repository.

    | Feature | Origin | Upstream |
    |----------|--------|----------|
    | Meaning | My repository | Original repository |
    | Purpose | Where I push my code | Where I pull updates from |
    | Easy to Remember | **Origin = My Repo** | **Upstream = Original Repo** |

13. Docker Container Lifecycle  
    Describe the lifecycle of a Docker container, including how it is created, started, stopped, and deleted.

    | Stage | Description | Command |
    |-------|-------------|---------|
    | **Create** | Create a container from a Docker image | `docker create <image>` or `docker run <image>` |
    | **Start** | Start the container and run the application | `docker start <container>` |
    | **Stop** | Gracefully stop the running container | `docker stop <container>` |
    | **Restart** | Stop and start the container again | `docker restart <container>` |
    | **Delete** | Remove the container | `docker rm <container>` |

    ```
    Docker Container Lifecycle

      Image → Create → Start (Running) → Stop → Delete
   
    ```

15. Kubernetes ReplicaSet  
    Explain the concept of a ReplicaSet in Kubernetes and how it ensures that a specified number of replicas of a pod are running at any given time.

    | Question | One-Line Answer |
    |----------|-----------------|
    | **What is a ReplicaSet in Kubernetes?** | **A ReplicaSet ensures that the desired number of pod replicas are always running by automatically creating or replacing pods if any fail or are deleted.** |

    ### How It Works

    | Event | ReplicaSet Action |
    |--------|-------------------|
    | Pod crashes | Creates a new pod automatically |
    | Pod is deleted | Recreates the pod |
    | Fewer pods than desired | Creates additional pods |
    | More pods than desired | Deletes extra pods |
    | Cluster healthy | Maintains the desired number of replicas |

    ### Example

    | Desired Replicas | Running Pods | ReplicaSet Action |
    |------------------|--------------|-------------------|
    | 3 | 3 | No action |
    | 3 | 2 | Creates 1 new pod |
    | 3 | 4 | Deletes 1 extra pod |

    

17. Configuring a NAT Gateway in AWS  
    Describe how to configure a NAT gateway in AWS to enable outbound internet access for instances in a private subnet.

18. Deleting `/var/lib/docker/overlay` on a Docker Host  
    What happens when you delete the `/var/lib/docker/overlay` directory on a Docker host?

    | Action | Result |
    |--------|--------|
    | Delete `overlay2` | Container filesystem is lost |
    | Running containers | May crash or become unusable |
    | Docker images | Become corrupted or unavailable |
    | Container data | Lost if not stored in Docker volumes
    | Recommended? | No, never delete manually while Docker is running |

19. Running a VM Without EC2 in AWS  
    Is it possible to run a virtual machine (VM) in AWS without creating an EC2 instance? If so, how?

| Question | One-Line Answer |
|----------|-----------------|
| **Can you run a VM in AWS without EC2?** | **No, a traditional VM in AWS always runs on EC2, but AWS offers services like Lambda and Fargate where you can run applications without managing EC2 instances.** |

### Quick Summary

| Traditional VM | Serverless / Managed Compute |
|----------------|------------------------------|
| **EC2** | **Lambda** |
| **EC2** | **Fargate** |
| Full OS access | No OS management |
| You manage the server | AWS manages the infrastructure |



18. Stopping vs Terminating EC2 Instances  
    Explain the difference between stopping and terminating an EC2 instance. Additionally, describe the concept of EC2 hibernation and how it enables instances to be restarted from a saved state.
