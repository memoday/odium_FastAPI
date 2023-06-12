from datetime import datetime

#심볼 첫 출시날에 일일 퀘스트 진행 가능으로 startValue는 0이 될 수 없음

symbols = { #기본 설정
    "odium" : {
        "startValue" : 742, #첫 심볼 개수
        "additionValue" : 380, #이벤트 심볼 개수
        "dailyValue" : 5, #일퀘 개수
        "releaseDate" : datetime.strptime('2022.12.09', '%Y.%m.%d'),
    },
    "new" : {
        "startValue" : 0,
        "additionValue" : 0,
        "dailyValue" : 0,
        "releaseDate" : datetime.strptime('2023.05.01', '%Y.%m.%d'),
    },
}