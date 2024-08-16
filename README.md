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
