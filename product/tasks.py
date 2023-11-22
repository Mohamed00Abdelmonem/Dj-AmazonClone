# tasks.py
from celery import shared_task
import time


@shared_task
def send_emails():
    for x in range(10):
        time.sleep(3)
        # Your email sending code goes here
        print(f"Sending email {x}")
