from datetime import datetime
import pytz

#startValue는 심볼 첫 출시일에 획득할 수 있는 심볼 개수를 입력해야함
# ex) 도원경 - 10개

symbols = { #기본 설정
    "odium" : { #오디움
        "startValue" : 2067, #첫 심볼 개수
        "additionValue" : 0, #이벤트 심볼 개수
        "dailyValue" : 10, #일퀘 개수
        "releaseDate" : datetime.strptime('2023.06.15', '%Y.%m.%d'),
    },
    "shangrila" : { #도원경
        "startValue" : 11,
        "additionValue" : 0,
        "dailyValue" : 10,
        "releaseDate" : datetime.strptime('2023.06.15', '%Y.%m.%d'),
    },
    "arteria" : { #아르테리아
        "startValue" : 10,
        "additionValue" : 0,
        "dailyValue" : 10,
        "releaseDate" : datetime.strptime('2023.07.13', '%Y.%m.%d'),
    },
    "carcion" : { #카르시온
        "startValue" : 10,
        "additionValue" : 0,
        "dailyValue" : 10,
        "releaseDate" : datetime.strptime('2023.08.10', '%Y.%m.%d'),
    },
}

updates = [
    # ("shangrila", datetime.strptime('2023.06.15', '%Y.%m.%d'), 10), 
    # ("carcion", datetime.strptime('2023.06.14', '%Y.%m.%d'), 10),
]

asia_timezone = pytz.timezone("Asia/Seoul")
current_date = datetime.now(asia_timezone).date()

def update_addition_value(symbol, date, value):
    data = symbols.get(symbol)
    if data and current_date >= date.date() and current_date >= data['releaseDate'].date():
        data["additionValue"] += value

# Apply the updates
for symbol, date, value in updates:
    update_addition_value(symbol, date, value)