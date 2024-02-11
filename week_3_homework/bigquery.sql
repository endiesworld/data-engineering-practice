-- Create a table in BQ using the Green Taxi Trip Records for 2022 without partition or cluster this table.

CREATE OR REPLACE EXTERNAL TABLE ny_taxi.external_nyc_green_taxi_2022_trip_data
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-workflow-emmanuel/nyc_green_taxi_2022.parquet']
);

CREATE OR REPLACE TABLE `ny_taxi.nyc_green_taxi_2022_trip_data`
AS
SELECT *
FROM `dtc-de-course-01-2024.ny_taxi.external_nyc_green_taxi_2022_trip_data`;

select 
  sum(size_bytes)/pow(10,6) as size
from
  ny_taxi.__TABLES__
where 
  table_id = 'external_nyc_green_taxi_2022_trip_data';


select 
  sum(size_bytes)/power(1024, 3) as size
from
  ny_taxi.__TABLES__
where 
  table_id = 'nyc_green_taxi_2022_trip_data';

SELECT
  SUM(total_logical_bytes) / power(1024, 3) AS total_logical_bytes
FROM
  `region-us`.INFORMATION_SCHEMA.TABLE_STORAGE;


-- How many records have a fare_amount of 0
SELECT
  COUNT(fare_amount)
FROM `ny_taxi.nyc_green_taxi_2022_trip_data`
  WHERE fare_amount = 0 ;


-- Create a partitioned table from table by lpep_pickup_datetime
CREATE OR REPLACE TABLE `ny_taxi.patitioned_by_lpep_nyc_green_taxi_2022_trip_data`
PARTITION BY
  lpep_pickup_date AS
SELECT * FROM `dtc-de-course-01-2024.ny_taxi.external_nyc_green_taxi_2022_trip_data`;


SELECT
  table_id,
  size_bytes/power(10, 6)
FROM
  `dtc-de-course-01-2024.ny_taxi.__TABLES__`
WHERE
  table_id = 'patitioned_by_lpep_nyc_green_taxi_2022_trip_data';
