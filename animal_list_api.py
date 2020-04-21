from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbanimal_list


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')
#
#
# ## API 역할을 하는 부분
# @app.route('/reviews', methods=['POST'])
# def write_review():
#     return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/animal', methods=['GET'])
def read_animal_list():
    animal_list = list(db.animal.find({},{'_id': False}))
    return jsonify({'result': 'success', 'animal_list': animal_list})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)