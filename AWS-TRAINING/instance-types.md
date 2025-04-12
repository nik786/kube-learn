


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
