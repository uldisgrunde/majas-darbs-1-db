from flask import Flask, render_template, request, json, jsonify

from flask_cors import CORS 
#CORS nepieciešams lai serverim var piekļūt skripti no citiem domēniem

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)



#failiem no static mapes var piekļūt šādi veidojot adresi
#https://flask-python-lessons.armandspucs.repl.co/static/css/main.css

@app.route('/')
def home():
  return 'Sveika pasaule!...'

#uldis teste
@app.route('/dati/<jsonFile>', methods=['GET'])
def dati(jsonFile):
  #print(jsonFile)
  file="data/{}.json".format(jsonFile)
  #print(file)
  #return render_template("data/{}.json".format(jsons))
  with open(file, "r") as f:
  # ielasām un pārvēršam par json
    dati = json.loads(f.read())
  # pārveidojam par string pirms atgriežam
  return jsonify(dati)
  #return render_template(file)
#uldis beidz testet

@app.route('/parametri')
def parametri():
  parametri = request.args
  print(parametri)
  action= request.args.get('action')
  print(action)
  return 'gaidu GET parametrus adresē'
  #parametrus var notestēt https://majas-darbs-1-db.uldisgrunde.repl.co/parametri?id=456&action=save

app.run(host='0.0.0.0', port=8020,debug=True)

#meģina andrejs



#armands testē