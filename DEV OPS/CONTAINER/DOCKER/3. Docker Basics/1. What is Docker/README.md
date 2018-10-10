**What is Docker**

    Docker is a platform for developers and sysadmins to develop, deploy, and run applications with containers.
    
    The use of Linux containers to deploy applications is called containerization. 
    
    
Containerization is increasingly popular because containers are:

    Flexible: Even the most complex applications can be containerized.
    Lightweight: Containers leverage and share the host kernel.
    Interchangeable: You can deploy updates and upgrades on-the-fly.
    Portable: You can build locally, deploy to the cloud, and run anywhere.
    Scalable: You can increase and automatically distribute container replicas.
    Stackable: You can stack services vertically and on-the-fly.
    
`Images and containers`

    An image is an executable package that includes everything needed to run an application--the code, a runtime, libraries, environment variables, and configuration files.

    A container is launched by running an image. 
    
    A container is a runtime instance of an image--what the image becomes in memory when executed (that is, an image with state, or a user process). 
    
`Containers and virtual machines`

    A container runs natively on Linux and shares the kernel of the host machine with other containers. 
    It runs a discrete process, taking no more memory than any other executable, making it lightweight.
    
    By contrast, a virtual machine (VM) runs a full-blown “guest” operating system with virtual access to host resources through a hypervisor. 
    
    
`Docker Engine`
    
    Docker Engine is a client-server application with these major components:

        A server which is a type of long-running program called a daemon process (the dockerd command).

        A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.

        A command line interface (CLI) client (the docker command).
        
    The CLI uses the Docker REST API to control or interact with the Docker daemon through scripting or direct CLI commands.
    
    The daemon creates and manages Docker objects, such as images, containers, networks, and volumes

`Docker registries`

    A Docker registry stores Docker images. 
    
    Docker Hub and Docker Cloud are public registries that anyone can use.
    
    Docker is configured to look for images on Docker Hub by default. 
    
    You can even run your own private registry.
    
    If you use Docker Datacenter (DDC), it includes Docker Trusted Registry (DTR).
    
    Docker Cloud :  https://cloud.docker.com/
    
    Docker Hub : https://hub.docker.com/
    
    Docker Store : https://store.docker.com/
