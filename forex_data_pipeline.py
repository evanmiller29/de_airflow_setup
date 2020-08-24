from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "start_date": datetime(2019, 12, 4),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "youremail@host.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)


}