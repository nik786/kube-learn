What is Apache Kafka?
------------------------
Apache Kafka is a publish-subscribe open source message broker application. This messaging application was coded in “Scala”. 
Basically, this project was started by the Apache software. Kafka’s design pattern is mainly based on the transactional logs design.
It is a distributed, partitioned and replicated log service.


Explain the role of the offset.
---------------------------------
There is a sequential ID number given to the messages in the partitions what we call, an offset. So, to identify each message in the partition uniquely, we use these offsets.
What is the role of the ZooKeeper in Kafka?
Apache Kafka is a distributed system is built to use Zookeeper. Although, Zookeeper’s main role here is to build coordination between different nodes in a cluster. 
However, we also use Zookeeper to recover from previously committed offset if any node fails because it works as periodically commit offset.


What is the role of the ZooKeeper in Kafka?
-----------------------------------------------
Apache Kafka is a distributed system is built to use Zookeeper. Although, Zookeeper’s main role here is to build coordination between different nodes in a cluster. 
However, we also use Zookeeper to recover from previously committed offset if any node fails because it works as periodically commit offset.

What do you know about Partition in Kafka?
--------------------------------------------
In every Kafka broker, there are few partitions available. And, here each partition in Kafka can be either a leader or a replica of a topic.

Explain the concept of Leader and Follower
--------------------------------------------
In every partition of Kafka, there is one server which acts as the Leader, and none or more servers plays the role as a Followers.

What ensures load balancing of the server in Kafka?
------------------------------------------------------
As the main role of the Leader is to perform the task of all read and write requests for the partition, whereas Followers passively replicate the leader. 
Hence, at the time of Leader failing, one of the Followers takeover the role of the Leader. Basically, this entire process ensures load balancing of the servers

Why are Replications critical in Kafka?
-----------------------------------------
Because of Replication, we can be sure that published messages are not lost and can be consumed in the event of any machine error, program error or frequent software upgrades.

If a Replica stays out of the ISR for a long time, what does it signify?
-------------------------------------------------------------------------
Simply, it implies that the Follower cannot fetch data as fast as data accumulated by the Leader.

When does QueueFullException occur?
------------------------------------------
whenever the Kafka Producer attempts to send messages at a pace that the Broker cannot handle at that time QueueFullException typically occurs. 
However, to collaboratively handle the increased load, users will need to add enough brokers, since the Producer doesn’t block.


Is Apache Kafka is a distributed streaming platform? if yes, what you can do with it?
---------------------------------------------------------------------------------------
Undoubtedly, Kafka is a streaming platform. It can help:
To push records easily
Also, can store a lot of records without giving any storage problems
Moreover, it can process the records as they come in


What is the purpose of retention period in Kafka cluster?
-----------------------------------------------------------
However, retention period retains all the published records within the Kafka cluster. It doesn’t check whether they have been consumed or not. 
Moreover, the records can be discarded by using a configuration setting for the retention period. And, it results as it can free up some space

Explain the maximum size of a message that can be received by the Kafka?
--------------------------------------------------------------------------
The maximum size of a message that can be received by the Kafka is approx. 1000000 bytes.

What is Lag??
--------------
The difference is called Lag, and represents how far the Consumer Group application is behind the producers. 
Producer offsets are kept in the Kafka Broker in charge of that partition, which can tell you the last offset in the partition.
Total lag is the number of messages behind real time

What are the types of traditional method of message transfer?
---------------------------------------------------------------
Basically, there are two methods of the traditional message transfer method, such as:
Queuing: It is a method in which a pool of consumers may read a message from the server and each message goes to one of them.
Publish-Subscribe: Whereas in Publish-Subscribe, messages are broadcasted to all consumers.



What does ISR stand in Kafka environment?
-------------------------------------------
ISR refers to In sync replicas. 
These are generally classified as a set of message replicas which are synced to be leaders.

What do you mean by Stream Processing in Kafka?
------------------------------------------------
The type of processing of data continuously, real-time,  concurrently, and in a record-by-record fashion is what we call Kafka Stream processing.

What is Geo-Replication in Kafka?
----------------------------------
For our cluster, Kafka MirrorMaker offers geo-replication. Basically, messages are replicated across multiple data centers or cloud regions, with MirrorMaker. 
So, it can be used in active/passive scenarios for backup and recovery; or also to place data closer to our users, or support data locality requirements.

Explain Multi-tenancy?
-----------------------
We can easily deploy Kafka as a multi-tenant solution. However, by configuring which topics can produce or consume data, Multi-tenancy is enabled. Also, it provides operations support for quotas.



| **Component**      | **Description**                                                                                                                                         |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Producer**       | A client application that publishes messages to Kafka topics.                                                                                           |
| **Consumer**       | A client application that subscribes to Kafka topics and consumes messages published by producers.                                                      |
| **Broker**         | A Kafka server responsible for storing and managing the topics and partitions. Brokers handle the storage and replication of message data.              |
| **Topic**          | A category or feed name to which messages are published by producers and from which consumers consume messages. Topics are partitioned and distributed across brokers. |
| **Partition**      | A unit of data organization within a Kafka topic. Each topic is divided into one or more partitions, which allow for horizontal scaling and parallel processing of messages. |
| **Offset**         | A unique identifier assigned to each message within a partition. Offsets provide sequential ordering and allow consumers to track their progress in reading messages. |
| **Consumer Group** | A group of consumers that jointly consume messages from a topic. Each message is consumed by only one consumer within a group, enabling load balancing and fault tolerance. |
| **Replication**    | The process of copying data across multiple Kafka brokers to ensure fault tolerance and high availability. Replication helps prevent data loss and ensures reliability in case of broker failures. |





