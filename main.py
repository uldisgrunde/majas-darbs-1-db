from flask import Flask, render_template, request, json

from flask_cors import CORS 
#CORS nepieciešams lai serverim var piekļūt skripti no citiem domēniem

app = Flask(__name__)

CORS(app)



#failiem no static mapes var piekļūt šādi veidojot adresi
#https://flask-python-lessons.armandspucs.repl.co/static/css/main.css

@app.route('/')
def home():
  return 'Sveika pasaule!...'


@app.route('/parametri')
def parametri():
  parametri = request.args
  print(parametri)
  action= request.args.get('action')
  print(action)
  return 'gaidu GET parametrus adresē'
  #parametrus var notestēt https://majas-darbs-1-db.uldisgrunde.repl.co/parametri?id=456&action=save

app.run(host='0.0.0.0', port=8020)

#meģina andrejs



#armands testē