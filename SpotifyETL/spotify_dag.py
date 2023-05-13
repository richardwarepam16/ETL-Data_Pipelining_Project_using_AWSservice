from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from spotify_api_dataExtract import lambda_handler1
from tranform_load_function import album, artist, songs, lambda_handler2

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 13),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

task1 = PythonOperator(
    task_id='complete_task1',
    python_callable= lambda_handler1,
    dag=dag, 
) 

task2 = PythonOperator(
    task_id='complete_album',
    python_callable= album,
    dag=dag, 
)

task3 = PythonOperator(
    task_id='complete_artist',
    python_callable= artist,
    dag=dag, 
)

task4 = PythonOperator(
    task_id='complete_songs',
    python_callable= songs,
    dag=dag, 
)

task5 = PythonOperator(
    task_id='complete_task2',
    python_callable= lambda_handler2,
    dag=dag, 
)

task1
task2
task3
task4
task5
