

```
pv for efs

# EFS PersistentVolume (PV)
apiVersion: v1
kind: PersistentVolume
metadata:
  name: efs-pv
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  storageClassName: efs-sc
  csi:
    driver: efs.csi.aws.com
    volumeHandle: <EFS_FILE_SYSTEM_ID> # Replace with your EFS file system ID

---
# PersistentVolumeClaim (PVC)
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: efs-pvc
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: efs-sc
  resources:
    requests:
      storage: 5Gi

---
# Nginx Deployment using the PVC
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-efs
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-efs
  template:
    metadata:
      labels:
        app: nginx-efs
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        volumeMounts:
        - name: efs-volume
          mountPath: /usr/share/nginx/html
      volumes:
      - name: efs-volume
        persistentVolumeClaim:
          claimName: efs-pvc

```
