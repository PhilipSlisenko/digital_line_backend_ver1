import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

print('######################config was ran')

basedir = os.path.abspath(os.path.dirname(__file__))
connexion_app = connexion.FlaskApp(__name__, specification_dir=basedir)

flask_app = connexion_app.app

flask_app.config['SQLALCHEMY_ECHO'] = True
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + \
    os.path.join(basedir, 'dline.db')
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)
ma = Marshmallow(flask_app)
