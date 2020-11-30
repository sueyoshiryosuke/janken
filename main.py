from flask import Flask, render_template
import random

# Faskのインスタンスを作成
app = Flask(__name__)

# ルーティングの指定（最初のページ）
@app.route('/')
def index():
  #index.hthlのテンプレートを設定する
  return render_template("index.html")

# ルーティングの指定（ぐうのとき）
@app.route('/guu')
def guu():
  #ロボットの出す手を決める
  #乱数を使う
  robot = random.randint(1,3)

  return render_template("guu.html", robot=robot)

# ルーティングの指定（ちょきのとき）
@app.route('/choki')
def choki():
  #ロボットの出す手を決める
  #乱数を使う
  robot = random.randint(1,3)

  return render_template("choki.html", robot=robot)

# ルーティングの指定（ぱあのとき）。未完


app.run(host='0.0.0.0')
