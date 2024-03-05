# file : p65_flaskApp.py
# desc : 플라스크 웹 서버

'''
> pip install Flask
'''
from flask import Flask, render_template

app = Flask(__name__)   # 현재의 모듈로 Flask 앱을 만듦

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/unit')
def testPage1():
    return render_template('unit.html')

@app.route('/naver')
def testPage2():
    return render_template('register.html')

def main():
    app.run(debug=True, port=80)    # port=80은 기본 포트라 생략 가능, 80이 아닌 수는 직접 입력해줘야 함

if __name__ == '__main__':
    main()