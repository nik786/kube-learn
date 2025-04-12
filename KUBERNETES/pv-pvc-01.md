

```

# Create a Persistent Volume with the given specification
------------------------------------------------------------

Volume Name: pv-log

Storage: 100Mi

Access Modes: ReadWriteMany

Host Path: /pv/log

Reclaim Policy: Retain


apiVersion: v1
kind: PersistentVolume
metadata:  
  name: pv-log
spec:
  capacity:
    storage: 100Mi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain  
  hostPath:
    path: /pv/log


Let us claim some of that storage for our application.
Create a Persistent Volume Claim with the given specification.

Persistent Volume Claim: claim-log-1

Storage Request: 50Mi

Access Modes: ReadWriteOnce


apiVersion: v1
kind: PersistentVolumeClaim
metadata:  
  name: claim-log-1
spec:
  
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 50Mi


Update the webapp pod to use the persistent volume claim as its storage.


Replace hostPath configured earlier with the newly created PersistentVolumeClaim



apiVersion: v1
kind: Pod
metadata:
  name: webapp
  namespace: default
spec:
  containers:
  - env:
    - name: LOG_HANDLERS
      value: file
    image: kodekloud/event-simulator
    imagePullPolicy: Always
    name: event-simulator
    volumeMounts:
    - mountPath: /log
      name: log
  volumes:
  - name: log
    hostPath: 
      path: /var/log/webapp
      type: Directory   


     volumeMounts:
    - mountPath: /log
      name: log

 volumes:
  - name: log
    persistentVolumeClaim:
      claimName: claim-log-1




```
