# 블로그 검색 예제 1 ================================================
import requests
import key
import json

BLOG_SEARCH_URL = "https://openapi.naver.com/v1/search/blog.json"

BLOG_SEARCH_PARAMS = {
    "query": "",
    "display": 10,
    "start": 1,
    "sort": "sim",
}

BLOG_HEADER = {
    "X-Naver-Client-Id": key.NAVER_CLIENT_ID,
    "X-Naver-Client-Secret": key.NAVER_CLIENT_SECRET,
}

search = input("검색어를 입력하세요 : ")

BLOG_SEARCH_PARAMS["query"] = search

res = requests.get(
    url=BLOG_SEARCH_URL,
    params=BLOG_SEARCH_PARAMS,
    headers=BLOG_HEADER,
)

print(res.json())

result = res.json()

# ensure_ascil 유니코드 문자를 올바르게 표기하기 위해 False
# indent json 파일을 보기 쉽게 포맷팅 (보통 4를 사용함)

with open("result.json", "w") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

# ======================================================
