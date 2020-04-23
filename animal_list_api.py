from flask import Flask, render_template, jsonify, request
import random
app = Flask(__name__)

from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.dbanimal_list


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')
#
# #
# # 이름짓기
# @app.route('/naming_ko', methods=['POST'])
# def A_naming():
#     ID_receive = request.form['ID_give']
#     newName_receive = request.form['newName_give']
#     mean_receive = request.form['mean_give']
#
#     newName = {
#         'ID': ID_receive,
#         'newName': newName_receive,
#         'mean': mean_receive
#     }
#
#     db.naming_ko.insert_one(newName)
#     return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

# 이름이 없는 동물 조회
@app.route('/animal_ko', methods=['GET'])
def need_naming():
    NoNames = list(db.animal_ko.find({'이름': '새 이름을 지어주세요 '}, {'_id': False}))
    NoName_A = random.choice(NoNames)
    return jsonify({'result': 'success', 'NoName_A': NoName_A})

# 동물 조회
@app.route('/animal_ko', methods=['GET'])
def read_animal_list():
    animal_list = list(db.animal_ko.find({},{'_id': False}))
    return jsonify({'result': 'success', 'animal_list': animal_list})



if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)