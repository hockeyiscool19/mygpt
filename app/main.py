"""
Functions of this API
1. Reading emails, sending emails, getting email addresses, adding emails, getting rid of emails, changing emails
2. Writing coverletter, updating template
"""


from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime, timedelta
import asyncio
import signal



from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from app.utils.gmail import GMAIL
from app.utils.firebase import FIRE
import os


load_dotenv()



app = FastAPI()



last_request_time = datetime.now()

@app.middleware("http")
async def update_last_request_time(request: Request, call_next):
    global last_request_time
    last_request_time = datetime.now()
    response = await call_next(request)
    return response

def shutdown_server():
    os.kill(os.getpid(), signal.SIGINT)

async def check_inactivity():
    global last_request_time
    idle_time = timedelta(minutes=5)
    while True:
        print("Checking activity")
        await asyncio.sleep(10)  
        if datetime.now() - last_request_time > idle_time:
            print("Shutting down due to inactivity.")
            shutdown_server()

loop = asyncio.get_event_loop()
loop.create_task(check_inactivity())


@app.get("/")
def read_root():
    return {"Hello": "Welcome to Jordan's API"}


"""
Emails
"""

@app.get("/emails/get_emails")
def get_emails(start_date, end_date):
    """
    Dates formatted as strings: YYYY/MM/DD
    Sample parameters: 2023/10/11,2023/10/12 
    """
    emails = GMAIL.read_emails_in_timeframe(start_date, end_date)
    return emails


@app.get("/emails/read_email")
def read_email(id):
    """
    Reads the email given an id
    Args:
        id (str): The id of an email.
    """
    emails = GMAIL.view_email_contents(id)
    return emails


@app.get("/emails/send_email")
def send_email(subject, body, recipients):
    """
    Sends an email message.
        Args:
            subject (str): The subject of the email message.
            body (str): The body text of the email message.
            recipients (str): A list of recipient email addresses. Separated by space and

        Returns:
            Sent Message.
        Sample args:
            subject = "Hello"
            body = "World"
            recipients = "jordaneisenman@gmail.com, person2@example.com"
            GMAIL.send_email(subject, body, recipients)
    """
    recipients = recipients.replace(" ", "")
    recipients = recipients.split(",")
    print(recipients)
    try:
        GMAIL.send_email(subject, body, recipients)
        return "Successfully Sent"
    except Exception as e:
        return f"Error: {e}"
    
# @app.post("emails/get_addresses")
# def get_addresses(name, ):
#     pass
