from datetime import datetime
from typing import List
import re

from airflow import DAG
from airflow import AirflowException
from airflow.operators.python import PythonOperator
from gousto.core import get_recipe


def process_recipe(**kwargs):
    dag_run_conf = kwargs["dag_run"].conf
    url = dag_run_conf.get("url", None)

    if not url:
        raise ValueError('Url of gousto recipe not provided')

    data = get_recipe(url=url)
    return data


dag = DAG(
    dag_id="gousto_dag",
    description="Search gousto recipe",
    start_date=datetime(2022, 11, 1),
    schedule_interval=None
)

dag.trigger_arguments = {"url": "string"}

task = PythonOperator(
    task_id="gousto_task",
    python_callable=process_recipe,
    provide_context=True,
    dag=dag)