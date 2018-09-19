$ minikube version    (Minikube Version)
  
$ minikube start  (Start Kubernetes Cluster)

$ kubectl version (Kubectl & Kubernetes version)

    The client version is the kubectl version;
    The server version is the Kubernetes version installed on the master.

$ kubectl cluster-info ( View kubernetes cluster info)

$ kubectl cluster-info dump ( View kubernetes cluster info with debug )

$ kubectl get nodes ( View nodes in the cluster )

& kubectl run kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1 --port=8080 ( Deploy an app)

$ kubectl get deployments (To get the list of deployments)

$ kubectl proxy ( creates a proxy )