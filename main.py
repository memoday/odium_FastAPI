from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timedelta
from pytz import timezone
import math

app = FastAPI()
# app.mount("/", StaticFiles(directory="public", html = True), name="static")

def symbolCount():
    today = datetime.now(timezone('Asia/Seoul')).strftime('%Y.%m.%d')
    td = today
    today = datetime.strptime(today,'%Y.%m.%d')

    nowValue = 742
    i = 0
    maxLevel = [0, 29, 76, 141, 224, 325, 444, 581, 736, 909, 1100]
    nowLevel = i
    publishedDate = datetime.strptime('2022.12.09','%Y.%m.%d')

    difference = today - publishedDate
    
    dailyCount = difference.days * 5 #일퀘 심볼 개수
    addition = 180 #이벤트 심볼

    nowValue = nowValue + int(dailyCount) + addition

    while(nowValue > maxLevel[i]):
        nowValue = nowValue - maxLevel[i]
        i += 1
        nowLevel = i

    nowLevelMaxValue = maxLevel[i]
    countsToNextLevel = maxLevel[i] - nowValue
    daysToNextLevel = math.ceil(countsToNextLevel/5) #math.ceil 써야지 올림됨 임시!!
    dateToNextLevel = today + timedelta(days=daysToNextLevel)
    dateToNextLevel = datetime.strftime(dateToNextLevel,'%Y.%m.%d')

    global symbol
    symbol = {
        'date' : td,
        'currentLevel' : nowLevel,
        'currentValue' : nowValue,
        'currentLevelMaxValue' : nowLevelMaxValue,
        'countsToNextLevel' : countsToNextLevel,
        'daysToNextLevel' : daysToNextLevel,
        'dateToNextLevel' : dateToNextLevel,
    }

    return symbol

@app.get("/")
async def root():
    symbolCount()
    return {"date": symbol['date'],
            "currentLevel" : symbol['currentLevel'], 
            "currentValue" : symbol['currentValue'],
            "currentLevelMaxValue" : symbol['currentLevelMaxValue'],
            "countsToNextLevel" : symbol['countsToNextLevel'],
            "daysToNextLevel" : symbol['daysToNextLevel'],
            "dateToNextLevel" : symbol['dateToNextLevel'],
            }

