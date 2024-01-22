# **_Introduction_**
**Postgres docker image:** Run postgres docker image/container without a dockerfile
>> docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:16

## Dockerfile
Dockerfile is used to define the structure and configuration of a Docker image, not the runtime characteristics of a container.

The Dockerfile includes instructions for building an image, specifying the base image, adding files, setting environment variables, exposing ports, and other image-related configurations. It does not contain information about container-specific details such as the container name or network name.
The local/host machine volume name is not specified in the Dockerfile.

Container-specific details, including the container name and network settings, are specified when you run a container based on the Docker image. When you run a container, you can use options such as --name to set the container name and --network to specify the network to which the container should be connected.

Run postgres docker container from a dockerfile.
>> docker build -t docker_sql . <!-- #"To build the image" -->
>> docker run -it --name docker_sql_container -p 5432:5432 docker_sql

**View Container:** 
>> docker ps

**Stop Container**
>> docker stop [container_name or container_id]

**Note:** Keep in mind that stopping a container doesn't remove it; it simply stops it. If you want to remove the container after stopping it, you can use the `docker rm`command. 
>> docker rm [container_name or container_id] #Not needed at thi time.

**Start the container again**
>> docker start -i docker_sql_container #Runs the container in interactive mode.

## Connect to a postgres database
 To connect to a postgres database via cli, we would require a tool called `pgcli`.
**Steps to install pgcli:** With python and pip already installed:
>> sudo apt-get install libpq-dev
>> pip install --upgrade --force-reinstall psycopg2
>> pip install pgcli

**Connect**
>> pgcli -h localhost -p 5432 -u root -d ny_taxi

### Download data via
>> wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz 

 >> gunzip yellow_tripdata_2021-01.csv.gz    <!--# To unzip the file -->
 >> wc -l  yellow_tripdata_2021-01.csv       <!--# To count the numbers of lines in the file -->
>> head -n 100 yellow_tripdata_2021-01.csv > yellow_head.csv   <!-- To get the first 100 lines of the dataset. -->

python
>> import pandas as pd
>> df = pd.read_csv('100 yellow_tripdata_2021-01.csv', nrows=100)

### Loading csv file to postgres
* We would require to specify the data schema using DDL syntax
>> print(pd.io.sql.get_schema(df, name='yellow_taxi_data'))

### Connecting to postgres database via pgadmin
>> docker run -it \
    -e PGADMMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4:latest \

<!-- You can save the above script in a `.sh` file "build_and_run_pgadmin.sh", then run the below command on the terminal -->
>> chmod +x build_and_run_pgadmin.sh
 **Run script**
 >> ./build_and_run_pgadmin.sh

 ### Two different containers
When we have two different running containers running in an isolated mood, it is impossible to connect both both via localhost. The right approach to do this connection is to create a netwook for these containers.
To achieve this, first stop the containers you want to connect/run in a network, and follow the below steps:

**Creating a netwook**
>> docker network create pg-network
**Update the containers script to at the network name created above and ensure that all containers in th network has a name.**

>> docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name docker_sql_container \
    postgres:16

<!--     OR   CONNECT AN EXISTING CONTAINER TO A NETWORK    -->
>> docker network create pg-network <!-- Create a network -->
>> docker network disconnect current-network docker_sql_container <!-- If the container is connected to any exisitng network -->
>> docker network connect pg-network docker_sql_container <!-- docker network connect my-network existing-container -->
