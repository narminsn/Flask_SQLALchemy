from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://database_user:testing12345@localhost:5432/database_name'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:shadyshady@localhost:5432/mydb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)