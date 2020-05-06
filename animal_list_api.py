from flask import Flask, render_template, jsonify, request
import random
app = Flask(__name__)

from pymongo import MongoClient


# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbanimal_list


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')
#

randomNum = '';

# 이름이 없는 동물 조회
@app.route('/need_naming', methods=['GET'])
def need_naming():
    NoNames = list(db.animal_ko.find({'이름': '새 이름을 지어주세요 '}, {'_id': False}))
    NoName_A = random.choice(NoNames)

    # 공고번호만 db.naming_ko 에 넣어주기
    # randomNum = NoName_A['공고번호']
    # doc={}
    # doc['공고번호'] = randomNum
    # db.naming_ko.insert_one(doc)

    return jsonify({'result': 'success', 'NoName_A': NoName_A})


# # 이름짓기
@app.route('/naming', methods=['POST'])
def A_naming():

    ID_receive = request.form['ID_give']
    newName_receive = request.form['newName_give']
    mean_receive = request.form['mean_give']
    like = 1
    num_receive = request.form['num_give']

    newName = {
        '공고번호' : num_receive,
        'ID': ID_receive,
        'newName': newName_receive,
        'mean': mean_receive,
        'like' : like,

    }

    db.naming_ko.insert_one(newName)
    return jsonify({'result': 'success', 'msg': '이름 추가 완료!'})

# # 이름 후보 조회
@app.route('/naming_list', methods=['GET'])
def naming_list():
    naming_list = list(db.naming_ko.find({}, {'_id': False}).sort('like', -1))

    return jsonify({'result': 'success', 'naming_list': naming_list})

# 동물 조회
@app.route('/animal_ko', methods=['GET'])
def read_animal_list():
    animal_list = list(db.animal_ko.find({},{'_id': False}))
    return jsonify({'result': 'success', 'animal_list': animal_list})

#좋아요
@app.route('/like', methods=['POST'])
def like():
    ID_receive = request.form['ID_give']

    IDname = db.naming_ko.find_one({'ID': ID_receive})
    like = IDname['like'] + 1
    db.naming_ko.update_one({'ID': ID_receive}, {'$set': {'like': like}})

    return jsonify({'result': 'success', 'msg': '이름 추천 성공!'})

if __name__ == '__main__':
    # app.run('0.0.0.0', port=5000, debug=True)
    app.run('localhost', port=5000, debug=True)