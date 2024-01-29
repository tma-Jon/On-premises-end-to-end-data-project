import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "sparking_flow",
    default_args = {
        "owner": "Vi Nguyen",
        "start_date": airflow.utils.dates.days_ago(1)
    },
    schedule_interval = "@daily"
)

start = PythonOperator(
    task_id="start",
    python_callable = lambda: print("Jobs started"),
    dag=dag
)

mysql_connect_jar = 'mysql-connector-j-8.3.0.jar'
iceberg_spark_jar = 'iceberg-spark-runtime-3.5_2.12-1.4.3.jar'
nessie_spark_jar = 'nessie-spark-extensions-3.5_2.12-0.76.3.jar'
s3a_jar = 'hadoop-aws-3.3.4.jar'
aws_sdk_jar = 'aws-java-sdk-bundle-1.12.262.jar'

python_job = SparkSubmitOperator(
    task_id="python_job",
    conn_id="spark-conn",
    application="jobs/spark-test.py",
    verbose=False,
    jars=f'/opt/airflow/jobs/jars/{mysql_connect_jar},/opt/airflow/jobs/jars/{iceberg_spark_jar},/opt/airflow/jobs/jars/{nessie_spark_jar},/opt/airflow/jobs/jars/{s3a_jar},/opt/airflow/jobs/jars/{aws_sdk_jar}',
    dag=dag
)

end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)

start >> python_job >> end