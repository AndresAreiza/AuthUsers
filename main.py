from typing import Union
from fastapi import FastAPI
import requests
from pydantic import BaseModel
from typing import Optional
import json
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename = 'authUsers.log',
    filemode='w'
)

app = FastAPI()

@app.get("/")
def getAuthUsers():
    data=''
    url = 'https://62ffa01534344b6431fdd472.mockapi.io/api/authUsers'
    response = requests.get(url, {}, timeout=5)
    data = json.loads(response.content)
    if data != '' and data != 'Not found':
            logging.info('GET method executed successfully')
            return {"authUsers": response.json()}
    else:
        logging.error('Failed to execute GET method')
        return {"HTTP status code 204: No Content"}

@app.get("/authUsers/internalId={internalId}")
def read_authUsers(internalId: str):
    url = 'https://62ffa01534344b6431fdd472.mockapi.io/api/authUsers'
    response = requests.get(url, {}, timeout=5)
    data = json.loads(response.content)
    wEncryptedToken = ''
    for usr in data:
        if usr['internalId'] == internalId:
            wEncryptedToken = usr['encryptedToken']    
    if wEncryptedToken != '' and wEncryptedToken != 'Not found':
        logging.info('GET method executed successfully')
        return {"encryptedToken": wEncryptedToken}
    else:
        logging.error('Failed to execute GET method')
        return {"HTTP status code 204: No Content"}
    