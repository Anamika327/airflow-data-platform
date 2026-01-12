from airflow.decorators import dag, task
from datetime import datetime, timedelta
@dag(
    dag_id = "batch_ingestion_dag",
    schedule="@daily",
    start_date=datetime(2024,1,1),
    catchup=True,
    default_args={
        "retries":3,
        "retry_delay":timedelta(minutes=5),
    },
    tags=["ingestion", "batch"],
)

# TaskFlow API used to simplify XCom handling
# Heavy processing intentionally avoided inside Airflow

def batch_ingestion():

    @task
    def extract():
        return "raw data path"

    @task
    def validate(data):
        return data

    @task
    def load(data):
        print(f"Loading data from {data}")

    load(validate(extract()))

    batch_ingestion()