# Docker PostgreSQL and Terraform Project
## Overview
This project sets up a PostgreSQL database using Docker, Docker Compose and Terraform. It includes the necessary infrastructure to manage a database instance, and it provides a script to ingest data from CSV files into PostgreSQL tables.<br>
The README includes a step-by-step guide with instructions, queries, images, and more to ensure a clear and thorough understanding of the project.
## Prerequisites
* <b>Docker:</b> For containerization of the PostgreSQL instance.
* <b>Terraform:</b> To manage and provision your infrastructure.
* <b>Python:</b> To create the data ingestion script.
* <b>PostgreSQL Client:</b> For direct interaction with the PostgreSQL database.
## Docker Compose Setup
* Ensure you have Docker and Docker Compose installed on your system.
* Run the following Docker Compose command to start a PostgreSQL container and PgAdmin container:
  
    ```bash
    docker-compose up -d
    ```
## Python ingest data script Setup
This section will guide you through the setup of the Python script that ingests data into the PostgreSQL database. The script is containerized using Docker, which allows for easy deployment and execution.

### Step 1: Build the Docker Image
First, you need to create a Docker image for the Python ingest script. The image will be built from the Dockerfile in the project directory. To build the image, run the following command:

```bash
docker build -t taxi_ingest:v001 .
```

### Step 2: Run the Docker Container
Once the image is built, you can run the container to execute the Python script. The script will download the datasets, process them, and ingest the data into the PostgreSQL database. Use the following command to run the container:
```bash
docker run -it \
    taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name_1=green_tripdata \
    --url_1=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz \
    --table_name_2=zones \
    --url_2=https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
```

## Question 3. Count records
How many taxi trips were totally made on September 18th 2019?<br>
```sql
SELECT count(*) Trips
FROM green_tripdata
WHERE CAST(lpep_pickup_datetime as date) = '2019-09-18' 
	    AND CAST(lpep_dropoff_datetime as date) = '2019-09-18';
```
![Screenshot of the query]("C:\Users\maati\DataEngineering\Docker-Terraform\Docker\images\Query1.png")<br>

## Question 4. Longest trip for each day
Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.<br>
Tip: For every trip on a single day, we only care about the trip with the longest distance.<br>

```sql
SELECT CAST(lpep_pickup_datetime as date) as Trip_date,
	   MAX(trip_distance) as Trip_distance
FROM green_tripdata
GROUP BY CAST(lpep_pickup_datetime as date)
ORDER BY MAX(trip_distance) DESC;
```
![Screenshot of the query]("C:\Users\maati\DataEngineering\Docker-Terraform\Docker\images\Query2.png")<br>

## Question 5. Count records
Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown<br>
Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?<br>
```sql
SELECT z."Borough",
	   SUM(g.total_amount) as Total_amount
FROM green_tripdata as g
LEFT JOIN zones z on g."PULocationID" = z."LocationID"
WHERE CAST(lpep_pickup_datetime as date) = '2019-09-18'
GROUP BY 1
HAVING SUM(total_amount) > 5000
ORDER BY SUM(total_amount) DESC;
```
![Screenshot of the query]("C:\Users\maati\DataEngineering\Docker-Terraform\Docker\images\Query3.png")<br>

## Question 6. Largest tip
For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.
```sql
SELECT z."Zone" as Pickup_zone,
	   z1."Zone" as Dropoff_zone,
	   MAX(g.tip_amount) as Total_tip
FROM green_tripdata as g
LEFT JOIN zones z on g."PULocationID" = z."LocationID"
LEFT JOIN zones z1 on g."DOLocationID" = z1."LocationID"
WHERE CAST(lpep_pickup_datetime as date) BETWEEN '2019-09-01' AND '2019-09-30'
	  AND z."Zone" = 'Astoria'
GROUP BY 1,2
ORDER BY MAX(g.tip_amount) DESC;
```
![Screenshot of the query]("C:\Users\maati\DataEngineering\Docker-Terraform\Docker\images\Query4.png")<br>