# Istio with Virtual Machine (VM) Workloads

| **Concept**                     | **Description**                                                                                                                                     |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **VM Integration**             | VM workloads can be integrated into the Istio service mesh and made part of it using specific configuration patterns.                             |
| **Architectures**              | There are two architectures for integrating VMs: Single-Network and Multi-Network.                                                                 |

## Architectures

| **Type**              | **Description**                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Single-Network**    | - VMs and Kubernetes are on the same network.<br>- They can communicate directly.<br>- Control plane traffic goes through the Gateway during VM bootstrap.   |
| **Multi-Network**     | - VMs and Kubernetes are on separate networks.<br>- No direct communication.<br>- All traffic (data + control) flows through the Gateway bridging both.      |

## Representing VM Workloads

| **Resource**           | **Description**                                                                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WorkloadGroup**      | Similar to a Kubernetes Deployment. Defines a logical group of VMs with shared properties. Acts as a template for VMs joining the mesh.                          |
| **WorkloadEntry**      | Similar to a Pod. Represents a single VM instance. Automatically created when a VM joins and deleted when it leaves the mesh.                                    |
| **Kubernetes Service** | Needed to provide stable access to VM workloads using hostname/IP. Also enables routing via `VirtualService` and `DestinationRule`.                              |

> ⚠️ Note: These Istio resources **do not provision or run VMs** — they simply reference existing VM workloads and allow them to be included in the service mesh configuration.

