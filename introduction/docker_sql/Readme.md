# **_Introduction_**
**Postgres docker image:** Run postgres docker image/container without a dockerfile
>> docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v ny_taxi_postgres_data: /var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:16

**Dockerfile** Run postgres docker image/container from a dockerfile.
>> docker build -t docker_sql . #"To build the image"
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
