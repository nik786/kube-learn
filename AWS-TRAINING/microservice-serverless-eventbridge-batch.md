
MicroService
----------------


| **Aspect**                 | **Description**                                                                                                           |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Microservices Architecture** | A method of developing applications as a collection of small, loosely coupled, independently deployable services.         |
| **Scalability**             | Microservices allow independent scaling of individual services based on demand, leading to more efficient resource usage.   |
| **Technology Flexibility** | Different services can be built using different technologies and languages, offering flexibility in choosing the right tools.|
| **Resilience**              | Failures in one service do not affect the entire application, improving overall system reliability.                        |
| **Faster Development**      | Smaller, independent teams can work on different services, speeding up the development and release cycle.                   |

| **Pros**                    | **Cons**                                                                                                               |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------|
| **Scalability**              | Can scale each service independently to optimize resource usage and meet demand.                                      | **Complexity**: Managing and coordinating multiple services can increase system complexity.                      |
| **Resilience**               | Failure of one service does not impact the entire application, enhancing fault tolerance.                            | **Communication Overhead**: Multiple services communicating over networks can lead to higher latency and more complex data handling. |
| **Flexibility in Development** | Services can be developed, tested, and deployed independently, enabling faster development cycles.                     | **Data Management**: Ensuring data consistency across services can become complex, requiring specialized techniques like eventual consistency. |
| **Technology Agnostic**     | Different services can use different technologies best suited for their requirements.                                  | **Deployment and Operations Overhead**: Managing multiple deployments and services increases operational burden. |
| **Easier Maintenance**       | Smaller codebases for each service make it easier to maintain and update individual services.                         | **Increased Network Traffic**: Services need to communicate over the network, which can lead to increased traffic and potential bottlenecks. |




ServerLess Computing
---------------------

| **Feature**                               | **Description**                                                                                                                                                                  |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Serverless Computing**                  | A method of providing backend services on an as-used basis, where the vendor is charged based on computation. Users don't need to reserve or pay for fixed bandwidth or servers.  |
| **Auto-Scaling**                          | The service automatically scales based on usage, ensuring the right resources are allocated as needed without manual intervention.                                               |
| **Agility & Cost Efficiency**             | Enables the building of modern applications with increased agility and a lower total cost of ownership.                                                                         |
| **Developer Focus**                       | Developers can focus on core product development instead of managing servers or runtimes, whether in the cloud or on-premises.                                                   |
| **Reduced Overhead**                      | Reduced overhead allows developers to reclaim time and energy, which can be spent on creating scalable and reliable products instead of worrying about infrastructure management. |


| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **Step Functions**           | A fully managed serverless orchestration service provided by AWS that allows you to coordinate and automate workflows involving multiple AWS services. It's commonly used for building and orchestrating complex workflows such as data processing pipelines, microservices coordination, and multi-step serverless applications. It simplifies the development and maintenance of workflows by providing a highly scalable and reliable orchestration service. |
| **State Machines and States**| Step Functions uses state machines as its core concept. A state machine is a collection of states connected by transitions. States represent individual tasks or steps in your workflow, such as AWS Lambda functions, AWS Batch jobs, Amazon ECS tasks, or AWS Glue ETL jobs. |
| **Logging and Monitoring**   | AWS Step Functions provides detailed logging and monitoring capabilities, including CloudWatch Logs and CloudWatch Metrics, to help troubleshoot and monitor the execution of workflows. |
| **Cost-Effective**           | AWS Step Functions charges based on the number of state transitions, making it cost-effective for various workloads. |
| **Built-In State Types**     | AWS Step Functions offers several built-in state types, including: <br> **Task State**: Represents an individual task like AWS Lambda functions or Amazon ECS tasks. <br> **Choice State**: Adds conditional logic based on the outcome of previous states. <br> **Parallel State**: Executes multiple states in parallel. <br> **Wait State**: Adds delays to the workflow. <br> **Fail State**: Marks the workflow as failed. <br> **Succeed State**: Marks the workflow as successful. |
| **Visual Workflow Designer**| Provides a visual interface for designing and defining workflows using the AWS Management Console or AWS CloudFormation templates. States and transitions are defined using JSON or YAML. |



| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **EventBridge**              | Amazon EventBridge is a serverless event bus service provided by AWS that simplifies event-driven application development. It allows you to connect various AWS services, integrated SaaS applications, and custom applications using events. |
| **Event Bus**                | EventBridge uses the concept of an event bus to route and manage events. There are two types: default event buses (created for you) and custom event buses (created for specific use cases). |
| **Events**                   | Messages that represent changes or occurrences within your applications, services, or infrastructure. They can be generated by AWS services, custom applications, or third-party services integrated with EventBridge. |
| **Event Sources**            | Services or entities that produce events. AWS services like AWS Lambda, Amazon S3, and Amazon CloudWatch can be event sources. You can also create custom event sources by publishing events to EventBridge using the API. |
| **Event Rules**              | Define what to do when specific events are received by the event bus. Event rules can filter events based on attributes, pattern matching, and other conditions. |
| **Targets**                  | AWS services or custom applications that receive events when they match an event rule. Supported targets include AWS Lambda functions, Amazon SNS topics, Amazon SQS queues, Kinesis Data Streams, Step Functions, and more. Custom applications can also be targeted via HTTP endpoints. |
| **Schema Registry**          | Includes a schema registry that allows defining the structure of events using JSON Schema. Schemas help ensure data consistency and make it easier to understand the format of events. |

EventBridge
------------

Amazon EventBridge is a serverless event bus that enables event-driven communication between AWS services, SaaS applications, and custom applications.



| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **Event Bus**                | EventBridge uses the concept of an event bus to route and manage events. There are two types: default event buses (created for you) and custom event buses (created for specific use cases). |
| **Events**                   | Messages that represent changes or occurrences within your applications, services, or infrastructure. They can be generated by AWS services, custom applications, or third-party services integrated with EventBridge. |
| **Event Sources**            | Services or entities that produce events. AWS services like AWS Lambda, Amazon S3, and Amazon CloudWatch can be event sources. You can also create custom event sources by publishing events to EventBridge using the API. |
| **Event Rules**              | Define what to do when specific events are received by the event bus. Event rules can filter events based on attributes, pattern matching, and other conditions. |
| **Targets**                  | AWS services or custom applications that receive events when they match an event rule. Supported targets include AWS Lambda functions, Amazon SNS topics, Amazon SQS queues, Kinesis Data Streams, Step Functions, and more. Custom applications can also be targeted via HTTP endpoints. |
| **Schema Registry**          | Includes a schema registry that allows defining the structure of events using JSON Schema. Schemas help ensure data consistency and make it easier to understand the format of events. |



AWS Batch Service:
-------------------

| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **AWS Batch**                | A fully managed service designed for batch processing and job scheduling, simplifying the process of launching, managing, and scaling batch computing jobs on AWS. |
| **Job Definitions**          | A blueprint for batch jobs specifying parameters such as the Docker image to use, resource requirements, and the command to execute. |
| **Job Queues**               | Used to prioritize and manage the execution of batch jobs. Jobs are submitted to specific queues, and AWS Batch handles scheduling and execution based on priorities and resource availability. |
| **Compute Environments**     | Define the type of compute resources available for executing jobs. AWS Batch can manage both Amazon EC2 instances and AWS Fargate tasks as compute environments. |


Workflow of AWS Batch:
-------------------------


| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **Job Submission**           | Users or applications submit batch jobs to AWS Batch.                         |
| **Job Queue**                | AWS Batch manages job queues, ensuring that jobs are processed in an orderly fashion based on priority and other factors. |
| **Scheduling**               | AWS Batch schedules jobs based on factors such as job priority, job dependencies, and resource availability. |
| **Compute Environment**      | AWS Batch provisions and manages the underlying compute resources needed for executing jobs, ensuring that the required resources are available. |


Use Cases for AWS Batch:
-------------------------

| **Use Case**                | **Description**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Data Processing**          | AWS Batch is often used for data processing tasks, such as ETL (Extract, Transform, Load) jobs, data validation, and data analytics. |
| **Scientific Computing**     | Suitable for running scientific simulations, computational chemistry, genomics, and other compute-intensive tasks. |
| **Image and Video Processing** | Can be used for image and video processing, transcoding, and analysis.         |
| **Job Orchestration**        | AWS Batch can be used to orchestrate complex workflows involving multiple job steps and dependencies. |
| **Rendering**                | Used in the media and entertainment industry for rendering animations, special effects, and high-quality images. |
| **Cost-effectiveness**       | AWS Batch simplifies the management of batch workloads by automating resource provisioning and job scheduling, making it cost-effective and scalable. |
