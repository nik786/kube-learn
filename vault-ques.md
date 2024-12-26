## Rotate the password
--------------------
```
#!/bin/bash

# Generate a new password
NEW_PASSWORD=$(openssl rand -base64 16)

# Update the password in Vault
vault kv put secret/ag-app/ag-dev/rds username="rds-user" password="$NEW_PASSWORD"

```


## Versioning
-----------
```
vault kv enable-versioning secret

vault kv put secret/ag-app/ag-dev/rds username="user1" password="user123"

vault kv put secret/ag-app/ag-dev/rds username="user1" password="user321"

```


Backend Engine
------------------
```
cat config.hcl 
storage "dynamodb" {
  table      = "vault-storage"  # Name of the DynamoDB table
  region     = "ap-south-1"     # AWS region
  access = ""  # Optional, use if not relying on instance profile
  secret = ""  # Optional, use if not relying on instance profile
}

listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_disable = 1                # Disable TLS for testing, enable it in production
}


ui = true  # Enable the Vault UI

```


Other options
---------------
external secrets operator - worked
i have fetched secret manager value in to k8s deployment by help of external secret operator

hardcoded vault api worked


injector
pending
vault s3 csi driver
secret store 



vault server http://10.233.43.216:8200 -config=config.hcl

export VAULT_ADDR="http://10.233.43.216:8200"
vault server -config=config.hcl





env:
      - name: VAULT_ADDR
        value: "http://$EXTERNAL_VAULT_ADDR:8200"
      - name: VAULT_TOKEN
        value: root



## External Secret Operator
----------------------------


- [External-Secret-01](https://eminalemdar.medium.com/external-secrets-operator-integration-with-hashicorp-vault-aff3f956237b)


External Secrets Operator is an Open Source Kubernetes Operator that 
integrates external Secret Management Systems like AWS Secrets Manager, 
HashiCorp Vault, Google Secrets Manager, etc. and it is designed to 
synchronize secrets from external APIs to Kubernetes



```

vault policy write eso -<<EOF
path "*"
{  capabilities = ["read"]
}
EOF


cat <<EOF > /home/vault/secret.hcl
path "secret/login/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

vault policy write read-policy /home/vault/secret.hcl


vault auth enable kubernetes
vault secrets enable -path=secret kv

```


```
kubernetes_host="$(kubectl exec vault-0 -n vault — printenv | grep KUBERNETES_PORT_443_TCP_ADDR | cut -f 2- -d "=" | tr -d " ")"

kubernetes_port="443"

kubernetes_cert="$(kubectl config view — raw — minify — flatten -o jsonpath='{.clusters[].cluster.certificate-authority-data}' | base64 — decode)"

```


```
account_token="$(kubectl get secret -n vault vault-token-5lwdt -o jsonpath='{.data.token} {"\n"}' | base64 — decode)"
```


```
vault write auth/kubernetes/config token_reviewer_jwt="${account_token}" kubernetes_host="https://${kubernetes_host}:${kubernetes_port}" kubernetes_ca_cert="${kubernetes_cert}" disable_issuer_verification=true

vault write auth/kubernetes/config \
    token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
    kubernetes_host="https://$KUBERNETES_PORT_443_TCP_ADDR:443" \
    kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt 

vault write auth/kubernetes/role/vault-role \
   bound_service_account_names=vault-serviceaccount \
   bound_service_account_namespaces=default \
   policies=read-policy \
   ttl=1h

```





```
demo_token="$(kubectl get secret -n external-secrets external-secrets-token-wz2fp -o jsonpath='{.data.token} {"\n"}' | base64 — decode)"
vault write auth/kubernetes/role/eso-role bound_service_account_names=external-secrets bound_service_account_namespaces=external-secrets policies=eso ttl=24h
vault write auth/kubernetes/login role=eso-role jwt=$demo_token iss=https://kubernetes.default.svc.cluster.local

```

```

vault secrets enable -version=2 kv
vault kv put kv/secret password=extremely-secure-password
aws secretsmanager create-secret --name hello-service/password --secret-string "1234"
vault kv put secret/login pattoken=ytbuytbytbf765rb65u56rv
kubectl create secret aws-credentials --from-literal=ACCESS= --from-literal=SECRET=
kubectl create secret generic aws-credentials --from-literal=ACCESS= --from-literal=SECRET=

```



```
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


```
```
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


```

```

hello-service-external-secret.yml


apiVersion: 'kubernetes-client.io/v1'
kind: ExternalSecret
metadata:
  name: hello-service
spec:
  backendType: secretsManager
  data:
    - key: hello-service/password
      name: password

      
kubectl apply -f hello-service-external-secret.yml

```


## Reference


- [Blog-02](https://eminalemdar.medium.com/external-secrets-operator-integration-with-hashicorp-vault-aff3f956237b)
- [Blog-03](https://artifacthub.io/packages/helm/external-secrets/kubernetes-external-secrets)
  








