**Docker Command Line**

    docker --version    # display docker version
    docker version      # display version with more info
    docker info         # same as docker version
    
    
    docker build -t <imageName> .               #Build docker image with latest tag in the current directory
    docker build -t helloflask:1.0.0 .          #Build docker image with 1.0.0 tag in the current directory
    
    docker image ls -a                          # List all images on this machine
    docker image rm <image id>                  # Remove specified image from this machine
    docker image rm $(docker image ls -a -q)    # Remove all images from this machine
    
    docker run -p 4000:80 <imagename>           # Run the image
    docker run -d -p 4000:80 <imagename>        # Run in detached mode 
    docker run -it <imagename>                  # Run in interactive mode
    docker run --name static-site -e AUTHOR="Your Name" -d -P dockersamples/static-site
         -d will create a container with the process detached from our terminal
         -P will publish all the exposed container ports to random ports on the Docker host
         -e is how you pass environment variables to the container
         --name allows you to specify a container name
         AUTHOR is the environment variable name and Your Name is the value that you can pass
    docker port static-site      #Now you can see the ports by running the docker port command.
    
    docker ps                                   # List the running container
    docker ps -a                                # List all the container
    docker container ls                         # List the Container
    docker container stop <hash>                # Gracefully stop the specified container
    docker container kill <hash>                # Force shutdown of the specified container
    docker container rm <hash>                  # Remove specified container from this machine
    docker container rm $(docker container ls -a -q)   # Remove all containers  
    
    docker login                                # Login to docker hub Account 
               
    docker tag <imagename> <username>/<repository>:<tag>   #Create Tag
    docker push <username>/<repository>:<tag> (Publish)    #Push the Image 
    
    docker service ls                           # List running services associated with an app
    docker service create -p 80:80 --name web nginx:latest  # Createa a Service
    docker service ps <service>                 # List tasks associated with an app
    docker inspect <task or container>          # Inspect task or container
    
    docker-machine ls                           # List the VMs  
    docker-machine ip                           # Ip of the machine 
    docker-machine create --driver virtualbox <vmname>   #Create Virtual Machine
    docker-machine env <machinename>            # Environment variable 
    docker-machine ssh <vmname> "any command"   # ssh to other machine 
    docker-machine start <vmname>               # Start a VM that is currently not running
    docker-machine stop $(docker-machine ls -q) # Stop all running VMs
    docker-machine rm $(docker-machine ls -q)   # Delete all VMs and their disk images
    
    
    docker swarm init                           #Enable swarm mode and make your current machine a swarm manager 
    docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 ip>"   #Make a vm as swarm manager from outside
    docker swarm join                           #on other machines to have them join the swarm as workers.
    docker swarm join-token manager             #on other machien to join them as swarm manager
    docker swarm join-token worker              #Token of worker 
    docker swarm join --token <token> <myvm ip>:<port>   #join as worker
    docker swarm leave                          #To Leave Swarm 
    
    docker node ls                            #on the manager to view the nodes in this swarm
    docker node inspect <node ID>             # Inspect a node
    
    docker stack deploy -c docker-compose.yml <app>  # Deploy an app; command shell must be set to talk to manager (myvm1), uses local Compose file
    docker stack deploy --with-registry-auth -c docker-compose.yml <app>      #with this flag you can run on private registry
    docker stack deploy --compose-file docker-compose.yml <app>  # Deploy an app; command shell must be set to talk to manager (myvm1), uses local Compose file
    docker stack services <app>              # To verify your stack has deployed 
    
    eval $(docker-machine env myvm1)         # Mac command to connect shell to myvm1
    & "C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe" env myvm1 | Invoke-Expression   # Windows command to connect shell to myvm1
    eval $(docker-machine env -u)            # Disconnect shell from VMs, use native docker
            
            
    https://raw.githubusercontent.com/docker/labs/master/developer-tools/java/scripts/docker-compose-pull-images.yml        
    docker-compose -f docker-compose-pull-images.yml pull --parallel  # Parallely pull the image 