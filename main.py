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

@app.get("/naver")
def naver():
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

@app.get("/inflearn")
def inflearn():
    url = 'https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%A4%EC%9A%A9%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8'
    response = requests.get(url)
    bsObject = bs(response.text, 'html.parser')

    title = bsObject.find('h2',class_='cd-header__title').get_text()
    image = bsObject.find('div',class_='cd-header__thumbnail').find('img')['src']
    contents = bsObject.find('p',class_='cd-body__description').get_text()

    return {
        "page" : "inflearn",
        "title" : title,
        "imagePath" : image,
        "contents" : contents,
        "link" : url
    }
