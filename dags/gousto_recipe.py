from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def get_recipe(**kwargs):
    dag_run_conf = kwargs["dag_run"].conf
    return dag_run_conf["url"]


dag = DAG(
    dag_id="gousto_dag",
    description="Search gousto recipe",
    schedule_interval=None
)

dag.trigger_arguments = {"url": "string"}

task = PythonOperator(
    task_id="hello_world_task",
    python_callable=get_recipe,
    provide_context=True,
    dag=dag)