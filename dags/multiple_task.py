from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    return 'Hello world!'

dag = DAG('multiple_tasks_yoanparasta', description='DAG with multiple tasks',
          schedule_interval='@hourly',
          start_date=datetime(2024, 1, 1),
          catchup=False)

task_start = DummyOperator(task_id='start', dag=dag)
task_hello = PythonOperator(task_id='print_hello', python_callable=print_hello, dag=dag)
task_end = DummyOperator(task_id='end', dag=dag)

task_start >> task_hello >> task_end