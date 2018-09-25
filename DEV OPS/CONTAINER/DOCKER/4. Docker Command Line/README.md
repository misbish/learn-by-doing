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
    
    
    docker container ls                         # List the Container
    docker container stop <hash>                # Gracefully stop the specified container
    docker container kill <hash>                # Force shutdown of the specified container
    docker container rm <hash>                  # Remove specified container from this machine
    docker container rm $(docker container ls -a -q)   # Remove all containers  
    
    docker login                                # Login to docker hub Account 
               
    docker tag <imagename> <username>/<repository>:<tag>   #Create Tag
    docker push <username>/<repository>:<tag> (Publish)    #Push the Image 