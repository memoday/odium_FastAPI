from datetime import datetime
import pytz

#startValue는 심볼 첫 출시일에 획득할 수 있는 심볼 개수를 입력해야함
# ex) 도원경 - 10개

symbols = { #기본 설정
    "odium" : { #오디움
        "startValue" : 2067, #첫 심볼 개수
        "additionValue" : 5, #이벤트 심볼 개수
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
        "startValue" : 11,
        "additionValue" : 0,
        "dailyValue" : 10,
        "releaseDate" : datetime.strptime('2023.07.13', '%Y.%m.%d'),
    },
    "carcion" : { #카르시온
        "startValue" : 11,
        "additionValue" : 0,
        "dailyValue" : 10,
        "releaseDate" : datetime.strptime('2023.08.10', '%Y.%m.%d'),
    },
}

# updates = [
#     ("shangrila", '2023.06.20', 40), #기본 탐험 일차 6
#     ("shangrila", '2023.06.22', 20), #기본 탐험 일차 8
#     ("shangrila", '2023.06.27', 40), #기본 탐험 일차 13
#     ("shangrila", '2023.06.29', 20), #기본 탐험 일차 15
#     ("shangrila", '2023.07.04', 40), #기본 탐험 일차 20
#     ("shangrila", '2023.07.06', 20), #기본 탐험 일차 22
#     ("shangrila", '2023.07.11', 40), #기본 탐험 일차 27 #아르테리아 7/13 출시
#     ("shangrila", '2023.07.18', 40), #기본 탐험 일차 34
#     ("shangrila", '2023.07.20', 20), #기본 탐험 일차 36
#     ("shangrila", '2023.07.22', 10), #기본 탐험 일차 38
#     ("shangrila", '2023.07.25', 40), #기본 탐험 일차 41
#     ("shangrila", '2023.07.27', 20), #기본 탐험 일차 43
#     ("shangrila", '2023.08.01', 40), #기본 탐험 일차 48
#     ("shangrila", '2023.08.03', 20), #기본 탐험 일차 50
#     ("shangrila", '2023.08.05', 10), #기본 탐험 일차 52
#     ("shangrila", '2023.08.08', 40), #기본 탐험 일차 55 #카르시온 8/10 출시
# ]

# asia_timezone = pytz.timezone("Asia/Seoul")
# current_date = datetime.now(asia_timezone).date()

# def update_addition_value(symbol, date, value):
#     data = symbols.get(symbol)
#     date = datetime.strptime(date,'%Y.%m.%d')
#     if data and current_date >= date.date() and current_date >= data['releaseDate'].date():
#         data["additionValue"] += value

# # Apply the updates
# for symbol, date, value in updates:
#     update_addition_value(symbol, date, value)