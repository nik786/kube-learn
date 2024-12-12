
1. You own multiple RDS instances .  How would  you manage the below tasks . (Use programming language of your choice to create a tool )
2. You would like to test connectivity and make sure all RDS are healthy and running as expected. (Assuming there are no 3rd party tools/monitoring framework)
3. You want to automatically run some set of sql commands on one or pool of RDS instances
4. You want to update some tables on set of RDS instances.


To manage the tasks you've outlined for multiple RDS instances, you can create a tool using Python, leveraging the boto3 AWS SDK for connectivity 
and instance management, and the psycopg2 or PyMySQL libraries for interacting with PostgreSQL or MySQL-based RDS instances.

1. Test Connectivity and Check RDS Health:
We will use the boto3 library to list all RDS instances and check their status (e.g., available status).
We can use psycopg2 or PyMySQL to test connectivity by connecting to the RDS instances and running a simple query (e.g., SELECT 1).

2. Automatically Run SQL Commands:
After establishing a connection to the RDS instance, we can execute a set of predefined SQL commands on one or more instances.

3. Update Tables on Set of RDS Instances:
The tool can take a list of SQL update commands and run them on selected RDS instances.


Python Tool Implementation:


```
import boto3
import psycopg2  # For PostgreSQL; use pymysql for MySQL
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import time

# AWS RDS client
rds_client = boto3.client('rds', region_name='us-east-1')  # Update with your region

# List RDS instances
def list_rds_instances():
    try:
        instances = rds_client.describe_db_instances()
        instance_ids = [db_instance['DBInstanceIdentifier'] for db_instance in instances['DBInstances']]
        return instance_ids
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Error fetching RDS instances: {e}")
        return []

# Check RDS Instance Health and Connectivity
def check_rds_health(instance_id):
    try:
        instance_info = rds_client.describe_db_instances(DBInstanceIdentifier=instance_id)
        status = instance_info['DBInstances'][0]['DBInstanceStatus']
        
        # Assuming RDS has public accessibility, you can connect to it
        endpoint = instance_info['DBInstances'][0]['Endpoint']['Address']
        port = instance_info['DBInstances'][0]['Endpoint']['Port']
        
        # Connect to the database (PostgreSQL example)
        conn = psycopg2.connect(
            host=endpoint,
            port=port,
            dbname='your_db_name',   # Update with actual DB name
            user='your_username',     # Update with actual DB user
            password='your_password'  # Update with actual DB password
        )
        cursor = conn.cursor()
        
        # Test query
        cursor.execute("SELECT 1;")
        cursor.close()
        conn.close()
        
        return status == 'available'
    
    except Exception as e:
        print(f"Error connecting to {instance_id}: {e}")
        return False

# Run SQL Commands on RDS Instance
def run_sql_commands(instance_id, sql_commands):
    try:
        instance_info = rds_client.describe_db_instances(DBInstanceIdentifier=instance_id)
        endpoint = instance_info['DBInstances'][0]['Endpoint']['Address']
        port = instance_info['DBInstances'][0]['Endpoint']['Port']
        
        # Connect to the database (PostgreSQL example)
        conn = psycopg2.connect(
            host=endpoint,
            port=port,
            dbname='your_db_name',   # Update with actual DB name
            user='your_username',     # Update with actual DB user
            password='your_password'  # Update with actual DB password
        )
        cursor = conn.cursor()
        
        for sql in sql_commands:
            cursor.execute(sql)
            conn.commit()  # Commit each SQL command
        
        cursor.close()
        conn.close()
        print(f"Executed SQL commands on {instance_id}")
        
    except Exception as e:
        print(f"Error executing SQL commands on {instance_id}: {e}")

# Update Tables on Set of RDS Instances
def update_tables_on_rds_instances(instance_ids, sql_update_commands):
    for instance_id in instance_ids:
        print(f"Running updates on {instance_id}...")
        run_sql_commands(instance_id, sql_update_commands)

# Main Execution
def main():
    instance_ids = list_rds_instances()
    if not instance_ids:
        print("No RDS instances found.")
        return
    
    print("Checking RDS health and connectivity...")
    for instance_id in instance_ids:
        if check_rds_health(instance_id):
            print(f"{instance_id} is healthy and reachable.")
        else:
            print(f"{instance_id} is not reachable or in unhealthy state.")
    
    # Example SQL commands
    sql_commands = [
        "SELECT NOW();",    # Just a simple test query
        "SELECT * FROM users;"  # Example of another query
    ]
    
    # Run SQL commands on all instances
    update_tables_on_rds_instances(instance_ids, sql_commands)
    
    # Example of updating tables with custom SQL
    sql_update_commands = [
        "UPDATE users SET active = 1 WHERE last_login > NOW() - INTERVAL '30 days';",
        "INSERT INTO audit_log (message) VALUES ('Batch update completed');"
    ]
    
    # Update tables on all instances
    update_tables_on_rds_instances(instance_ids, sql_update_commands)

if __name__ == '__main__':
    main()


```

Explanation:
---------------
List RDS Instances:

list_rds_instances() fetches all RDS instance identifiers from your AWS account.

Check RDS Health and Connectivity:
------------------------------------

check_rds_health() checks the RDS instance status (e.g., available) and attempts to establish a database connection using psycopg2. If the connection is successful, it means the RDS instance is healthy.

Run SQL Commands:
----------------------

run_sql_commands() takes an instance ID and a list of SQL commands and executes each command on the RDS instance.
Update Tables on Multiple RDS Instances:

update_tables_on_rds_instances() runs a set of update commands across a list of RDS instances.
Example Workflow:

First, the tool checks the connectivity and health of each RDS instance.
Then, it runs some example SQL commands and updates tables on the RDS instances.
Notes:
You will need to install the required libraries (boto3, psycopg2) by running pip install boto3 psycopg2.
Replace your_db_name, your_username, and your_password with your actual RDS database credentials.
This script can be extended to handle specific use cases, error handling, and log outputs.
Ensure your AWS credentials are properly set (e.g., via environment variables or AWS credentials file).
This approach provides a scalable and automated way to manage multiple RDS instances, ensuring their health, running SQL queries, and performing updates efficiently.
