from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from pytz import timezone

app = FastAPI()
# app.mount("/", StaticFiles(directory="public", html = True), name="static")


@app.get("/")
async def root():
    testNum = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
    return {"date": testNum}

