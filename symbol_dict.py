from datetime import datetime

#startValue는 심볼 첫 출시일에 획득할 수 있는 심볼 개수를 입력해야함
# ex) 도원경 - 10개

symbols = { #기본 설정
    "odium" : { #오디움
        "startValue" : 742, #첫 심볼 개수
        "additionValue" : 380, #이벤트 심볼 개수
        "dailyValue" : 5, #일퀘 개수
        "releaseDate" : datetime.strptime('2022.12.09', '%Y.%m.%d'),
    },
    "shangrila" : { #도원경
        "startValue" : 0,
        "additionValue" : 0,
        "dailyValue" : 10,
        "releaseDate" : datetime.strptime('2023.06.15', '%Y.%m.%d'),
    },
    "arteria" : { #아르테리아
        "startValue" : 0,
        "additionValue" : 0,
        "dailyValue" : 10,
        "releaseDate" : datetime.strptime('2023.07.13', '%Y.%m.%d'),
    },
    "carcion" : { #카르시온
        "startValue" : 0,
        "additionValue" : 0,
        "dailyValue" : 10,
        "releaseDate" : datetime.strptime('2023.08.10', '%Y.%m.%d'),
    },
}