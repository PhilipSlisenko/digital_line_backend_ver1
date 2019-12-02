import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from connexion.resolver import RestyResolver

basedir = os.path.abspath(os.path.dirname(__file__))
# Create the Connexion application instance
connexion_app = connexion.FlaskApp(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
flask_app = connexion_app.app

# Configure the SQLAlchemy part of the app instance
flask_app.config['SQLALCHEMY_ECHO'] = True
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + \
    os.path.join(basedir, 'dline.db')
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(flask_app)

# Initialize Marshmallow
ma = Marshmallow(flask_app)

connexion_app.add_api('swagger_small.yaml', resolver=RestyResolver('api'))

if __name__ == "__main__":
    connexion_app.run(debug=True)
