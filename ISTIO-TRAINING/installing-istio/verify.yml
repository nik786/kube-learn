kubectl exec "$(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>

istioctl analyze

kubectl get svc istio-ingressgateway -n istio-system


use the istio-ingressgateway service as a NodePort


kubectl get svc istio-ingressgateway -n istio-system -o yaml > istio-svc.yml

kubectl delete -f istio-svc.yml

kubectl apply -f istio-svc.yml

kubectl get svc istio-ingressgateway -n istio-system


export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
echo $INGRESS_PORT

export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')
echo $SECURE_INGRESS_PORT

export INGRESS_HOST=$(kubectl get po -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].status.hostIP}')



for i in $(seq 1 100); do curl -s -o /dev/null "http://$GATEWAY_URL/productpage"; done
