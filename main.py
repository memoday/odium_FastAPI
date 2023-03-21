from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from pytz import timezone

app = FastAPI()
# app.mount("/", StaticFiles(directory="public", html = True), name="static")

def symbolCount():
    today = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d')
    today = datetime.strptime(today,'%Y-%m-%d')

    nowValue = 742
    i = 0
    maxLevel = [0, 29, 76, 141, 224, 325, 444, 581, 736, 909, 1100]
    nowLevel = i
    publishedDate = datetime.strptime('2022-12-09','%Y-%m-%d')

    difference = today - publishedDate
    
    dailyCount = difference.days * 5 #일퀘 심볼 개수
    addition = 180 #이벤트 심볼

    nowValue = nowValue + int(dailyCount) + addition

    while(nowValue > maxLevel[i]):
        nowValue = nowValue - maxLevel[i]
        i += 1
        nowLevel = i

    return nowLevel, nowValue

@app.get("/")
async def root():
    nowLevel, nowValue = symbolCount()
    testNum = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d')
    return {"nowLevel" : nowValue, "nowValue" : nowValue,"date": testNum}

