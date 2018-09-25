**Running Kubernetes Locally via Minikube**

Minikube runs a single-node Kubernetes cluster inside a VM on your laptop 

**Minikube Features**

    Minikube supp
    Supports Kubernetes features such as:
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
                
                       