from flask import Flask
 
app = Flask(__name__)
 
# 테스트 기능
@app.route('/hello') #url 요청이 들어오면 (무엇을 실행)어디로 보낼거야, 만든 앱에 헬로가 들어오면 밑 함수로 보낼거야
def hello_Flask():
    return 'Hello, Flask'
 
if __name__ == '__main__': #제일 처음 실행되는 영역이 밑이다. main이다.
    app.run( #app 실행
    host="0.0.0.0", #어디서든 실행
    port=7777, #포트
    debug=True) #오고가는 메세지 보여줘