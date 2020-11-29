from flask import Flask

# Faskのインスタンスを作成
app = Flask(__name__)

# ルーティングの指定
@app.route('/')
def index():
    return "じゃんけんアプリ"

@app.route('/guu')
def guu():
    return "ぐー"

# デバッグモードでサーバを起動させる
#app.run(debug=True)
app.run(host='0.0.0.0', port=3000)
