#!/bin/bash
# --host will now be the database container's name. but while running on local machine, it used to be localhost because the conatainers port can be accessed by our local machine directly.
python ingest_data.py \
    --user=root \
    --password=root \
    --host=docker_sql_container \
    --port=5432 \
    --db=ny_taxi \
    --table=yellow_taxi_data \
    --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"