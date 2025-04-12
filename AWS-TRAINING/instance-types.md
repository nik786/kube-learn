


Instance Types as per capacity
--------------------------------


| Instance Type | Processor Type        | Use Case                        | Memory    | Network Performance               | Storage Option        | Cost (Approx)        | Special Features                                                  |
|---------------|-----------------------|---------------------------------|-----------|-----------------------------------|-----------------------|----------------------|-------------------------------------------------------------------|
| **T2**        | Intel Xeon (Burstable) | Low to moderate performance     | 2-8 GB    | Low to moderate                  | EBS-Optimized         | Low (cost-effective)  | Burstable performance, cost-effective for low traffic applications |
| **M4**        | Intel Xeon (E5-2676 v3) | General-purpose workloads       | 16-64 GB  | High                              | EBS-Optimized         | Moderate             | High baseline performance, ideal for balanced workloads           |
| **M3**        | Intel Xeon E5-2670 v2  | Balanced performance            | 7.5-30.5 GB| Moderate                         | EBS-Optimized         | Moderate             | Good for multi-purpose workloads, stable performance              |
| **C3**        | Intel Xeon E5-2670 v2  | Compute-intensive workloads     | 7.5-30.5 GB| High                              | EBS-Optimized         | Moderate             | Optimized for CPU-intensive tasks, good for batch processing      |
| **C4**        | Intel Xeon E5-2666 v3  | High-performance compute        | 16-60 GB  | Very high                        | EBS-Optimized         | High                 | Superior network performance, ideal for compute-heavy applications|
| **G2**        | Intel Xeon E5-2670 v2  | Graphics workloads, GPU-based   | 15-60 GB  | High                              | EBS-Optimized         | High                 | GPU-based instance, suitable for rendering and machine learning  |
| **R3**        | Intel Xeon E5-2670 v2  | Memory-intensive workloads      | 30.5-244 GB| Moderate                         | EBS-Optimized         | High                 | High memory capacity, suitable for in-memory databases            |
| **I2**        | Intel Xeon E5-2670 v2  | High I/O performance workloads  | 30.5-488 GB| High                              | SSD-based storage     | High                 | SSD-backed storage for I/O-intensive workloads, low latency       |
| **D2**        | Intel Xeon E5-2670 v2  | Data warehousing and big data   | 64-768 GB | High                              | HDD-based storage     | High                 | Large storage capacity, cost-effective for big data workloads    |


Instance Types as per price
-------------------------------



| **Instance Type**  | **Description**                                                                                  | **Pricing Model**                                       | **Use Case**                                                                                       | **Commitment/Duration**                             |
|--------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **On-Demand**      | Instances that are available immediately without requiring long-term commitment.                 | Pay as you go, based on hourly usage.                  | Best for short-term or unpredictable workloads where flexibility is needed.                        | No commitment, pay only for what you use.            |
| **Spot**           | Instances available at a discount, but can be terminated by AWS with little notice.              | Pay for unused capacity, much lower than On-Demand.     | Best for flexible, fault-tolerant workloads like batch processing, big data, and background tasks. | No commitment, but may be interrupted with short notice. |
| **Reserved**       | Instances that require a commitment for 1 or 3 years in exchange for a discount.                 | Pay upfront or with partial upfront options.            | Best for steady-state applications with predictable usage like databases or long-term workloads.    | 1 or 3 years commitment, lower cost over time.        |
| **Dedicated**      | Instances that run on hardware dedicated to a single customer.                                  | Typically higher than On-Demand prices.                 | Best for compliance requirements or workloads that need isolation from other tenants.              | No commitment required, but generally more expensive. |
   





Production Preferrable Instances
--------------------------------


| **Instance Type**  | **vCPUs** | **Memory (GiB)** | **Processor**                           | **Network Bandwidth** | **On-Demand Pricing (per hour)** | **Spot Pricing (approx per hour)** |
|--------------------|----------|------------------|------------------------------------------|-----------------------|----------------------------------|-------------------------------------|
| **c6gn.4xlarge**  | 16       | 32               | AWS Graviton2 (ARM-based)               | Up to 25 Gbps         | $0.499                          | $0.150                              |
| **c6i.4xlarge**   | 16       | 32               | Intel Xeon Platinum 8375C (Ice Lake)    | Up to 12.5 Gbps       | $0.680                          | $0.204                              |
| **m6i.4xlarge**   | 16       | 64               | Intel Xeon Platinum 8375C (Ice Lake)    | Up to 12.5 Gbps       | $0.768                          | $0.230                              |
| **r6i.4xlarge**   | 16       | 128              | Intel Xeon Platinum 8375C (Ice Lake)    | Up to 12.5 Gbps       | $1.008                          | $0.302                              |
| **c5n.4xlarge**   | 16       | 42               | Intel Xeon Platinum 8259CL (Cascade Lake) | Up to 25 Gbps         | $0.904                          | $0.270                              |
| **m5n.4xlarge**   | 16       | 64               | Intel Xeon Platinum 8259CL (Cascade Lake) | Up to 25 Gbps         | $1.040                          | $0.310                              |
| **r5n.4xlarge**   | 16       | 128              | Intel Xeon Platinum 8259CL (Cascade Lake) | Up to 25 Gbps         | $1.344                          | $0.400                              |
| **g5.2xlarge**    | 8        | 32               | NVIDIA A10G Tensor Core GPU (GPU-Optimized) | Up to 25 Gbps    | $1.006                          | $0.300                              |
| **p4d.24xlarge**  | 96       | 1152             | NVIDIA A100 Tensor Core GPU (AI/ML)     | 400 Gbps              | $32.77                          | $9.830                              |
| **inf1.6xlarge**  | 24       | 96               | AWS Inferentia (Optimized for AI/ML Inference) | 100 Gbps      | $2.226                          | $0.670                              |



Why These Choices?
--------------------


Spring Boot is CPU and memory-intensive, so compute-optimized (C-series) or memory-optimized (R-series) instances are preferable.

Graviton3-based instances offer better price-performance for most workloads unless specific x86 dependencies exist.
Higher network bandwidth ensures lower latency and faster request processing, especially for microservices communicating frequently.

Auto-scaling and cost efficiency: Graviton instances provide up to 40% better price-performance than x86.

java spring boot
-----------------

| **Instance Type** | **vCPUs** | **Memory (GiB)** | **Processor** | **Network Bandwidth** | **On-Demand Pricing (per hour)** | **Spot Pricing (approx per hour)** |
|-------------------|-----------|------------------|---------------|-----------------------|----------------------------------|------------------------------------|
| **c7g.4xlarge**   | 16        | 32               | AWS Graviton3 | Up to 30 Gbps         | $0.536                           | $0.161                             |
| **c6i.4xlarge**   | 16        | 32               | Intel Xeon    | Up to 12.5 Gbps       | $0.680                           | $0.204                             |
| **r7g.4xlarge**   | 16        | 64               | AWS Graviton3 | Up to 30 Gbps         | $0.691                           | $0.207                             |
| **r6i.4xlarge**   | 16        | 128              | Intel Xeon    | Up to 12.5 Gbps       | $1.008                           | $0.302                             |
| **m7g.4xlarge**   | 16        | 64               | AWS Graviton3 | Up to 30 Gbps         | $0.625                           | $0.188                             |
| **m6i.4xlarge**   | 16        | 64               | Intel Xeon    | Up to 12.5 Gbps       | $0.768                           | $0.230      
