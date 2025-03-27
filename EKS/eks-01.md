

| Feature                          | Managed Node Group                        | Self-Managed Node Group                  |
|----------------------------------|-------------------------------------------|------------------------------------------|
| Upgrade specific node            | ❌ Not supported                           | ✅ Possible manually                      |
| Upgrade entire group (rolling)   | ✅ Supported via `eksctl`                  | ✅ Supported via ASG + Launch Template    |
| Auto rejoin after upgrade        | ✅ Yes                                     | ✅ With proper bootstrap script           |
| Node control granularity         | ❌ Group-based only                        | ✅ Per-node control                       |

