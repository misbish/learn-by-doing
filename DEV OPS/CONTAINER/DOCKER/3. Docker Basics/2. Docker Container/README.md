**DOCKER CONTAINER**

Learn the syntax of Dockerfile and its execution process


What happens behind the scene when you run a container : docker run helloworld ls -l

    - The Docker client contacts the Docker daemon
    - The Docker daemon checks local store if the image is available locally, and 
      if not, downloads it from Docker Store. 
    - The Docker daemon creates the container and then runs a command in that container.
    - The Docker daemon streams the output of the command to the Docker client
    
Terminology

    Docker daemon - The background service running on the host that manages building, running and distributing Docker containers.
    Docker client - The command line tool that allows the user to interact with the Docker daemon.
    Docker Store - A registry of Docker images, where you can find trusted and enterprise ready containers, plugins, and Docker editions.
    
Dockerfile
   
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
https://docs.docker.com/engine/reference/builder/#environment-replacement

    - Must start with FROM Keyword
    - There must be only 1 CMD 
    - Unlike RUN , CMD does not create additional layer .   
     