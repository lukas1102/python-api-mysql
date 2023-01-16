kubectl delete node k8s6
kubectl delete node k8s5 
kubectl delete node k8s4 
kubectl delete node k8s3 
kubectl delete node k8s2 
kubectl delete node k8s1
ssh kube@172.16.0.16 "sudo kubeadm reset -f" &
ssh kube@172.16.0.15 "sudo kubeadm reset -f" &
ssh kube@172.16.0.14 "sudo kubeadm reset -f" &
ssh kube@172.16.0.13 "sudo kubeadm reset -f" &
ssh kube@172.16.0.12 "sudo kubeadm reset -f" &
ssh kube@172.16.0.11 "sudo kubeadm reset -f" &