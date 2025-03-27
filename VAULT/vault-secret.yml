


vault secrets enable -version=2 kv
vault kv put kv/secret password=extremely-secure-password

cat secret-store.yml
apiVersion: external-secrets.io/v1alpha1
 kind: SecretStore
 metadata:
   name: hashicorp-vault
   spec:
     provider:
       vault:
         server: "http://vault.vault:8200"
         path: "kv"
         version: "v2"
         auth:
           kubernetes:
             mountPath: "kubernetes"
             role: "eso-role"


cat external-secret.yml

apiVersion: external-secrets.io/v1alpha1
 kind: ExternalSecret
 metadata:
   name: vault-secret
 spec:
   secretStoreRef:
     name: hashicorp-vault
     kind: SecretStore
   target:
     name: vault-secret-example
   data:
   - secretKey: password
     remoteRef:
       key: secret
       property: password

cat deployment.yml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        volumeMounts:
        - name: secret-volume
          mountPath: /etc/secrets
          readOnly: true
      volumes:
      - name: secret-volume
        secret:
          secretName: vault-secret-example




