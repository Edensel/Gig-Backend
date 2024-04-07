from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


#initilization of app
app = Flask(__name__)
BASEDIR = os.path.join(os.path.dirname(__file__))

#Database connection
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(BASEDIR, 'gig.sqlite') #database name as well connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#init db
db = SQLAlchemy(app)

#init Marshmallow
ma = Marshmallow(app)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello Group 4'




if __name__ == '__main__':
    app.run(debug=True)