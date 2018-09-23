**Kubernetes Basics**

https://kubernetes.io/docs/tutorials/kubernetes-basics/

Katacoda to run a virtual terminal in your web browser that runs Minikube,

Kubernetes is a production-ready, open source platform designed with Google's accumulated experience in container orchestration.
 
Kubernetes is a production-grade, open-source platform that orchestrates the placement (scheduling) and execution of application containers within and across computer clusters.

Covers below 
    
    Create a Cluster
    Deploy an App
    Explore Your App
    Explore Your App Publicly
    Scale Your App
    Update Your App
    
    
`Create a Cluster`

    A Kubernetes cluster consists of two types of resources:
       - Master -  Manages the cluster
       - Nodes -   workers that host & run applications


    - A node is a VM or a physical computer that serves as a worker machine in a Kubernetes cluster.
    - Each node has a Kubelet, which is an agent for managing the node and communicating with the Kubernetes master.
    - The node should also have tools for handling container operations, such as Docker or rkt.
    - A Kubernetes cluster that handles production traffic should have a minimum of three nodes.
    - Minikube has 1 node .
    
    Commands :
    
            $ minikube version
            $ minikube start
            $ kubectl version 
            $ kubectl cluster-info
            $ kubectl cluster-info dump 
            $ kubectl get nodes 
            

`Deploy an App`

    Make your Kubernetes cluster up 
    Ready with your containerized applications 
    
    Create a Kubernetes Deployment configuration. 
    The Deployment instructs Kubernetes how to create and update instances of your application.
    Once you've created a Deployment, the Kubernetes master schedules mentioned application instances onto individual Nodes in the cluster.
    Once the application instances are created, a Kubernetes Deployment Controller continuously monitors those instances. 
    If the Node hosting an instance goes down or is deleted, the Deployment controller replaces it.
    This provides a self-healing mechanism to address machine failure or maintenance.
    
    Command:
        kubectl run kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1 --port=8080
        kubectl get deployments
        kubectl proxy
        
`Explore Your App`

    Kubernetes Pods: 
    - A Pod is a group of one or more application containers (such as Docker or rkt) and includes shared storage (volumes), IP address and information about how to run them.
    - Pods are the atomic unit on the Kubernetes platform.
    - When we create a Deployment on Kubernetes, that Deployment creates Pods with containers inside them (as opposed to creating containers directly).
    - Each Pod is tied to the Node where it is scheduled, and remains there until termination (according to restart policy) or deletion.
    - In case of a Node failure, identical Pods are scheduled on other available Nodes in the cluster.
    

    Kubernetes Nodes:
    - A Pod always runs on a Node.
    - A Node is a worker machine in Kubernetes and may be either a virtual or a physical machine, depending on the cluster.
    - Each Node is managed by the Master. 
    - A Node can have multiple pods, and the Kubernetes master automatically handles scheduling the pods across the Nodes in the cluster.
    - Every Kubernetes Node runs at least:
         -  Kubelet, a process responsible for communication between the Kubernetes Master and the Node; it manages the Pods and the containers running on a machine.
         -  A container runtime (like Docker, rThe Master's automatic
   
   Command:
       kubectl get pods 
       kubectl describe pods 
       kubectl proxy
       export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
       echo Name of the Pod: $POD_NAME
       curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/
       kubectl logs $POD_NAME
       kubectl exec $POD_NAME env
       kubectl exec -ti $POD_NAME bash
       
       
`Expose your app publicly i.e. via service`

    A Kubernetes Service is an abstraction layer which defines a logical set of Pods and enables external traffic exposure, load balancing and service discovery for those Pods.
    