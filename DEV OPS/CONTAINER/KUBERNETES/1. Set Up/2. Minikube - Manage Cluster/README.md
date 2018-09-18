**Running Kubernetes Locally via Minikube**

Minikube supports the following drivers:

    virtualbox
    vmwarefusion
    kvm2 
    kvm 
    hyperkit 
    xhyve (driver installation) (deprecated)
    
    --vm-driver=xxx option in Minikube start can be used to select apprpriate VM .
    
    
Start Minikube 

    VM:
    $ minikube start
    
    Container (An open and reliable container runtime https://containerd.io):
    - To use containerd as the container runtime, run:
    
    $ minikube start \
        --network-plugin=cni \
        --container-runtime=containerd \
        --bootstrapper=kubeadm 
        
            Or you can use the extended version:
      
    $ minikube start \
        --network-plugin=cni \
        --extra-config=kubelet.container-runtime=remote \
        --extra-config=kubelet.container-runtime-endpoint=unix:///run/containerd/containerd.sock \
        --extra-config=kubelet.image-service-endpoint=unix:///run/containerd/containerd.sock \
        --bootstrapper=kubeadm
     
     CRI-O  (Open Container Initiative-based implementation of Kubernetes Container Runtime Interface):
     - To use CRI-O as the container runtime, run:
     
     $ minikube start \
         --network-plugin=cni \
         --container-runtime=cri-o \
         --bootstrapper=kubeadm
      
            Or you can use the extended version:
     
     $ minikube start \
         --network-plugin=cni \
         --extra-config=kubelet.container-runtime=remote \
         --extra-config=kubelet.container-runtime-endpoint=/var/run/crio.sock \
         --extra-config=kubelet.image-service-endpoint=/var/run/crio.sock \
         --bootstrapper=kubeadm
         
    rkt  (rkt is a pod-native container engine for Linux. )
    - To use rkt as the container runtime run:
    
    $ minikube start \
        --network-plugin=cni \
        --container-runtime=rkt  
        
    Reusing the Docker daemon
    - minikube comes with built in docker dameon
    
    - To be able to work with the docker daemon on your mac/linux host use the docker-env command in your shell:
          $ eval $(minikube docker-env)
    - You should now be able to use docker on the command line on your host mac/linux machine talking to the docker daemon inside the minikube VM:
          $ docker ps
          
**Managing your Cluster**

`Starting a Cluster`

    $ minikube start 
    
    - This command creates and configures a virtual machine that runs a single-node Kubernetes cluster.
    - This command also configures your kubectl installation to communicate with this cluster.

    NOTE: Minikube supports running multiple different versions of Kubernetes.
     
    
    $ minikube get-k8s-versions
    - You can access a list of all available versions via
    
    $ minikube start --kubernetes-version v1.7.3
    
    
       

`Stopping a Cluster`

    $ minikube stop
    
    - The minikube stop command can be used to stop your cluster. 
    - This command shuts down the minikube virtual machine, 
    - but preserves all cluster state and data. 
    - Starting the cluster again will restore it to it’s previous state.

`Deleting a Cluster`

    $ minikube delete
    
    - The minikube delete command can be used to delete your cluster. 
    - This command shuts down and deletes the minikube virtual machine. 
    - No data or state is preserved.


`Interacting with Your Cluster`

    1.  kubectl context (This is not a command)   

    - The minikube start command creates a “kubectl context” called “minikube”.
    - This context contains the configuration to communicate with your minikube cluster.
    - Minikube sets this context to default automatically, but if you need to switch back to it in the future, run:

    $ kubectl config use-context minikube,
       Or 
    $ kubectl get pods --context=minikube.


   
    2.  $ minikube dashboard
    
    - To access the Kubernetes Dashboard, run this command in a shell after starting minikube to get the address:

        
    3.  $ minikube service [-n NAMESPACE] [--url] NAME
  
    - To access a service exposed via a node port, run this command in a shell after starting minikube to get the address:



