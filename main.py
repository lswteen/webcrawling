# main.py
import requests
from fastapi import FastAPI # FastAPI 모듈 가져오기
from bs4 import BeautifulSoup as bs

app = FastAPI() # 객체 생성

@app.get("/") # Route Path
def test_index():

    # Json 타입으로 값 반환
    return {
	    "Python": "Framework",
	}

@app.get("/something")
def something():
    return {
        "Something": "Page",
    }

@app.get("/weba")
def web_a():
    url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
    response = requests.get(url)
    answer = ''
    if response.status_code == 200:
        html = response.text
        soup = bs(html, 'html.parser')
        answer = soup
    else:
        answer = response.status_code
    return {
        "html" : print(answer)
    }