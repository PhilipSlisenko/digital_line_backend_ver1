#from connexion import request
from config import db
from models import Client, ClientSchema
from flask import abort, request


def search():
    if request.args:
        clients = Client.query.filter_by(**request.args).all()
    else:
        clients = Client.query.all()
    client_schema = ClientSchema(many=True)
    return client_schema.dump(clients).data, 200


def post():
    data = request.get_json()
    client = Client.query \
        .filter(Client.client_id == data['client_id']) \
        .first()
    if client is not None:
        abort(409, "Client with id {} already exists".format(
            data['client_id']))

    new_client = Client(name=data['name'])
    db.session.add(new_client)
    db.session.commit()

    client_schema = ClientSchema()
    return client_schema.dump(new_client).data, 201


def get(client_id):
    client = Client.query.filter(Client.client_id == client_id).first()

    if not client:
        abort(404, "Client with id {} was not found".format(client_id))

    client_schema = ClientSchema()
    return client_schema.dump(client).data, 200
