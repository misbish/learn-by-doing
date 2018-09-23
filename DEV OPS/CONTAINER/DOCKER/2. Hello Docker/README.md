**DOCKER HELLOWORLD**

`1. Define a container with Dockerfile`
           
           vi Dockerfile
           
           
           # Use an official Python runtime as a parent image
           FROM python:2.7-slim
           
           # Set the working directory to /app
           WORKDIR /app
           
           # Copy the current directory contents into the container at /app
           COPY . /app
           
           # Install any needed packages specified in requirements.txt
           RUN pip install --trusted-host pypi.python.org -r requirements.txt
           
           # Make port 80 available to the world outside this container
           EXPOSE 80
           
           # Define environment variable
           ENV NAME World
           
           # Run app.py when the container launches
           CMD ["python", "app.py"]

`2. Build the app`

           docker build -t helloflask .
           
           NOTE: helloflask must be lowercase
           
           By Default , latest tag will be built.Else supply tag as
                 docker build -t helloflask:1.0.0 .
           
`3. List Image`

           docker image ls 
           
           docker image ls -a          # List all images on this machine
           docker image rm <image id>      # Remove specified image from this machine
           docker image rm $(docker image ls -a -q)   # Remove all images from this machine
           
           
`4. Run the app`

           docker run -p 4000:80 helloflask
           
           docker run -d -p 4000:80 helloflask ( Run in detached mode )
           
`5. List Container`

           docker container ls 
           
`6. Verify`

           http://localhost:4000
           
           NOTE:  If you are running using docker toolbox , then find ip 
           as docker-machine ip and use that ip instead of localhost
           
          
           
`7. Quit`

           Ctrl + C  then
           
           docker container stop <Container Name or ID>
           
           docker container stop <hash>     # Gracefully stop the specified container
           docker container kill <hash>     # Force shutdown of the specified container
           docker container rm <hash>       # Remove specified container from this machine
           docker container rm $(docker container ls -a -q)   # Remove all containers
           
`8. Share your image`

           Create a Docker account, sign up for one at hub.docker.com.
           
           docker login  (Login)
           
           docker tag <imagename> <username>/<repository>:<tag>  (Create Tag)
           
           docker push <username>/<repository>:<tag> (Publish)
           
           
           From now onwards , you can run anywhere using below 
           docker run -p 4000:80 <username>/<repository>:<tag>
           
           
           NOTE : You can set up your own private registry using Docker Trusted Registry.