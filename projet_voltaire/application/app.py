from flask import Flask, redirect
import json
from datetime import datetime, timedelta

app = Flask(__name__)

def get_dt():
	dtc_f = open("api.json", "r")
	dtc = json.load(dtc_f)
	return dtc

@app.route('/', methods=["post", "get"])
def main():
	dt=get_dt()
	if dt["did_i_click?"]:
		etat="<h1>Etat : Actif</h1>"
	else:
		etat="<h1>Etat : Inactif</h1>"
	last_time_up="<h1>"+dt["time"]+"</h1>"
	return '<form action="/ACCESS" method="post"><button>CHANGER</button></form><br>'+etat+"<br>"+last_time_up

@app.route("/api")
def api():
	return get_dt()

@app.route("/ACCESS", methods=["post"])
def ACCESS():
	val1=get_dt()
	val=val1["did_i_click?"]
	if val:
		val1["did_i_click?"]=False
		time=datetime.now().strftime("%H:%M")
	else:
		val1["did_i_click?"]=True
		time=str(datetime.now()+timedelta(hours=1))[11:16]
	val1["time"]=time
	fl = open("api.json", "w")
	json.dump(val1, fl)
	return redirect("/")


if __name__=="__main__":
	app.run(debug=True)