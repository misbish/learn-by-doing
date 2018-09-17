**KUBERNETES SET UP**

This involves installation and setting up a kubernetes Cluster

Important URL from Official Sites of Kubernetes
    
    https://kubernetes.io/docs/setup
    
    
Kubernetes can run on various platforms:

        1) in your laptop
        2) in VMs on a cloud provider
        3) In a rack of bare metal servers
        
Various Approach 

        1) Local-machine Solutions
        2) Hosted Solutions
        3) Turnkey Cloud Solutions
        4) Custom Solution 
        
Local Machine Solutions (For Learning )

    
    1) Minikube 
    
       -    Creating a local, single-node Kubernetes cluster for development and testing.
       -    Setup is completely automated and doesn’t require a cloud provider account.
    
    2) Kubeadm-dind 
    
       -    It is a multi-node (while minikube is single-node) Kubernetes cluster
       -    This only requires a docker daemon. 
       -    It uses docker-in-docker technique to spawn the Kubernetes cluster.
    
    3) Ubuntu on LXD 
    
       -    This supports a nine-instance deployment on localhost.
    
    4) IBM Cloud Private-CE (Community Edition) 
    
       -    It can use VirtualBox on your machine to deploy Kubernetes to one or more VMs for development and test scenarios.
       -    It Scales to full multi-node cluster.
    
    5) IBM Cloud Private-CE (Community Edition) on Linux Containers
     
       -    It is a Terraform/Packer/BASH based Infrastructure as Code (IaC) scripts to create a seven node (1 Boot, 1 Master, 1 Management, 1 Proxy and 3 Workers) LXD cluster on Linux Host.
    
    
    
Hosted Solutions (scale up to more machines and higher availability)

    1) Google Kubernetes Engine
     
      -     offers managed Kubernetes clusters.
    
    2) Amazon Elastic Container Service for Kubernetes 
      -     offers managed Kubernetes service.
    
    3) Azure Kubernetes Service 
      -     offers managed Kubernetes clusters.
    
    4) Stackpoint.io 
      -     provides Kubernetes infrastructure automation and management for multiple public clouds.
    
    5) AppsCode.com 
      -     provides managed Kubernetes clusters for various public clouds, including AWS and Google Cloud Platform.
    
    6) Madcore.Ai 
      -     is devops-focused CLI tool for deploying Kubernetes infrastructure in AWS. Master, auto-scaling group nodes with spot-instances, ingress-ssl-lego, Heapster, and Grafana.
    
    7) Platform9 
      -     offers managed Kubernetes on-premises or on any public cloud, and provides 24/7 health monitoring and alerting. (Kube2go, a web-UI driven Kubernetes cluster deployment service Platform9 released, has been integrated to Platform9 Sandbox.)
    
    8) OpenShift Dedicated 
      -     offers managed Kubernetes clusters powered by OpenShift.
    
    9) OpenShift Online 
      -     provides free hosted access for Kubernetes applications.
    
    10) IBM Cloud Kubernetes Service 
      -     offers managed Kubernetes clusters with isolation choice, operational tools, integrated security insight into images and containers, and integration with Watson, IoT, and data.
    
    11) Giant Swarm 
      -     offers managed Kubernetes clusters in their own datacenter, on-premises, or on public clouds.
    
    12) Kubermatic 
      -     provides managed Kubernetes clusters for various public clouds, including AWS and Digital Ocean, as well as on-premises with OpenStack integration.
    
    13) Oracle Container Engine for Kubernetes 
      -     is a fully-managed, scalable, and highly available service that you can use to deploy your containerized applications to the cloud.
    
    14) Kublr 
      -     offers enterprise-grade secure, scalable, highly reliable Kubernetes clusters on AWS, Azure, GCP, and on-premise. It includes out-of-the-box backup and disaster recovery, multi-cluster centralized logging and monitoring, and built-in alerting.
    
    15) APPUiO 
      -     runs an OpenShift public cloud platform, supporting any Kubernetes workload. Additionally APPUiO offers Private Managed OpenShift Clusters, running on any public or private cloud.
      
  Tunrkey Cloud Solutions (create Kubernetes clusters on a range of Cloud IaaS providers)
  
        1) Conjure-up Kubernetes with Ubuntu on AWS, Azure, Google Cloud, Oracle Cloud
        2) Google Compute Engine (GCE)
        3) AWS
        4) Azure
        5) Pivotal Container Service
        
       Others include below 
        Tectonic by CoreOS
        CenturyLink Cloud
        IBM Cloud
        Stackpoint.io
        Madcore.Ai
        Kubermatic
        Rancher 2.0
        Oracle Container Engine for K8s
        Gardener
        Kontena Pharos
        Kublr
        Agile Stacks
        Alibaba Cloud
        APPUiO
        
 On-Premises turnkey cloud solutions (create Kubernetes clusters on your internal, secure, cloud network)
 
        1) Pivotal Container Service
        2) Kubermatic
        
    Otheres include below 
        IBM Cloud Private
        SUSE CaaS Platform
        SUSE Cloud Application Platform
        Rancher 2.0
        Kontena Pharos
        Kublr
        Agile Stacks
        APPUiO
   
Custom Solutions
   
       Kubernetes can run on a wide range of Cloud providers and bare-metal environments, and with many base operating systems.
       