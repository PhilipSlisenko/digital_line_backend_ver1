#from connexion import request
from config import db
from models import Clerk, ClerkSchema
from flask import abort, request


def search():
    if request.args:
        clerks = Clerk.query.filter_by(**request.args).all()
    else:
        clerks = Clerk.query.all()
    clerk_schema = ClerkSchema(many=True)
    return clerk_schema.dump(clerks).data, 200


def post():
    data = request.get_json()
    clerk = Clerk.query \
        .filter(Clerk.clerk_id == data['clerk_id']) \
        .first()
    if clerk is not None:
        abort(409, "Clerk with id {} already exists".format(data['clerk_id']))

    new_clerk = Clerk(name=data['name'])
    db.session.add(new_clerk)
    db.session.commit()

    clerk_schema = ClerkSchema()
    return clerk_schema.dump(new_clerk).data, 201


def get(clerk_id):
    clerk = Clerk.query.filter(Clerk.clerk_id == clerk_id).first()

    if not clerk:
        abort(404, "Clerk with id {} was not found".format(clerk_id))

    clerk_schema = ClerkSchema()
    return clerk_schema.dump(clerk).data, 200
