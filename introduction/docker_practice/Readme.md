# **_Introduction_**
**Data Engineering** is the design and development of systems for collecting, storing, transforming and analyzing data at scale. among the tools needed for data engineering is a data pipeline.

**Data Pipeline** is a service that receives data as input and outputs data in the desired format for a system. To develope a reusable data pipeline, we make use of a container(Docker).

**Docker** is an open platform for developing, shipping, and running applications.

**Docker image** is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization. Example, may build an image which is based on the ubuntu image, but installs the Apache web server and your application, as well as the configuration details needed to make your application run.

**Docker container** is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI. A container is defined by its image as well as any configuration options you provide to it when you create or start it. 

## Some docker commands and output
>> docker run -it ubuntu bash 
* **docker run:** Instructs Docker to run a container.
* **-it:** Enables an interactive mode and allocates a pseudo-TTY for smoother interaction.
* **ubuntu:** Specifies the Docker image based on the Ubuntu operating system.
* **bash:** Starts an interactive Bash shell inside the container.

>> docker run -it python:3.9 
* **python:3.9** This is the image name.

>> docker run -it --entrypoint=bash python:3.9 
* **ENTRYPOINT** command is used to specify the default executable that should run when a container starts. i.e what exactly should be executed when a container starts.

To enable repeatability of docker image/container, we use a docker file.

* **Dockerfile** is a text document that contains all the commands a user could call on the command line to assemble an image.
Docker can build images automatically by reading the instructions from a Dockerfile.

>> docker build -t test:pandas . 
* **test:pandas** this is our chosen image name, ususally a user defined name
* **.** This tells docker to chech the current directory for the dockerfile to use in building the image.

>> docker run -it test:pandas

<!-- THIS SECTION OF THE CODE OCCURED AFTER THE LESSON IN docker_sql directory -->
1. Updated the dockerfile to include instructions required for running the ingest_data.py file.
>> docker build -t ingest_data_image .
>> docker run -it --network=pg-network --name ingest_data_container ingest_data_image

2. For repaeted run of this container:
>> docker start -i ingest_data_container

## Using Docker-compose File

In summary, docker-compose file is an advanced and better way of saying "docker run my_image"

In essence, a docker-compose.yml file provides a more sophisticated and flexible approach compared to the simple docker run command. It allows you to define multiple services, each with its own configuration, dependencies, and network settings.

While docker run my_image is a command to start a single container using a specific image, a docker-compose.yml file allows you to define and manage a complete multi-container application, making it easier to orchestrate complex setups and environments