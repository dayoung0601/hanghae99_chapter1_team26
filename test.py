from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


   test.py 수정 해보기


 뭐가 문제일까요.

