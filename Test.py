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
#
#
# soup = BeautifulSoup(data.text, 'html.parser')
#
# information = soup.select('#searchList > div > ul > li')
#
#
# for info in information:
#     info_img = info.select('div.photo > div > a ')
#     info_list =info.select('div.txt > dl ')
#
#     img = info.select_one('div.photo > div > a ')
#
#
#
#     if img is None:
#         continue
#     img_src = 'https://www.animal.go.kr/' + img['href']
#
#
#
#     print(img_src)
# naming_list = list(db.naming_ko.find({},{'_id':0}))
naming_list = list(db.naming_ko.find({}, {'_id': False}).sort('like', -1))
print(naming_list)
