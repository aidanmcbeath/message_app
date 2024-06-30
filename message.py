#!/c/Users/aidan/Documents/Projects/message/message.venv/Scripts/python.exe

from fastapi import FastAPI
import sqlalchemy
import sys
import os

# Add the parent directory to sys.path and importing secrets
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from message_app_artifacts.secrets import secret_variable

#Assigning secrets to variables for ease of access
mysql_user = secret_variable['mysql']['user']
mysql_pass = secret_variable['mysql']['password']

#API application logic
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World, this is the root of the API",
            "testonly": mysql_user}

@app.get("/getmessage")
async def get_message():
    return {"message": "Hello World"}

# @app.post("/post/{itemid}")
# async def post(itemid: str):
#     arg = itemid
#     return {"message": arg,
#             "type": "post"}

# @app.put("/put/{itemid}/{updatedValue}")
# async def put(itemid: str, updatedValue: str):
#     arg = itemid
#     val = updatedValue
#     return {"item": arg,
#             "oldvalue": "Test",
#             "newvalue": val