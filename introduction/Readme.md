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