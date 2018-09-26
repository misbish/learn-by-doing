**Running Kubernetes Locally via Minikube**

Minikube runs a single-node Kubernetes cluster inside a VM on your laptop 

**Minikube Features**

    Minikube supports Kubernetes features such as:
        DNS
        NodePorts
        ConfigMaps and Secrets
        Dashboards
        Container Runtime: Docker, rkt, CRI-O and containerd
        Enabling CNI (Container Network Interface)
        Ingress
        
**Minikube Installation**

https://kubernetes.io/docs/tasks/tools/install-minikube/

     
    1)    VT-x or AMD-v virtualization must be enabled in your computer’s BIOS
        
    2)    Install a Hypervisor
            -  macOS: VirtualBox or VMware Fusion, or HyperKit.
            -  Linux: VirtualBox or KVM.
            -  Windows: VirtualBox or Hyper-V.
            
            Note: Minikube also supports a --vm-driver=none option that runs the Kubernetes components on the host and not in a VM. 
            Using this driver requires Docker, but not a hypervisor.
            
            --vm-driver=xxx option in Minikube start can be used to select apprpriate VM 
        
    3)    Install kubectl (Kubernetes command-line tool)
            - https://kubernetes.io/docs/tasks/tools/install-kubectl/
            
            WINDOWS:
            - curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.11.0/bin/windows/amd64/kubectl.exe
            - Add the binary in to your PATH
            
            LINUX : 
            - curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.11.0/bin/linux/amd64/kubectl
            - chmod +x ./kubectl (Make the kubectl binary executable)
            - sudo mv ./kubectl /usr/local/bin/kubectl (Move the binary in to your PATH)
        
            MAC OS:
            - curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.11.0/bin/darwin/amd64/kubectl
            - chmod +x ./kubectl (Make the kubectl binary executable)
            - sudo mv ./kubectl /usr/local/bin/kubectl (Move the binary in to your PATH)
                    
            
            - To find out the latest stable version 
                    https://storage.googleapis.com/kubernetes-release/release/stable.txt.
            - Other Options are available , Refer mentioned Link
            
            **NOTE**:   You must use a kubectl version that is within one minor version difference of your cluster. 
            For example, a v1.2 client should work with v1.1, v1.2, and v1.3 master.
             
    4) Verify kubectl
            - kubectl version 
            
    5) Install Minikube 
            - https://github.com/kubernetes/minikube/releases
            
            OSX
            - curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.28.2/minikube-darwin-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
               or
            - you can install via homebrew with brew cask install minikube.
            
            Linux
            - curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.28.2/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
               or
            - Download the Debian Package minikube_0.28-2.deb file, and install it using sudo dpkg -i minikube_.deb
            
            Windows
            - Download the minikube-windows-amd64.exe file, rename it to minikube.exe and add it to your path.
               or  
            - Download the minikube-installer.exe file, and execute the installer. This will automatically add minikube.exe to your path with an uninstaller available as well.
            
    6) Verify Minikube
            - minikube version
                
**Start Minikube**

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
