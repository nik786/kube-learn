
```

apiVersion: v1
kind: Pod
metadata:
  name: red
  namespace: default
spec:
  containers:
  - image: busybox:1.28
    name: red-container
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
    
  initContainers:
  - image: busybox
    name: red-init
    command: ["sleep", '20']

```

```
apiVersion: v1
kind: Pod
metadata:
  name: red
  namespace: default
spec:
  containers:
  - command:
    - sh
    - -c
    - echo The app is running! && sleep 3600
    image: busybox:1.28
    name: red-container
  initContainers:
  - command:
    - "sleep"
    - "20"
    image: busybox:1.28
    name: red-init

```
