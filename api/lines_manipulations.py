from models import Client, ClientSchema, Line, LineSchema, Clerk, ClerkSchema
from flask import abort
from config import db


def add_client_to_line(line_id, client_id):
    print("------------------------------------------------")
    print(f"{line_id=}\n{client_id=}")
    line = Line.query.filter_by(line_id=line_id).first()
    client = Client.query.filter_by(client_id=client_id).first()
    print("------------------------------------------------")

    print(f"{line=}\n{client=}")
    if not all((line, client)):  # true if any of objects is None
        abort(404, "No such line or client")
    line.clients.append(client)
    db.session.add(line)
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
