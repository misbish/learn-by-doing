**Docker Service**

    A service only runs one image,
    but it codifies the way that image runs
        - what ports it should use,
        - how many replicas of the container should run so the service has the capacity it needs
          and so on
          
    It’s very easy to define, run, and scale services with the Docker platform 
    -- just write a docker-compose.yml file.   
    
`1. Define service with docker-compose.yml`

    version: "3"
    services:
      web:
        # replace username/repo:tag with your name and image details
        image: username/repo:tag
        deploy:
          replicas: 5
          resources:
            limits:
              cpus: "0.1"
              memory: 50M
          restart_policy:
            condition: on-failure
        ports:
          - "4000:80"
        networks:
          - webnet
    networks:
      webnet:   #load-balanced overlay network
      
  
  
`2. Start the cluster`

    docker swarm init
        
`3. Run the App`

    docker stack ls   #List stacks or apps    
    docker stack deploy -c docker-compose.yml <appname>
    
`4. Verify` 

    docker service ls       # List running services associated with an app
    docker service ps <service>     # List tasks associated with an app
    docker inspect <task or container>    # Inspect task or container
    
`5. Stop`

    docker stack rm <appname>       # Tear down an application
    docker swarm leave --force      # Take down a single node swarm from the manager  