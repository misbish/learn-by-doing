**Kubernetes Command Line**

     kubectl version     #Kubectl version # Kubectl Clinet & Kubernetes Server
     minikube version    #Minikube version
     

     minikube start                 #Start Kubernetes Cluster, See other options as args 
     minikube get-k8s-versions      #List Kubernetes version
     minikube start --kubernetes-version v1.7.3  # Start approprate version of kubernetes
     
     minikube stop                  #Stop the Cluster 
     minikube delete                #Delete the Cluster
     
     

$ kubectl version (Kubectl & Kubernetes version)

    The client version is the kubectl version;
    The server version is the Kubernetes version installed on the master.

$ kubectl cluster-info ( View kubernetes cluster info)

$ kubectl cluster-info dump ( View kubernetes cluster info with debug )

$ kubectl get nodes ( View nodes in the cluster )

& kubectl run kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1 --port=8080 ( Deploy an app)

$ kubectl get deployments (To get the list of deployments)

$ kubectl proxy ( creates a proxy )

$ kubectl get pods  (List the pods running in a deployment )

$ kubectl describe pods ( To view what containers and what images in the pod )

$ kubectl logs $POD_NAME (To view logs if pod has 1 container)

$ kubectl exec $POD_NAME env (To execute command in pod )

$ kubectl exec -ti $POD_NAME bash

$ exit ( to Exit)

$ kubectl get services #(by default serice called kubernetes runs when minikube starts)
              