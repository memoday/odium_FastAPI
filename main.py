from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from pytz import timezone
import math
import symbol_dict
import json
from pydantic import BaseModel, ValidationError

app = FastAPI()
# app.mount("/", StaticFiles(directory="public", html = True), name="static")

origins = [
    "https://odium.kr",  # Replace with the domain of your client-side code
    "http://127.0.0.1:5502",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

def getSymbolData(updateValue):
    result = {
        'authenticForce' : 220, #세르니움, 아르크스 만렙 적용
    }

    #기본 데이터
    today = datetime.now(timezone('Asia/Seoul')).strftime('%Y.%m.%d')
    today = datetime.strptime(today,'%Y.%m.%d')

    maxLevel = [0, 29, 76, 141, 224, 325, 444, 581, 736, 909, 1100]

    #심볼값 계산
    for symbolName in symbol_dict.symbols.keys():
        symbol_data = symbol_dict.symbols[symbolName]

        startValue = symbol_data["startValue"]
        additionValue = symbol_data["additionValue"]
        dailyValue = symbol_data["dailyValue"]
        releaseDate = symbol_data["releaseDate"]
        currentLevel = 0

        #일퀘 개수 추가
        days = today - releaseDate
        dailyCount = dailyValue * days.days
        if dailyCount < 0:
            dailyCount = 0
        
        #현재 심볼값
        currentValue = startValue + additionValue + dailyCount + updateValue

        if today == releaseDate:
            currentValue = startValue
        if today < releaseDate:
            currentValue = 0

        #누적 심볼 성장치
        currentCulmativeValue = currentValue

        #현재 심볼 레벨
        while(currentValue > maxLevel[currentLevel]):
            currentValue = currentValue - maxLevel[currentLevel]
            currentLevel += 1

        #현재 레벨 최대 개수
        currentLevelMaxValue = maxLevel[currentLevel]

        #현재 어센틱포스
        authenticForce = currentLevel*10
        result['authenticForce'] += authenticForce

        #레벨 업까지 남은 개수
        countsToNextLevel = currentLevelMaxValue - currentValue

        #레벨 업까지 남은 일수
        daysToNextLevel = math.ceil(countsToNextLevel/symbol_data["dailyValue"])

        #레벨 업 날짜
        dateToNextLevel = today + timedelta(days=daysToNextLevel)
        dateToNextLevel = datetime.strftime(dateToNextLevel,'%Y.%m.%d')

        result[symbolName] = {}
        symbols = result[symbolName]

        symbols["currentLevel"] = currentLevel
        symbols["currentCulmativeValue"] = currentCulmativeValue
        symbols["currentValue"] = currentValue
        symbols["currentLevelMaxValue"] = currentLevelMaxValue
        symbols["countsToNextLevel"] = countsToNextLevel
        symbols["daysToNextLevel"] = daysToNextLevel
        symbols["dateToNextLevel"] = dateToNextLevel

    return result

@app.get("/")
async def root():
    symbolData = getSymbolData(0)
    json_str = json.dumps(symbolData, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')

class additionValue(BaseModel):
    counts: int
    symbolName : str

@app.post("/calculator/")
async def calculate(additionValue: additionValue):
    try:
        counts = additionValue.counts
        symbolData = getSymbolData(counts)
        symbolData = symbolData[additionValue.symbolName]
        json_str = json.dumps(symbolData, indent=4, default=str)
        return Response(content=json_str, media_type='application/json')
    except Exception as e:
        print('error')

#POST ex) {"symbolName":"odium","counts":500}