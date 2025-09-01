

```

$ cat kafka-broker.yaml
---
apiVersion: v1
kind: ReplicationController
metadata:
  name: kafka-broker
spec:
  replicas: 1
  selector:
    app: kafka
  template:
    metadata:
      labels:
        app: kafka
    spec:
      containers:
      - name: kafka
        image: wurstmeister/kafka
        ports:
        - containerPort: 9092
        env:
        - name: KAFKA_ADVERTISED_PORT
          value: "9092"
        - name: KAFKA_ADVERTISED_HOST_NAME
          value: "kafka-service"
        - name: KAFKA_ZOOKEEPER_CONNECT
          value: zoo1:2181,zoo2:2181,zoo3:2181
        #- name: KAFKA_CREATE_TOPICS
        #  value: mytopic:2:1

---
apiVersion: v1
kind: Service
metadata:
  name: kafka-service
  labels:
    app: kafka
spec:
  ports:
  - port: 9092
    name: kafka-port
    targetPort: 9092
    protocol: TCP
  selector:
    app: kafka
  type: ClusterIP


Create Zookeeper broker using below given yaml.

$ cat zookeeper.yaml 
---
apiVersion: v1
kind: ReplicationController
metadata:
  name: zookeeper-controller-1
spec:
  replicas: 1
  selector:
    app: zookeeper-1
  template:
    metadata:
      labels:
        app: zookeeper-1
    spec:
      containers:
      - name: zoo1
        image: digitalwonderland/zookeeper
        ports:
        - containerPort: 2181
        env:
        - name: ZOOKEEPER_ID
          value: "1"
        - name: ZOOKEEPER_SERVER_1
          value: zoo1
        - name: ZOOKEEPER_SERVER_2
          value: zoo2
        - name: ZOOKEEPER_SERVER_3
          value: zoo3
---
apiVersion: v1
kind: ReplicationController
metadata:
  name: zookeeper-controller-2
spec:
  replicas: 1
  selector:
    app: zookeeper-2
  template:
    metadata:
      labels:
        app: zookeeper-2
    spec:
      containers:
      - name: zoo2
        image: digitalwonderland/zookeeper
        ports:
        - containerPort: 2181
        env:
        - name: ZOOKEEPER_ID
          value: "2"
        - name: ZOOKEEPER_SERVER_1
          value: zoo1
        - name: ZOOKEEPER_SERVER_2
          value: zoo2
        - name: ZOOKEEPER_SERVER_3
          value: zoo3
---
apiVersion: v1
kind: ReplicationController
metadata:
  name: zookeeper-controller-3
spec:
  replicas: 1
  selector:
    app: zookeeper-3
  template:
    metadata:
      labels:
        app: zookeeper-3
    spec:
      containers:
      - name: zoo3
        image: digitalwonderland/zookeeper
        ports:
        - containerPort: 2181
        env:
        - name: ZOOKEEPER_ID
          value: "3"
        - name: ZOOKEEPER_SERVER_1
          value: zoo1
        - name: ZOOKEEPER_SERVER_2
          value: zoo2
        - name: ZOOKEEPER_SERVER_3
          value: zoo3
---
apiVersion: v1
kind: Service
metadata:
  name: zoo1
  labels:
    app: zookeeper-1
spec:
  ports:
  - name: client
    port: 2181
    protocol: TCP
  - name: follower
    port: 2888
    protocol: TCP
  - name: leader
    port: 3888
    protocol: TCP
  selector:
    app: zookeeper-1
---
apiVersion: v1
kind: Service
metadata:
  name: zoo2
  labels:
    app: zookeeper-2
spec:
  ports:
  - name: client
    port: 2181
    protocol: TCP
  - name: follower
    port: 2888
    protocol: TCP
  - name: leader
    port: 3888
    protocol: TCP
  selector:
    app: zookeeper-2
---
apiVersion: v1
kind: Service
metadata:
  name: zoo3
  labels:
    app: zookeeper-3
spec:
  ports:
  - name: client
    port: 2181
    protocol: TCP
  - name: follower
    port: 2888
    protocol: TCP
  - name: leader
    port: 3888
    protocol: TCP
  selector:
    app: zookeeper-3


List down the topics in kafka
$ ./kafka-topics.sh --list --zookeeper zoo1:2181

Create topic called "demo"
$ ./kafka-topics.sh --create --zookeeper zoo1:2181 --replication-factor 1 --partitions 1 --topic demo

Produce message inside "demo" topic.
$ ./kafka-console-producer.sh --broker-list kafka-service:9092 --topic demo

Consume message from "demo" topic.
$ ./kafka-console-consumer.sh --bootstrap-server kafka-service:9092 --topic demo --from-beginning

```
