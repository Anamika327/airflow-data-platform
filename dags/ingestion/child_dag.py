from airflow.decorators import task, dag
from datetime import datetime, timedelta

@dag(
    dag_id="child_processing_dag"
    schedule=None
    start_date=datetime(2024,1,1)
    catchup = False
    default_args = {
        "retries":2,
        "retry_delay":timedelta(minutes=5),
        tags=["processing", "child"]
    }
)

def child_processing():

    @task
    def transform():
        print("Transforming data")
        
    @task
    def load():
        print("loading procesed data...")

    load(transform())

child_processing()