import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbanimal_list


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.animal.go.kr/front/awtis/protection/protectionList.do?totalCount=6293&pageSize=10&menuNo=1000000060&&page=1', headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

information = soup.select('#searchList > div > ul > li')


for info in information:
    info_img = info.select('div.photo > div > a ')
    info_list =info.select('div.txt > dl ')

    img = info.select_one('div.photo > div.thumbnail > a > img')

    # img_url = img['src']
    #
    # img = info.find('img').attrs('image-src')

    # print(img['src'])
    for inf in info_list:
        a_tag = inf.select_one('dt')
        a_info = inf.select_one('dd')

        if a_tag is not None:
            title = a_tag.text
            infom = a_info.text

            doc = {
                # 'img': img_url,
                'title': title,
                'infom': infom
            }
            db.animal.insert_one(doc)

# all_animal =list(db.animal.find())
# for animal in all_animal:
#      print(animal)

