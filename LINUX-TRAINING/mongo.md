

Master Mongo
--------------

use admin
rs.initiate()


var cfg = rs.conf();cfg.members[0].host="mongo-0.mongo.default.svc.cluster.local:27017";rs.reconfig(cfg)


rs.isMaster()

rs.add("mongo-1.mongo.default.svc.cluster.local:27017")
rs.add("mongo-2.mongo.default.svc.cluster.local:27017")


use test_db

db.test.save(
{
   "desc": "My Test Database",
   "apps":  ["Test1", "Test2", "Test3", "Test4"],
})



Slave Mongo
------------

rs.slaveOk()
Show dbs


use test_db

db.test.save(
{
   "desc": "My Test Database",
   "apps":  ["Test1", "Test2", "Test3", "Test4"],
})


rs.slaveOk()
Show dbs


nslookup mongo-0.mongo.default.svc.cluster.local
nslookup mongo-1.mongo.default.svc.cluster.local
nslookup mongo-2.mongo.default.svc.cluster.local
nslookup mongo.default.svc.cluster.local
telnet mongo-0.mongo.default.svc.cluster.local 27017



Reference Links
https://developer.ibm.com/technologies/containers/tutorials/cl-deploy-mongodb-replica-set-using-ibm-cloud-container-service/
https://computingforgeeks.com/how-to-setup-mongodb-replication-on-ubuntu-18-04-lts/
https://sysadmins.co.za/setup-a-3-node-mongodb-replica-set-on-ubuntu/
https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#pods-in-a-statefulset
https://codelabs.developers.google.com/codelabs/cloud-mongodb-statefulset/index.html?index=..%2F..index#5
https://medium.com/google-cloud/sharded-mongodb-in-kubernetes-statefulsets-on-gke-ba08c7c0c0b0
https://github.com/cicciodifranco/kubernetes-mongo-shard-cluster/blob/master/mongo_sh_1.yaml


















