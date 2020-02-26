from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_albuns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

# @app.route('/<int:numero1>/<int:numero2>', methods=['GET'])
# def index(numero1, numero2):
#     soma = numero1 + numero2
#     return 'retornando soma de n1 e n2 : {}'.format(soma)

from album_api.view import main
