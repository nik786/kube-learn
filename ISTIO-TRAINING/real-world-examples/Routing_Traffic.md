

## Routing Traffic


- [frontend-original](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/real-world-examples/frontend-original.md)

   kubectl apply -f frontend-original.yaml.


- [frontend-dr](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/real-world-examples/frontend-dr.md)

  kubectl apply -f frontend-dr.yaml

- [frontend-vs](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/real-world-examples/frontend-vs.md)

  kubectl apply -f frontend-vs.yaml

  Now that we configured the VirtualService to route all incoming traffic to the original subset, we can safely create the new frontend deployment.


 - [frontend-v1](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/real-world-examples/frontend-v1.md)

   kubectl apply -f frontend-v1.yaml.

   If we open the INGRESS_HOST in the browser, we will still see the original version of the frontend.
   Let's update the weights in the VirtualService and start routing 30% of the traffic to the v1 subset.



- [frontend-30](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/real-world-examples/frontend-30.md)

  kubectl apply -f frontend-30.yaml.


If we refresh the web page a couple of times, we will notice an updated layout coming from the frontend v1 and looks like one in the figure below


















  
