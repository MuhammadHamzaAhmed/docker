"""
Usage: __init__.py

Start flask api at port 5000
"""
from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
swagger = Swagger(app)
cors = CORS(app, origins=['*'])

app.secret_key = 'nets-x-map'
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@form_db:3306/FormDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# three line comment
app.config['SQLALCHEMY_BINDS'] = {
    'FormDB': 'mysql+pymysql://root:root123@form_db:3306/FormDB'
}

db = SQLAlchemy(app)
