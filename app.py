import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbanimal_list


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.animal.go.kr/front/awtis/protection/protectionList.do?totalCount=6293&pageSize=10&menuNo=1000000060&&page=2', headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

information = soup.select('#searchList > div > ul > li')


for info in information:
    info_img = info.select('div.photo > div > a ')
    info_list =info.select('div.txt > dl ')

    img = info.select_one('div.photo > div > a')

    if img is None:
        continue
    img_href = 'https://www.animal.go.kr/' + img['href']

    doc = {}
    doc['img_url'] = img_href
    name = '새 이름을 지어주세요 '
    is_insert = False
    for inf in info_list:
        title = inf.select_one('dt')
        desc = inf.select_one('dd')

        if title is not None:
            is_insert = True

            doc['이름'] = name
            doc[title.text] = desc.text

    if is_insert:
        db.animal_ko.insert_one(doc)

# all_animal =list(db.animal.find())
# for animal in all_animal:
#      print(animal)
