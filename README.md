# Docker PostgreSQL and Terraform Project
## Overview
This project sets up a PostgreSQL database using Docker and Terraform. It includes the necessary infrastructure to manage a database instance, and it provides a script to ingest data from CSV files into PostgreSQL tables.<br>
The README includes a step-by-step guide with instructions, queries, images, and more to ensure a clear and thorough understanding of the project.
## Prerequisites
* <b>Docker:</b> For containerization of the PostgreSQL instance.
* <b>Terraform:</b> To manage and provision your infrastructure.
* <b>Python:</b> To run the data ingestion script.
* <b>PostgreSQL Client:</b> For direct interaction with the PostgreSQL database.
## Docker Compose Setup
* Ensure you have Docker and Docker Compose installed on your system.
* Run the following Docker Compose command to start a PostgreSQL container and PgAdmin container:
  
    ```bash
    docker-compose up -d
    ```


