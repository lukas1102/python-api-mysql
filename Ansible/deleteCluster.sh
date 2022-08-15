kubectl delete node k8s-5 
kubectl delete node k8s-4 
kubectl delete node k8s-3 
kubectl delete node k8s-2 
kubectl delete node k8s-1
ssh kube@172.16.0.15 "sudo kubeadm reset -f" &
ssh kube@172.16.0.14 "sudo kubeadm reset -f" &
ssh kube@172.16.0.13 "sudo kubeadm reset -f" &
ssh kube@172.16.0.12 "sudo kubeadm reset -f" &
ssh kube@172.16.0.11 "sudo kubeadm reset -f" &