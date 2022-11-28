from datetime import datetime
from typing import List
import re

from airflow import DAG
from airflow import AirflowException
from airflow.operators.python import PythonOperator
from markdownify import markdownify as md
from recipe_scrapers import scrape_me
from recipe_scrapers.goustojson import GoustoJson
import parse_ingredients


def get_recipe(**kwargs):
    dag_run_conf = kwargs["dag_run"].conf
    url = dag_run_conf.get("url", None)

    if not url:
        raise ValueError('Url of gousto recipe not provided')

    return url


dag = DAG(
    dag_id="gousto_dag",
    description="Search gousto recipe",
    start_date=datetime(2022, 11, 1),
    schedule_interval=None
)

dag.trigger_arguments = {"url": "string"}

task = PythonOperator(
    task_id="gousto_task",
    python_callable=get_recipe,
    provide_context=True,
    dag=dag)