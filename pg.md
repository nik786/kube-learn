| **ACID Property** | **Description**                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------|
| **Atomicity**      | Ensures that each transaction is all-or-nothing; either fully completed or fully rolled back.        |
| **Consistency**    | Guarantees that a transaction brings the database from one valid state to another.                   |
| **Isolation**      | Ensures that concurrent transactions do not interfere with each other, maintaining data integrity.    |
| **Durability**     | Ensures that once a transaction is committed, the data remains saved even in case of a system crash. |

Using ASCII Diagrams

```

                   +--------------------+
                   |  Internal ALB       |
                   | (Load Balancer)     |
                   +--------------------+
                             |
                             |
                     +---------------+
                     | Pgpool-II/HAProxy|
                     | (Connection Pool)|
                     +---------------+
                      /             \
         +------------------+   +------------------+
         | PostgreSQL ECS 1  |   | PostgreSQL ECS 2  |
         | (AZ 1)            |   | (AZ 2)            |
         +------------------+   +------------------+
              |                        |
         +----------+            +----------+
         |   EFS    |            |   EFS    |
         | (Shared  |            | (Shared  |
         | Storage) |            | Storage) |
         +----------+            +----------+
              |                        |
         +------------+            +-------------+
         | Secrets    |            | Secrets     |
         | Manager    |            | Manager     |
         +------------+            +-------------+
              |                        |
         +-------------+           +-------------+
         | Backup to S3 |           | Backup to S3 |
         +-------------+           +-------------+

```
