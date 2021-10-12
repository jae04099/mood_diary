# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request, session, redirect, url_for, escape

app = Flask(__name__)
app.secret_key = "12341234"

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('mongodb+srv://jae04099:Lc0711zz@moodplaylist.n3ute.mongodb.net/test', 27017)
db = client.dbmusicdiary


@app.route('/signup')
def signup():
    return render_template("sign-up.html")


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


@app.route('/signup', methods=['POST'])
def add_personal_info():
    nickname_recieve = request.form['nickname']
    id_recieve = request.form['ID']
    pw_recieve = request.form['PW']

    person_info = {
        'nickname': nickname_recieve,
        'ID': id_recieve,
        'PassWord': pw_recieve
    }
    if nickname_recieve == '' or id_recieve == '' or pw_recieve == '':
        return jsonify({'result': 'error', 'msg': '빈칸이 없이 적어주세요'})
    else:
        db.person_info.insert_one(person_info)
        return jsonify({'result': 'success', 'msg': '가입되셨습니다.'})

 # 로그인 처리


@app.route('/', methods=['POST'])
def verified_login():
    entered_id = request.form['ID']
    entered_pw = request.form['PW']
    exist_info = db.person_info.find(
        {"ID": entered_id}, {"PassWord": entered_pw}).count()
    if exist_info >= 1:
        target_ID = db.person_info.find_one({'ID': entered_id})
        session['username'] = target_ID['nickname']
        # result = '%s' % escape(session["username"])
        return jsonify({'result': 'success', 'nickname': target_ID['nickname']})
    else:
        return jsonify({'result': 'error'})

@app.route('/record', methods=['POST'])
def write_record():
    nickname = request.cookies.get('UserName')
    date_receive = request.form['date']
    feel_receive = request.form['feel']
    title_receive = request.form['musicTitle']
    artist_receive = request.form['musicArtist']
    diary_receive = request.form['diary']

    music_diary = {
        'nickname' : nickname,
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

# 삭제 api


@app.route('/checkrecord/delete', methods=['POST'])
def delete_record():
    title_receive = request.form.get('music_title')
    db.music_diary.delete_one({'music_title': title_receive})
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


