from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta   

from include.main import main


default_args = {
    "owner": "spinice007",
    "depends_on_past": False,
    "start_date": datetime(2025, 8, 29),
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
    "schedule_interval": "@hourly"
}

with DAG(dag_id='disaster_insurance', default_args=default_args) as dag:
    
    start = EmptyOperator(task_id='pipeline_start')

    end = EmptyOperator(task_id='pipeline_end')

    api_connect = PythonOperator(
        task_id='api_connect',
        python_callable=main
    )


start >> api_connect >> end