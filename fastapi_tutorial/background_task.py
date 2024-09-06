from fastapi import BackgroundTasks, FastAPI, Depends
from typing import Annotated, Union

app = FastAPI()

'''
def write_notification(email:str, message=""):
    with open('log.txt', mode='w') as email_file:
        content = f'notification for {email}: {message}'

@app.post('/send-notification/{email}')
async def send_notification(email:str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {'message': "Notification sent in the background"}
'''

# 의존성 주입

def write_log(message:str):
    with open('log.txt', mode='a') as log:
        log.write(message)
        
def get_query(background_tasks: BackgroundTasks, q: Union[str, None] = None):
    if q:
        message = f'found query: {q} \n'
        background_tasks.add_task(write_log, message)
    return q

@app.post('/send-notification/{email}')
async def send_notification(
    email:str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(get_query)]
):
    message = f'message to {email}\n'
    background_tasks.add_task(write_log, message)
    return {'message': 'Message sent'}