
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

- **D = Disk**
  - Check disk space on Jenkins agents.
  - Verify disk I/O performance.
  - Check filesystem health.

- **N = Network**
  - Verify network connectivity to the artifact repository.
  - Check network latency and bandwidth.

- **P = Plugin**
  - Review Jenkins plugin versions.
  - Check build logs for plugin-related errors.

- **P = Proxy / Timeout**
  - Validate proxy configurations.
  - Review timeout settings.
  - Implement retry mechanisms for transient failures.

- **Repository Validation**
  - Review artifact repository logs.
  - Check Azure Blob Storage, Artifactory, or Nexus access logs.
