from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbmusicdiary

@app.route('/login')
def loginwname():
    return render_template('sample.html')


@app.route('/showcookie')
def showcookie():
    return render_template('sample2.html')

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/record')
def record():
    return render_template('record.html')

@app.route('/checkrecord')
def checkrecord():
    return render_template('check-record.html')

@app.route('/satisfylist')
def emotionsatisfy():
    return render_template('musicByEmotionSatisfy.html')

@app.route('/happylist')
def emotionhappy():
    return render_template('musicByEmotionHappy.html')

@app.route('/lovelylist')
def emotionlovely():
    return render_template('musicByEmotionLovely.html')

@app.route('/unsatisfylist')
def emotionunsatisfy():
    return render_template('musicByEmotionUnsatisfy.html')

@app.route('/sadlist')
def emotionsad():
    return render_template('musicByEmotionSad.html')

@app.route('/angrylist')
def emotionangry():
    return render_template('musicByEmotionAngry.html')


# API 역할 부분

@app.route('/record', methods=['POST'])
def write_record():
    date_receive = request.form['date']
    feel_receive = request.form['feel']
    title_receive = request.form['musicTitle']
    artist_receive = request.form['musicArtist']
    diary_receive = request.form['diary']

    music_diary = {
        'date': date_receive,
        'feel': feel_receive,
        'music_title': title_receive,
        'music_artist': artist_receive,
        'diary': diary_receive
    }

    db.music_diary.insert_one(music_diary)
    return jsonify({'result': 'success', 'msg': '저장 완료!'})

@app.route('/checkrecorded', methods=['GET'])
def read_record():
    records = list(db.music_diary.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'records': records})

##삭제 api
@app.route('/checkrecord/delete', methods=['POST'])
def delete_record():
    title_receive = request.form.get('music_title')
    print(title_receive)
    db.music_diary.delete_one({'music_title': title_receive})
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
