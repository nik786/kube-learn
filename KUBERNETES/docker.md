

How do you ensure a container restarts automatically if it crashes?
--------------------------------------------------------------------

--restart policy: <br>
docker run --restart always <image_name>

How do you handle a container running out of disk space?
--------------------------------------------------------

Check disk usage:

docker system df

Prune unused resources:

docker system prune -a --volumes

Clean unused images:
docker image prune -a



How do you troubleshoot network issues between Docker containers?
------------------------------------------------------------------


Check the network configuration:<br>
docker network inspect <network_name>

Verify container connectivity using ping:
docker exec <container_id> ping <another_container>

Ensure both containers are on the same network.

Examine firewall rules and port mappings.

Use curl or telnet to test specific ports:
docker exec <container_id> curl http://<other_container>:<port>


How do you pass sensitive data to a Docker container securely?

Use Docker secrets:

Create a secret:
echo "my-secret-password" | docker secret create db_password -

Use the secret in a Docker service:

docker service create --name my-service --secret db_password alpine

Pass environment variables securely with docker-compose:

version: '3.7'
services:
 app:
 image: my-app
 environment:
 - SECRET_KEY=${SECRET_KEY}


How do you reduce the size of a Docker image?


Use smaller base images like alpine:
FROM alpine:latest


Minimize the number of layers by combining commands:

RUN apt-get update && apt-get install -y \
 curl \
 vim && \
 apt-get clean

Remove unnecessary files in the same layer:
RUN rm -rf /var/lib/apt/lists/*

Use .dockerignore to exclude files from the build context.



How do you connect a Docker container to multiple networks?
Answer:
1. Create the networks:
docker network create network1
docker network create network2
2. Run the container and attach it to one network:
docker run --network network1 --name my-container -d alpine
3. Connect the container to the second network:
docker network connect network2 my-container
4. Verify connections:
docker network inspect network1
docker network inspect network2



 How do you set resource limits for a container?
Answer:
 Use the --memory and --cpu options when running a container:
docker run --memory=512m --cpus=1 <image_name>
 Example to limit:
o Memory to 512MB.
o CPU usage to 1 core.
 For docker-compose:
version: '3.7'
services:
 app



 How do you share environment variables across multiple containers?
Answer:
1. Use an .env file:
o Example .env file:
DB_USER=root
DB_PASSWORD=secret
o Reference in docker-compose.yml:
version: '3.7'
services:
 app:
 image: my-app
 env_file:
 - .en

Use a shared configuration management tool like HashiCorp Vault or
AWS Secrets Manager for production environments.



How do you run multiple versions of the same application in Docker?
Answer:
1. Use separate tags for each version:
docker run --name app-v1 my-app:v1



docker run --name app-v2 my-app:v2
2. Use different ports for each version:
docker run -p 8080:80 my-app:v1
docker run -p 8081:80 my-app:v2


. How do you troubleshoot high CPU usage in a Docker container?
Answer:
1. Identify the problematic container:
docker stats
2. Inspect the running processes:
docker exec <container_id> top
3. Analyze the logs:
docker logs <container_id>
4. Profile the application to detect bottlenecks.
5. Use strace or similar tools inside the container:
docker exec <container_id> strace -p <process_id>




How do you build a multi-stage Dockerfile?
Answer:
 Multi-stage builds optimize image size by separating build and runtime
stages:
# Build stage
FROM node:16 AS builder
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build
# Production stage
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html




How do you roll back to a previous version of an image?
Answer:
1. Pull the previous version:
docker pull my-app:v1
2. Stop the current container:
docker stop <container_id>
3. Start a new container with the older version:
docker run --name app-v1 -d my-app:v1






How do you run a container with limited network access?
Answer:
 Use a custom Docker network with restricted rules:
docker network create --subnet=192.168.1.0/24 my-network
docker run --network my-network <image_name>
 Use firewall rules on the host to restrict outgoing traffic.
 Use --network none to completely isolate the container from the
network:






How do you configure logging for a Docker container?
Answer:
1. Use logging options when running a container:
docker run --log-driver json-file --log-opt max-size=10m --log-opt max-file=3
<image_name>
2. Configure logging in docker-compose.yml:
logging:
 driver: "json-file"
 options:
 max-size: "10m"
 max-file: "3"
3. Integrate with centralized logging systems like Fluentd or ELK by
specifying a logging driver.




How do you restart a container automatically with a delay between
retries?
Answer:
 Use --restart policies with Docker Compose:
version: '3.7'
services:
 app:
 image: my-app
 deploy:
 restart_policy:
 condition: on


 docker run --restart on-failure:<max_attempts> <image_name>





  How do you prevent data loss when recreating a container?
Answer:
1. Use named volumes:
docker volume create my_data
docker run -v my_data:/app/data <image_name>
2. Backup the volume before recreating the container:
docker run --rm -v my_data:/data -v $(pwd):/backup busybox tar czf
/backup/data.tar.gz /data
3. Store configurations in environment variables or configuration files
mounted as volumes.




. How do you scale a service in Docker Compose?
Answer:
1. Use the --scale option with docker-compose:
docker-compose up --scale app=5
2. Define scaling in the Compose file:
version: '3.7'
services:
 app:
 image: my-app
 deploy:
 replicas: 5
3. Ensure the application can handle multiple replicas (e.g., stateless
design, shared storage).




 How do you handle a situation where a container is consuming too much
memory?
Answer:
1. Set memory limits during container creation:
docker run --memory=512m <image_name>
2. Monitor container memory usage with docker stats:
docker stats <container_id>
3. Check logs for memory-related errors:

docker logs <container_id>
4. Optimize the application code and reduce memory-intensive operations.




How do you limit the number of processes inside a container?
Answer:
1. Use the --pids-limit option:
docker run --pids-limit=100 <image_name>
2. Configure this limit in docker-compose.yml:
version: '3.7'
services:
 app:
 image: my-app
 deploy:
 resources:
 limits:
 pids: 100



cat /proc/sys/kernel/pid_max


How do you restart a container with updated environment variables
without stopping the current one?
Answer:
1. Use docker update to modify the environment variables:
docker update --env NEW_VAR=value <container_id>
(Note: This works only for certain updates; restarting is generally required for
env changes.)
2. Stop and start the container with new variables:
docker stop <container_id>
docker run -e NEW_VAR=value <image_name>
3. Use docker-compose to apply changes:
docker-compose up -d



How do you ensure a Docker container always starts on system boot?
Answer:
1. Use the --restart always policy:
docker run --restart always <image_name>
2. For docker-compose, define the restart policy:
version: '3.7'
services:
 app:
 image: my-app
 restart: always
3. Enable Docker to start on boot:
sudo systemctl enable docker





How do you secure a Docker container running a sensitive application?
Answer:
1. Use non-root users:
RUN adduser --disabled-password appuser
USER appuser
2. Limit container capabilities:
docker run --cap-drop=ALL <image_name>
3. Enable read-only filesystem:
docker run --read-only <image_name>
4. Use secrets management tools for sensitive data.
5. Scan the image for vulnerabilities using tools like Trivy.




How do you connect a container to a running database container?
Answer:
1. Use a shared Docker network:
docker network create my-network
docker run --network=my-network --name=db postgres
docker run --network=my-network my-app
2. Use the container name as the hostname:
o Example configuration in the app:
DATABASE_HOST=db
DATABASE_PORT=5432
3. Test connectivity from the application container:
docker exec <app_container_id> ping db




How do you handle image versioning for a CI/CD pipeline?
Answer:
1. Tag images with unique identifiers:
docker build -t my-app:1.0 .
2. Use Git commit hashes or build numbers for tagging:
docker build -t my-app:$(git rev-parse --short HEAD) .
3. Automate the tagging and push in CI/CD pipelines:
docker build -t my-app:${CI_COMMIT_TAG} .
docker push my-app:${CI_COMMIT_TAG}
4. Use a latest tag for the most recent stable version



How do you run a container in privileged mode, and why would you need
it?
Answer:
 Privileged mode grants the container access to host resources, similar to
root access.
 Run a container in privileged mode:
docker run --privileged <image_name>
 Common use cases:
o Running Docker inside Docker (dind).
o Accessing hardware devices like USB or GPU.
 Caution: Avoid using privileged mode in production due to security risks



. How do you manage multiple containers with different configurations in
Docker Compose?
Answer:
1. Define separate services in the docker-compose.yml file:



version: '3.7'
services:
 app:
 image: my-app
 ports:
 - "8080:8080"
 environment:
 - ENV=production
 db:
 image: postgres
 environment:
 - POSTGRES_PASSWORD=secret
2. Use multiple Compose files for overrides:
docker-compose -f docker-compose.yml -f docker-compose.override.yml up
3. Pass environment-specific configurations using .env files.




How do you debug slow container startup times?
Answer:
1. Analyze logs:
docker logs <container_id>
2. Profile the application startup process inside the container:
docker exec -it <container_id> /bin/bash
3. Check health checks in the Compose file or Kubernetes deployment.
4. Investigate dependencies like database or API latency.



How do you implement health checks in a Docker container?
Answer:
 Define health checks in the Dockerfile:
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -f
http://localhost:8080/health || exit 1
 Use docker inspect to monitor health status:
docker inspect <container_id> | grep Health
 For Docker Compose:
healthcheck:
 test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
 interval: 30s
 timeout: 5s
 retries: 3
   

How do you back up and restore a Docker volume?

1. Backup:
   
docker run --rm -v my_volume:/data -v $(pwd):/backup busybox tar czf
/backup/backup.tar.gz /data

2. Restore:

docker run --rm -v my_volume:/data -v $(pwd):/backup busybox tar xzf
/backup/backup.tar.gz -C /data




How do you deploy a multi-tier application using Docker Compose?
Answer:
 Example docker-compose.yml for a multi-tier app:
version: '3.7'
services:
 frontend:
 image: frontend-app
 ports:
 - "3000:3000"
 depends_on:
 - backend
 backend:
 image: backend-app
 ports:
 - "5000:5000"
 depends_on:
 - db
 db:
 image: postgres
 environment:
 - POSTGRES_PASSWORD=secret




How do you handle secrets securely in Docker Compose?
Answer:
1. Use the secrets feature in Compose version 3.1+:
version: '3.7'
services:
 app:
 image: my-app
 secrets:
 - db_password
secrets:
 db_password:
 file: ./db_password.txt
2. Ensure the secrets file is excluded from version control (.gitignore).
3. Use external tools like HashiCorp Vault or AWS Secrets Manager for
production.




How do you secure Docker images before deployment?
Answer:
1. Use tools to scan for vulnerabilities:
trivy image <image_name>
2. Minimize the image size using smaller base images like alpine.
3. Avoid embedding secrets in the image.
4. Implement multi-stage builds to exclude unnecessary files:
FROM builder AS build-stage
# Build application
FROM alpine AS runtime
# Copy only necessary artifacts
COPY --from=build-stage /app /app

Sign images using Docker Content Trust (DCT):
export DOCKER_CONTENT_TRUST=1














