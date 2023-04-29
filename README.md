### Web-based docker application

#### Pre-requisites
- Install docker - `sudo apt update && sudo apt install docker.io -y`
- Bring docker service up - `service docker start`

#### Steps to execute
- Check if container associated with this app is already executed - `docker ps –a`
- If container is already running, stop it and remove it - `docker rm $( docker stop <container-id> )`
- Migrate to app repository - `cd my-first-docker-app`
- Build docker image for app - `docker build -t <image-name> .`
- Execute build docker image in container - `docker run -p 8888:5000 --name <container-name> <image-name>`
- Now to go browser and run `localhost:8888`. This will run ur application in web browser.

#### Result
![Screenshot of Web-based Docker Application Execution Result](result.png)
