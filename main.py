from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import socket

app = FastAPI()
# app.mount("/", StaticFiles(directory="public", html = True), name="static")


@app.get("/")
async def root():
    testNum = datetime.now()
    myIp = socket.gethostbyname(socket.gethostname())
    return {"date": testNum,"IP": myIp}

