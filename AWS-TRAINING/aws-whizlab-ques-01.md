

# You are running to website on EC2 instances can deployed across multiple Availability Zones with an Multi-AZ RDS MySQL Extra Large DB Instance etc. Then site performs a high number of the small reads and the write per second and the relies on the eventual consistency model. After the comprehensive tests you discover to that there is read contention on RDS MySQL. Which is the best approaches to the meet these requirements?

Deploy Elastic Cache in each availability zone and Then Increase the RDS MySQL Instance size and the Implement provisioned IOPS.

## An startup is running to a pilot deployment of around 100 sensors to the measure street noise and The air quality is urban areas for the 3 months. It was noted that every month to around the 4GB of sensor data are generated. The company uses to a load balanced take auto scaled layer of the EC2 instances and a RDS database with a 500 GB standard storage. The pilot was success and now they want to the deploy take atleast 100K sensors.let which to need the supported by backend. You need to the stored data for at least 2 years to an analyze it. Which setup of  following would you be prefer?

The Replace the RDS instance with an 6 node Redshift cluster with take 96TB of storage



Let to Suppose you have an application where do you have to render images and also do some of general computing. which service will be best fit your need?
Used on Application Load Balancer.

How will change the instance give type for the instances, which are the running in your applications tier and Then using Auto Scaling. Where will you change it from areas?
Changed to Auto Scaling launch configuration areas

You have an content management system running on the Amazon EC2 instance that is the approaching 100% CPU of utilization. Which option will be reduce load on the Amazon EC2 instance?

What does the Connection of draining do?
It re-routes traffic from the instances which are to be updated (or) failed for health-check.


## You use the Amazon CloudWatch as your primary monitoring system for web application. After a recent to software deployment, your users are to getting Intermittent the 500 Internal Server to the Errors, when you using web application. You want to create the CloudWatch alarm, and notify the on-call engineer let when these occur. How can you accomplish the using the AWS services?

1. Create a CloudWatch  Log  group
2. Then create a metric filters which will capture 500 Internal Servers error.
3. Then Set a CloudWatch alarm on this metric .
4. Then Use sns  to notify on-call engineers when CloudWatch alarm is triggered.


## You are migrating to legacy client-server application for AWS. The application responds to a specific DNS visible domain (e.g. www.example.com) and server 2-tier architecture, with multiple application for the servers and the database server. Remote clients use to TCP to connect to the application of servers. The application servers need to know the IP address of clients in order to  the function of properly and are currently taking of that information from  TCP socket. A Multi-AZ RDS MySQL instance to will be used for database. During the migration you  change the application code but you have file a change request. How do would you implement the architecture on the AWS in order to maximize scalability and high availability?

File a change request to get implement of Proxy Protocol support in the application. Use of ELB with TCP Listener and A Proxy Protocol enabled to distribute the  load on two application servers in the different AZs.


## Your application currently is leverages AWS Auto Scaling to the grow and shrink as a load Increases/decreases and has been performing as well. Your marketing a team expects and steady ramp up in traffic to follow an upcoming campaign that will result in 20x growth in the traffic over 4 weeks. Your forecast for approximate number of the Amazon EC2 instances necessary to meet  peak demand is 175. What should be you do  avoid potential service disruptions during the ramp up traffic?

Check the service limits in the Trusted Advisors and adjust as necessary, so that forecasted count remains within  the limits.


## You are the designing an application that a contains protected health information. Security and Then compliance requirements for your application mandate that all protected to health information in application use to encryption at rest and in the transit module. The application to uses an three-tier architecture. where should data flows through the load balancers and is stored on the Amazon EBS volumes for the processing, and the results are stored in the Amazon S3 using a AWS SDK. Which of the options satisfy the security requirements?

Use TCP load balancing on load balancer system, 
SSL termination on Amazon to create EC2 instances, 
OS-level disk  encryption on Amazon EBS volumes,
The amazon S3 with server-side to encryption 
Use the SSL termination on load balancers, 
an SSL listener on the Amazon to create EC2 instances, 
Amazon EBS encryption on the EBS volumes containing the PHI, and Amazon S3 with a server-side of encryption.

# An AWS customer are deploying an web application that is the composed of a front-end running on the Amazon EC2 and confidential data that are stored on the Amazon S3. The customer security policy is that all accessing operations to this sensitive data must authenticated and authorized by centralized access to management system that is operated by separate security team. In addition, the web application team that be owns and administers the EC2 web front-end instances are prohibited from having the any ability to access data that circumvents this centralized access to management system. Which are configurations will support these requirements?

We need to use STS tokens to download of the approved data directly from a Amazon S3


## A Enterprise customer is starting on their migration to the cloud, their main reason for the migrating is agility and they want to the make their internal Microsoft active directory available to the many applications running on AWS, this is so internal users for only have to remember one set of the credentials and as a central point of user take control for the leavers and joiners. How could they make their actions the directory secures and the highly available with minimal on-premises on infrastructure changes in the most cost and the time-efficient way?

By Using a VPC, they could be create an the extension to their data center. 
 make use of resilient hardware IPSEC on tunnels
