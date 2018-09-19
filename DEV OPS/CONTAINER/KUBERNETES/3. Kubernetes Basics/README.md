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