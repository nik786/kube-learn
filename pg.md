| **ACID Property** | **Description**                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------|
| **Atomicity**      | Ensures that each transaction is all-or-nothing; either fully completed or fully rolled back.        |
| **Consistency**    | Guarantees that a transaction brings the database from one valid state to another.                   |
| **Isolation**      | Ensures that concurrent transactions do not interfere with each other, maintaining data integrity.    |
| **Durability**     | Ensures that once a transaction is committed, the data remains saved even in case of a system crash. |

mermaid ```

graph TD
    B[Internal ALB (Load Balancer)] --> D[Pgpool-II/HAProxy (Connection Pooling)]
    D --> C1[PostgreSQL ECS Task (AZ 1)]
    D --> C2[PostgreSQL ECS Task (AZ 2)]
    C1 --- E[EFS (Shared Storage)]
    C2 --- E
    C1 --> F[Secrets Manager]
    C2 --> F
    C1 --> G[Backup to S3]
    C2 --> G


```
