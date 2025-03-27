


## Installation

```
cd /root/t/he/chart/vault/vault
It requires to deploy sc.yml and pv.yml before deploy values.yml


helm install vault hashicorp/vault -f values.yaml

dynamic pvc will be created and attached to existing pv.


helm uninstall vault
kubectl delete -f pv4
kubectl create -f pv4

helm install vault hashicorp/vault --values values.yaml


kubcetl get po 

kubectl exec vault-0 -- vault operator init

Helm commands

helm status vault
helm get manifest vault
helm uninstall vault
helm ls

helm install vault hashicorp/vault   --set "server.dev.enabled=true"   --set "ui.enabled=true"
helm install vault hashicorp/vault --set='server.dev.enabled=true' -f values.yaml

```

## Configuration

```
k exec -it vault-0 /bin/sh

export VAULT_ADDR='http://127.0.0.1:8200'



kubectl exec vault-0 -- vault operator init \
    -key-shares=1 \
    -key-threshold=1 \
    -format=json > cluster-keys.json

vault operator init

vault operator unseal

vault login <root-token>




jq -r ".unseal_keys_b64[]" cluster-keys.json

VAULT_UNSEAL_KEY=$(jq -r ".unseal_keys_b64[]" cluster-keys.json)

kubectl exec vault-0 -- vault operator unseal $VAULT_UNSEAL_KEY

jq -r ".root_token" cluster-keys.json

kubectl exec --stdin=true --tty=true vault-0 -- /bin/sh

Login with the root token when prompted

vault login









```



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

vault secrets enable transit

vault write -f transit/keys/my-encryption-key

vault write transit/encrypt/my-encryption-key plaintext=$(base64 <<< "mysecret")

vault write transit/decrypt/my-encryption-key ciphertext=<your_ciphertext>

vault secrets enable -version=2 -path="demo-app" kv

vault kv put demo-app/user01 name=devopscube

vault kv get demo-app/user01 

vault kv put secret/login pattoken=ytbuytbytbf765rb65u56rv

vault kv put secret/ag-app/ag-dev/rds username="user1" password="user123"



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
vault write auth/kubernetes/role/devweb-app bound_service_account_names=internal-app bound_service_account_namespaces=vault policies=demoapp ttl=24h
vault kv put kv/dev/config  rds-username=rds-user rds-password=rds@123
vault kv get kv/dev/config
vault kv put kv/login pattoken=ytbuytbytbf765rb65u56rv



```

```

vault secrets enable -version=2 kv
vault kv put kv/secret password=extremely-secure-password
aws secretsmanager create-secret --name hello-service/password --secret-string "1234"
vault kv put secret/login pattoken=ytbuytbytbf765rb65u56rv
kubectl create secret aws-credentials --from-literal=ACCESS= --from-literal=SECRET=
kubectl create secret generic aws-credentials --from-literal=ACCESS= --from-literal=SECRET=
vault kv put secret/webapp/config username="static-user" password="static-password"
vault kv put secret/ssh alexis=password
vault kv get secret/ssh
vault secrets list
vault secrets enable -path=secret kv-v2
vault kv put secret/devwebapp/config username='giraffe' password='salsa'
vault kv get secret/devwebapp/config






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


- [Blog-01](https://eminalemdar.medium.com/external-secrets-operator-integration-with-hashicorp-vault-aff3f956237b)
- [Blog-02](https://artifacthub.io/packages/helm/external-secrets/kubernetes-external-secrets)
- [Blog-03](https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-deploy#initializing-the-vault)
     








