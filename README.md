# On-Premises Batch Data Processing build on Docker Project
### 1. Docker basic learning
  - Install WSL version 2 and Docker Desktop (for Windows)
  https://docs.docker.com/desktop/install/windows-install/
  - In the folder C:\Users\<your-user>, create .wslconfig and write the number of memory that you want to allocate for the wsl2 system

![image](https://github.com/tma-Jon/On-prem-batch-data-project/assets/105640122/a80695c5-945f-4295-90de-259068b24473)

  - Learn Docker basic
https://www.youtube.com/watch?v=Y3zqsFpUzMk&list=PLncHg6Kn2JT4kLKJ_7uy0x4AdNrCHbe0n

### 2. Download jars file
  - mysql-connector-j-8.3.0.jar
  - iceberg-spark-runtime-3.5_2.12-1.4.3.jar
  - nessie-spark-extensions-3.5_2.12-0.76.3.jar
  - hadoop-aws-3.3.4.jar
  - aws-java-sdk-bundle-1.12.262.jar

### 3. Run Docker Compose
  - Git clone the source code, create new branch if you want to edit source code then create pull request later
  - Build image for airflow first, go to airflow folder then run
```
docker build -t airflow
```
Learn more about how to build airflow docker here https://www.youtube.com/watch?v=o_pne3aLW2w&t=2866s
  - Back to the docker compose file folder, run
```
docker compose -p de-project up -d
```
#### Note: airflow and dremio are heavy, so you should not run them at the same time if your memory is not big enough.

### 4. Create data in MySQL
  - Using MySQL Workbench to connect MySQL
  - Create table and import data sample (data-test.csv), detail in the mysql-query folder

### 5. Create bucket and access key in Minio
  - Connect to Minio at localhost:9000
  - Create bucket name de-1
  - Create access key and secret key

### 6. Submit spark job directly to spark cluster
  - Copy jars file to same folder with docker compose file
  - Input Minio access key and secret key in spark-test.py
  - run command
```
docker exec de-project-spark-master-1 spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/spark-test.py
```
#### Note: edit spark-test.py before run

### 7. Submit spark job using airflow
  - Copy jars file to folder airflow/jobs/jars
  - Input Minio access key and secret key in airflow/jobs/spark-test.py
  - Go to localhost:8080, in the DAGs, choose the job and start
  - Learn more here https://www.youtube.com/watch?v=waM3Z6ofj9c&t=464s
#### Note: edit airflow/jobs/spark-test.py before run

### 8. Query data using Dremio
  - Go to localhost:9047 to access Dremio
  - Config Nessie catalog and Minio, follow https://www.dremio.com/blog/intro-to-dremio-nessie-and-apache-iceberg-on-your-laptop/

