# 231015 5번째 파일입니다.
# flask 라이브러리 로드 #render_template는 html로 만들어진 코드를 화면에 덮어씌운다는 뜻
from flask import Flask, render_template

# Flask class 생성
# 해당 class에는 생성자함수 존재
# 입력값으로 파일의 이름이 필요.
# __name__:현재 파일의 이름(자동으로 파일 이름을 넣어줌)
app = Flask(__name__)

# 포트번호 설정
_port = 3000

# api 생성
# localhost: 3000

# 네비게이터 함수
# localhost:3000 / 요청시 바로 아래의 함수를 호출
@app.route("/")
def index():
    return render_template('index.html')

# localhost:3000/second 요청시 #3000까지는 내 컴퓨터라는 뜻이니까, 그 이후의 /second만 써주면 됨.
@app.route("/second")
def second():
    return render_template('second.html')




app.run(port = _port, debug=True)  #debug는 기본적으로 False로 두는 것이 좋다. 그런데 개발 단계에서는 True로 두는 게 편함.

# samplates라는 폴더 생성, index.html이라는 파일 생성