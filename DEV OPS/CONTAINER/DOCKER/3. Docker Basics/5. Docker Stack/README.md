**Docker Stack**

    A stack is a group of interrelated services that share dependencies, and 
    can be orchestrated and scaled together. 
    
    docker stack ps <stack name>            # See the visualization 
    
    
    
A sample docker-compose.yml with 3 service 

    version: "3"   # This is mandatory , as docker stack deploy wont work with earlier version
    services:
      web:  #Service  name
        # replace username/repo:tag with your name and image details
        image: username/repo:tag
        deploy:
          replicas: 5
          restart_policy:
            condition: on-failure
          resources:
            limits:
              cpus: "0.1"
              memory: 50M
        ports:
          - "80:80"
        networks:
          - webnet
      visualizer:
        image: dockersamples/visualizer:stable
        ports:
          - "8080:8080"
        volumes:
          - "/var/run/docker.sock:/var/run/docker.sock"  
        deploy:
          placement:
            constraints: [node.role == manager]
        networks:
          - webnet
      redis:
        image: redis
        ports:
          - "6379:6379"
        volumes:
          - "/home/docker/data:/data"   #Give the service access to the host’s socket file for Docker
        deploy:
          placement:
            constraints: [node.role == manager]   # to ensure the service only ever runs on a swarm manager -- never a worker
        command: redis-server --appendonly yes
        networks:
          - webnet
    networks:
      webnet:
      
Deploy     

    docker stack deploy --compose-file docker-compose.yml vote
    
Verfiy
    
    docker stack services vote

YML File
    
    version: "3" is mandatory 
    services key which contains all the service
    NOTE : There is a build key but , docker stack deploy does not suppport build, hence use pre built images
    depends_on - one service depend on other 
    deploy : new in version 3 , allows you to specify variiour properties of deployment
    

    
    