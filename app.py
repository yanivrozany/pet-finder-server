from flask import Flask,jsonify
from flask_restful import Api,Resource, reqparse
from src import petFinderHelper
from flask_cors import CORS
import time
app = Flask(__name__)
api = Api(app)
CORS(app)

# populate golden retriver list 
pf= petFinderHelper.PetFinderAPI()
doglist,lastupdate = pf.findGoldenRetriver()

@app.route("/")
@app.route("/api/v1/dogs/findgoldenretriver/")
def get():
	global lastupdate
	doupdate,updated = pf.updateData(lastupdate)
	lastupdate = updated
	if (doupdate) :
		doglist,lastupdate = pf.findGoldenRetriver()
	return jsonify(doglist),200
	

app.run(debug=True)
