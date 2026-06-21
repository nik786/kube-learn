
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

| Area | Checks |
|--------|--------|
| **D = Disk** | - Check disk space on Jenkins agents.<br>- Verify disk I/O performance.<br>- Check filesystem health. |
| **N = Network** | - Verify network connectivity to the artifact repository.<br>- Check network latency and bandwidth. |
| **P = Plugin** | - Review Jenkins plugin versions.<br>- Check build logs for plugin-related errors. |
| **P = Proxy / Timeout** | - Validate proxy configurations.<br>- Review timeout settings.<br>- Implement retry mechanisms for transient failures. |
| **Repository Validation** | - Review artifact repository logs.<br>- Check Azure Blob Storage, Artifactory, or Nexus access logs. |

- **Repository Validation**
  - Review artifact repository logs.
  - Check Azure Blob Storage, Artifactory, or Nexus access logs.
