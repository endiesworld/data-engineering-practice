#!/bin/bash

# Build the Docker image
docker build -t my-pgadmin-image .

# Run the Docker container interactively
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pgadmin_container \
    my-pgadmin-image
