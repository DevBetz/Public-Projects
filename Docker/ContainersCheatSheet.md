# Containers Cheat Sheet
## **1. Docker Basics**

|Command|Description|
|---|---|
|`docker --version`|Check Docker version.|
|`docker info`|View system-wide information about Docker.|
|`docker help`|Show help for Docker commands.|

---

## **2. Working with Images**

|Command|Description|
|---|---|
|`docker images`|List all locally available images.|
|`docker search <image>`|Search for an image on Docker Hub.|
|`docker pull <image>`|Download an image from Docker Hub.|
|`docker build -t <name> .`|Build an image from a Dockerfile in the current directory.|
|`docker rmi <image>`|Remove a specific image.|
|`docker rmi $(docker images -q)`|Remove all unused images.|

---

## **3. Working with Containers**

|Command|Description|
|---|---|
|`docker ps`|List all running containers.|
|`docker ps -a`|List all containers (including stopped ones).|
|`docker run <image>`|Run a container from an image.|
|`docker run -it <image>`|Run a container in interactive mode (with a shell).|
|`docker run -d <image>`|Run a container in detached mode (in the background).|
|`docker stop <container>`|Stop a running container.|
|`docker start <container>`|Start a stopped container.|
|`docker restart <container>`|Restart a running or stopped container.|
|`docker rm <container>`|Remove a stopped container.|
|`docker rm $(docker ps -a -q)`|Remove all stopped containers.|
|`docker logs <container>`|View logs from a container.|
|`docker exec -it <container> bash`|Execute a bash shell inside a running container.|

---

## **4. Networking**

|Command|Description|
|---|---|
|`docker network ls`|List all Docker networks.|
|`docker network create <name>`|Create a custom network.|
|`docker network connect <network> <container>`|Connect a container to a network.|
|`docker network disconnect <network> <container>`|Disconnect a container from a network.|

---

## **5. Volumes and Storage**

|Command|Description|
|---|---|
|`docker volume ls`|List all volumes.|
|`docker volume create <name>`|Create a new volume.|
|`docker volume rm <name>`|Remove a volume.|
|`docker run -v <host_path>:<container_path> <image>`|Mount a host directory as a volume in a container.|
|`docker run -v <volume_name>:<container_path> <image>`|Use a Docker-managed volume.|

---

## **6. Inspecting and Debugging**

|Command|Description|
|---|---|
|`docker inspect <container_or_image>`|Display detailed information about a container or image.|
|`docker stats`|Display live resource usage stats for running containers.|
|`docker top <container>`|Show processes running inside a container.|
|`docker diff <container>`|Show changes made to a container’s filesystem.|

---

## **7. Docker Compose**

|Command|Description|
|---|---|
|`docker-compose up`|Start all services defined in a `docker-compose.yml` file.|
|`docker-compose down`|Stop and remove services defined in a `docker-compose.yml` file.|
|`docker-compose ps`|List all services managed by Docker Compose.|
|`docker-compose logs`|View logs for services defined in the Compose file.|

---

## **8. Clean Up**

|Command|Description|
|---|---|
|`docker system prune`|Remove unused data (stopped containers, unused networks, dangling images).|
|`docker system df`|Show disk usage by Docker.|
|`docker volume prune`|Remove all unused volumes.|
|`docker image prune`|Remove all dangling (unused) images.|

---

## **Tips for Getting Started**

1. **Use Descriptive Names:** Use the `--name <name>` option with `docker run` to assign a meaningful name to your container.
    
    bash
    
    Copy code
    
    `docker run --name my-container -d nginx`
    
2. **Save Docker Commands as Aliases:** Add shortcuts to your shell configuration file for frequently used commands.
    
    bash
    
    Copy code
    
    `alias dps="docker ps -a" alias drm="docker rm $(docker ps -a -q)"`
    
3. **Explore Docker Hub:** Many ready-to-use images are available on Docker Hub (e.g., `mysql`, `nginx`, `ubuntu`).
    
4. **Experiment with Docker Compose:** Create a `docker-compose.yml` file to manage multi-container applications.






set up docker networks:
watch this network chuck video for more info:
https://www.youtube.com/watch?v=bKFMS5C4CG0&list=PLIhvC56v63IJlnU4k60d0oFIrsbXEivQo&index=4

```
sudo docker network create 

```

macvlan


check out docker documentation.
https://docs.docker.com/get-started/introduction/build-and-push-first-image/

# Notes:

## Working List of commonly used commands:

This will show the command that was used to create each layer within the image:
`docker image history`

See the layers you created:
`docker image history getting-started`

Runs a nginx web server on port 80 in detatched mode (meaning you can do other stuff with the terminal and not just have to open a new tab for that to run)
`docker run -p 80:80 -d nginx`

To specify a name:
`docker run -p 80:80 -d --name Container_Name_Here nginx`

Stop container:
`docker stop container_name_here`

Remove all stopped containers:
`docker container prune`


Automatically remove stopped containers once they are stopped.
`docker run -p 80:80 -d --rm nginx`



Leaving this here to make copying easier:
`docker run -p 80:80 nginx`



can refer to a container by its ID or by name.

if you don't specify version, you get the latest version.




slim images:
alpine images.

tags to specify things.
any tags with slim.
slim are much more barebones versions.

alpine linux is a minimum linux distro focused on minimalism.

alpine images:
- musl libc
- ash default shell
- apk & .apk packages
- busybox



debugging:

```
# run this command for debugging. -it means interactive and tty gives us a nicer cli interface and allows us to keep interacting with it:

docker exec -it <container_ID_here> /bin/bash





# stuff for copying:
docker run -p 80:80 nginx


```

adding persistence: essentially saving stuff to a storage unit.
different mount types:
- volumes
- bind-mounts
- tempfs mounts


volumes:
- newer
- more features
- managed by docker daemon
- syntax
	- -v mydata:/path/in/container
	- or more verbose --mount

bind mounts:
- older but still useful
- less features
- mounts host file/dir into container
	- -v ./mydata:/path/in/container
	- -v /mydata:/path/in/container
	- or more verbose --mount

just depends if you give it a name (like "data") or an absolute path or a relative path.

they both use the- V flag it just depends on whether you give it a name like my data or a relative or absolute path like /mydata or ./mydata if you give it a path then Docker will Mount
The Source path into the target path as a bind Mount if you give it a name then Docker will mount a named volume into the target path.

let's try creating a my data directory and passing my data to


when using code on your local machine, bind mounts are typically what you want because their main benefit is that they are simply mapping a file or data on the host into the container. you can see all the files right there inspect them in your IDE or with other programs and change them as you please.

benefits:
volumes:
- often better in production
- not dependent on host filesystem
- easy to share across containers.
- can use remote or cloud storage
	- aws efs
	- nfs
	- sshfs
- container does not need access to host
- this is not convenient to share with the host. cannot conveniently view or modify a file from the host


bind-mounts:
- often convenient in dev
- quickly share w/ host
	- gives container access to host. can mitigate this by making them read only
	- consider readonly mount
		- -v ./mydata:/path/in/container:ro



docker makes it super easy to create you own images.
