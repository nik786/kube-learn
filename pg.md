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


```

@startuml
' Simple icons without AWS resource icons

' Resources
actor "Internal ALB" as ALB
rectangle "Pgpool-II/HAProxy\n(Connection Pool)" as Pgpool
rectangle "PostgreSQL ECS 1\n(AZ 1)" as PG1
rectangle "PostgreSQL ECS 2\n(AZ 2)" as PG2
rectangle "Shared Storage (EFS 1)" as EFS1
rectangle "Shared Storage (EFS 2)" as EFS2
rectangle "Secrets Manager 1" as SM1
rectangle "Secrets Manager 2" as SM2
rectangle "Backup to S3 1" as S3_1
rectangle "Backup to S3 2" as S3_2

' Connections between resources
ALB -down-> Pgpool
Pgpool -down-> PG1
Pgpool -down-> PG2
PG1 -down-> EFS1
PG2 -down-> EFS2
EFS1 -down-> SM1
EFS2 -down-> SM2
SM1 -down-> S3_1
SM2 -down-> S3_2

@enduml
```

