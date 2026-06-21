
Azure DevOps / SRE Interview Quick Revision Guide
---------------------------------------------------
11. Jenkins Jobs Randomly Failing at Artifact Upload
    -------------------------------------------------

Memory Trick: DNPP
--------------------
```
D = Disk I/O
N = Network Bandwidth
P = Plugin Issues
P = Proxy / Timeout
Interview Answer

```

Interview Answer
------------------
```
I would first check disk I/O and network bandwidth on Jenkins agents.
Then verify connectivity and access logs of the artifact repository such as Azure Blob Storage, Artifactory, or Nexus.
Finally, review plugin versions, proxy settings, timeout configurations, and implement retry mechanisms if required.
```
