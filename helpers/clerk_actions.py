from config import db
from models import Clerk, Client, Line, LineClientLink
from flask import abort
from exceptions import ShouldntHappen
from api import lines


def call_next_client(clerk_id: int, line_id: int):
    line = Line.query.filter_by(line_id=line_id).first()
    clerk = Clerk.query.filter_by(clerk_id=clerk_id).first()

    if not all([line, clerk]):
        abort(404, "No such clerk or client")

    # Checking if clerk belongs to line
    if clerk not in line.clerks:
        abort(404, "Provided clerk does not belong to given line")

    # todo:
    #  - check if there are people in the line
    #  - notify client
    #  - update db
    order_number_who_to_notify = line.next_client_to_serve
    client_to_notify = LineClientLink.query \
        .filter_by(line_id=line_id, client_place_in_line=order_number_who_to_notify) \
        .first()

    if not client_to_notify:
        raise ShouldntHappen(
            "Client who should have been next in line wasn't found. Some bad business logic error.")

    client = Client.query.filter_by(client_id=client_to_notify).first()

    client.notify_me("You are next in line '{}'.".format(line.name))

    line.next_client_to_serve += 1
    line.people_in_line -= 1

    db.session.add(line)
    db.session.commit()


def notify_n_next(clerk_id: int, line_id: int, n: int = None, message: str = "Hello world!"):
    """If n not provided, then notifying all people in line"""

    line = Line.query.filter_by(line_id=line_id).first()
    clerk = Clerk.query.filter_by(clerk_id=clerk_id).first()

    if not all([line, clerk]):
        abort(404, "No such clerk or client")

    if clerk not in line.clerks:
        abort(404, "Provided clerk does not belong to given line")

    if n is not None:
        line_client_link = LineClientLink.query \
            .filter_by(line_id=line_id) \
            .order_by('client_place_in_line') \
            .limit(n) \
            .all()
    else:
        line_client_link = LineClientLink.query \
            .filter_by(line_id=line_id) \
            .order_by('client_place_in_line') \
            .all()

    clients = [Client.query.filter_by(
        client_id=lcl.client_id).first() for lcl in line_client_link]

    for client in clients:
        client.notify_me(message)


def close_line(clerk_id: int, line_id: int):
    line = Line.query.filter_by(line_id=line_id).first()
    message = "Line '{}'' has been closed.".format(line.name)
    notify_n_next(clerk_id, line_id, message=message)
    db.session.delete(line)
    db.session.commit()
