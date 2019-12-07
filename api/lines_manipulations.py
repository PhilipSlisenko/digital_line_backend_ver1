from models import (
    Client, ClientSchema,
    Line, LineSchema,
    Clerk, ClerkSchema,
    LineClientLink,
)
from flask import abort
from config import db


def add_client_to_line(line_id, client_id):
    line = Line.query.filter_by(line_id=line_id).first()
    client = Client.query.filter_by(client_id=client_id).first()

    if not all((line, client)):  # true if any of objects is None
        abort(404, "No such line or client")

    # line order number to give to this client
    number_to_give = line.number_for_new_client
    line.number_for_new_client += 1
    line.people_in_line += 1
    line.clients.append(client)
    line_client_link = LineClientLink.query \
        .filter_by(line_id=line_id, client_id=client_id) \
        .first()
    line_client_link.client_place_in_line = number_to_give
    # db.session.add(client)
    db.session.add(line)
    # db.session.commit()
    db.session.add(line_client_link)
    db.session.commit()
    line_schema = LineSchema()
    return line_schema.dump(line).data, 200


def add_clerk_to_line(line_id, clerk_id):
    line = Line.query.filter_by(line_id=line_id).first()
    clerk = Clerk.query.filter_by(clerk_id=clerk_id).first()
    if not all((line, clerk)):  # true if any of objects is None
        abort(404, "No such line or clerk")
    line.clerks.append(clerk)
    db.session.add(line)
    db.session.commit()
    line_schema = LineSchema()
    return line_schema.dump(line).data, 200
