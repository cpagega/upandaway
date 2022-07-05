from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.AmadeusApiHandler import AmadeusApiHandler
#from api.UserApiHandler import UserApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/public')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')


#api.add_resource(UserApiHandler, '/flask/newUser')
api.add_resource(AmadeusApiHandler, '/flask/search')