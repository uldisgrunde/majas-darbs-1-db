from flask import Flask, render_template, request, json, jsonify

from flask_cors import CORS 
#CORS nepieciešams lai serverim var piekļūt skripti no citiem domēniem
#https://blog.ruanbekker.com/blog/2018/06/01/add-a-authentication-header-to-your-python-flask-app/
#https://flask-python-lessons.armandspucs.repl.co/data/css/main.css
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)
#failiem no data mapes var piekļūt šādi veidojot adresi

@app.route('/')
def home():
  return 'Sveiki datortehnikas uzskaites sistēmā!'

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

#@app.route('/data/room.json')
#def room():  
#  filer=open("data/room.json","r")  
#  telpas = filer.read()
#  filer.close()
#  return telpas

@app.route('/api/kabineti', methods=['GET'])
def kabineti():
    # atveram datni
    with open("data/room.json", "r") as f:
        # ielasām un pārvēršam par json
        telpas = json.loads(f.read())
        #print(telpas)
    # pārveidojam par string pirms atgriežam
    return jsonify(telpas)
  


#@app.route('/data/datorudb.json')
#def datorudb():  
#  filed=open("data/datorudb.json","r")  
#  tehnika=filed.read()
#  filed.close()
#  return tehnika

@app.route('/api/tehnika', methods=['GET'])
def datorudb():
    # atveram datni
    with open("data/datorudb.json", "r") as f:
        # ielasām un pārvēršam par json
        tehnika = json.loads(f.read())
        #print(tehnika)
    # pārveidojam par string pirms atgriežam
    return jsonify(tehnika)


#@app.route('/api/pievienot',methods=['POST'])
#def pievienot_tehniku():
  #datne="data/datorudb.json"
  #with open(datne, "r", encoding = "utf-8") as f:
  #  dati = json.loads(f.read())
  
  #garums = len(dati['dati'])-1
  #lid=dati["dati"][garums]['id']
  #jauna_tehnika=json.loads(request.data)
  #jauna_tehnika['id']=lid+1
  #dati["dati"].append(jauna_tehnika)
  #with open(datne, "w", encoding = "utf-8") as f:
  #  f.write(json.dumps(dati))
  #atbilde="elements pievienots"
  #return atbilde

@app.route('/api/pievienot',methods=['POST'])  
def pievienot_tehniku():
  datne="data/datorudb.json"
  with open(datne, "r", encoding = "utf-8") as f:
    dati = json.loads(f.read())
  lid=dati['lastId']
  lid=lid+1
  #garums = len(dati['dati'])-1
  #lid=dati["dati"][garums]['id']
  jauna_tehnika=json.loads(request.data)
  jauna_tehnika['id']=lid
  dati["dati"].append(jauna_tehnika)
  dati["lastId"]=lid
  with open(datne, "w", encoding = "utf-8") as f:
    f.write(json.dumps(dati))
  atbilde="elements pievienots"
  return atbilde  
  
@app.route('/tests')
def tests():
  datne="data/datorudb.json"
  with open(datne, "r", encoding = "utf-8") as f:
    dati = json.loads(f.read())
  
  gar=len(dati)
  x=dati['lastId']
  x1=str(x)
  return x1
   
  #x=dati.get("lastId")
  #x1=int(x)
  #return x1

@app.route('/api/dzest', methods = ['POST'])
def dzest(id):
  datne = "data/datorudb.json"
  with open(datne, "r", encoding = 'utf-8') as f:
    dati = json.loads(f.read())

  datneDzestie="data/dzestie.json"
  with open(datneDzestie, "r", encoding = 'utf-8') as fdz:
    dzestie = json.loads(fdz.read())
  
  jauniDati={}
  jauniDati['lastId']=dati['lastId']
  jauniDati["dati"] = []
  for ieraksti in dati:
    if str(ieraksts['id']) == id:
      print(id)
      jauniDati["dati"].append(ieraksts)
    else:
      dzestie.append(ieraksts)

  with open(datne, "w", encoding = "utf-8") as f:
    f.write(json.dumps(jauniDati))

  with open(datneDzestie, "w", encoding = "utf-8") as fdz:
    fdz.write(json.dumps(dzestie))

  return "1"
  
  
@app.route('/api/<id>/norakstit', methods = ['POST'])
def norakstit(id):
  datne = "data/datorudb.json"
  with open(datne, "r", encoding = 'utf-8') as f:
    dati = json.loads(f.read())
  datneDzestie="data/dzestie.json"
  with open(datneDzestie, "r", encoding = 'utf-8') as fdz:
    dzestie = json.loads(fdz.read())
  
  jauniDati={}
  jauniDati['lastId']=dati['lastId']
  jauniDati["dati"] = []
  for ieraksts in dati:
    if ieraksts['id'] == id:
      print(id)
      jauniDati["dati"].append(ieraksts)
    else:
      dzestie.append(ieraksts)


  with open(datne, "w", encoding = "utf-8") as f:
    f.write(json.dumps(jauniDati))

  with open(datneDzestie, "w", encoding = "utf-8") as fdz:
    fdz.write(json.dumps(dzestie))

  return "1"



@app.route('/api/delete', methods = ['POST'])
def izdzest():
  request_data = request.get_json()

  try:
    nid = int(request_data['id'])
    datne = "data/datorudb.json"
    with open(datne, "r", encoding = 'utf-8') as f:
      datim = json.loads(f.read())

    
    datnetuks = "data/datorudbtuks.json"
    with open(datnetuks, "r", encoding = 'utf-8') as ft:
      jauniDati = json.loads(ft.read())
    
    for ieraksts in datim['dati']:
      if ieraksts['id'] != nid:
        jauniDati['dati'].append(ieraksts)
    jauniDati['lastId']=datim['lastId']

    with open(datne, "w", encoding = "utf-8") as f:
      f.write(json.dumps(jauniDati))
      
    atbilde=1
  except: 
    atbilde=0

  return {'status':atbilde}

  
  app.run(host='0.0.0.0', port=8020,debug=True)
