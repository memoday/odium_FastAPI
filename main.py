from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()
# app.mount("/", StaticFiles(directory="public", html = True), name="static")


@app.get("/")
async def root():
    testNum = datetime.now()
    return {"date": testNum}

