# data-engineering-practice
## **_Introduction_**
**Data Engineering** is the design and development of systems for collecting, storing, transforming and analyzing data at scale. among the tools needed for data engineering is a data pipeline.

**Data Pipeline** is a service that receives data as input and outputs data in the desired format for a system. To develope a reusable data pipeline, we make use of a container(Docker).

**Docker** is an open platform for developing, shipping, and running applications.

**Docker image** is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization. Example, may build an image which is based on the ubuntu image, but installs the Apache web server and your application, as well as the configuration details needed to make your application run.

**Docker container** is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI. A container is defined by its image as well as any configuration options you provide to it when you create or start it. 
<!-- for a container, localhost is its self-->

## Serving project modules via http
>> python -m http.server 
>> ipconfig <!-- To access your machines ip sddress -->
python: Calls the Python interpreter.
-m: Stands for "module," allowing you to run a module as a script.
http.server: The module that comes with Python 3 and provides a basic HTTP server.
When you run python -m http.server in your terminal or command prompt, it starts an HTTP server on your local machine, serving files from the current working directory. By default, it uses port 8000.

Here's what happens:

If you don't specify a port, the server will listen on port 8000.
It serves files from the current working directory.
You can access the served files by opening a web browser and navigating to http://localhost:8000 (or the specified port if you provided one).