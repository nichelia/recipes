from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def hello_world():
    return 'Hello World'


dag = DAG('hello_world_dag',
          description='Hello World DAG',
          start_date=datetime(2022, 11, 1),
          schedule_interval=None,
          catchup=False)

task = PythonOperator(task_id='hello_world_task', python_callable=hello_world, dag=dag)
task