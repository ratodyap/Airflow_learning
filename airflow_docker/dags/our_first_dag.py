
from datetime import datetime,timedelta

from airflow import DAG

from airflow.operators.bash_operator import BashOperator

default_args = {
    "owner":"vn5705j",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

with DAG(

    dag_id = "our_first_dag_v1",
    default_args = default_args,
    description = "This is our first DAG",
    schedule_interval = "@daily",
    start_date = datetime(2021, 2, 1,2)
) as dag:
    
    task1 = BashOperator(
        task_id = "first_task",
        bash_command = "echo 'Hello World!' This is the first Task"
    )

    task2 = BashOperator(
        task_id = "second_task",
        bash_command = "echo Second task will run after first task"
    )

    task1.set_downstream(task2)