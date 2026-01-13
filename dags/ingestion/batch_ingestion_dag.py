from airflow.models import TaskInstance
from airflow.decorators import dag, task
from datetime import datetime, timedelta
import logging

def task_failure_alert(context):
    ti: TaskInstance = context['task_instance']
    msg = f"""
    DAG: {ti.dag_id}
    Task: {ti.task_id}
    Execution_time: {context['execution_date']}
    Error: {context.get('exception')}
    """
    print(msg)

@dag(
    dag_id = "batch_ingestion_dag",
    schedule="@daily",
    start_date=datetime(2024,1,1),
    catchup=True,
    default_args={
        "retries":3,
        "retry_delay":timedelta(minutes=5),
        "on_failure_callback":task_failure_alert,
    },
    tags=["ingestion", "batch"],
)

# TaskFlow API used to simplify XCom handling
# Heavy processing intentionally avoided inside Airflow

def batch_ingestion():

    @task(sla=timedelta(minutes=15))
    def extract():
        return "raw data path"

    @task
    def validate(data):
        logging.info(f'Validating data: {data}')
        if data == "fail":
            raise ValueError("Data Validation failed!")
        return data

    @task
    def load(data):
        print(f"Loading data from {data}")

    load(validate(extract()))

batch_ingestion()