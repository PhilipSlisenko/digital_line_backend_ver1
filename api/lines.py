from connexion import request
from config import db
from models import Line, LineSchema
from flask import abort


def search():
    if request.args:
        lines = Line.query.filter_by(**request.args).all()
    else:
        lines = Line.query.all()
    line_schema = LineSchema(many=True)
    return line_schema.dump(lines).data, 200


def post():
    data = request.get_json()
    line = Line.query \
        .filter(Line.line_id == data['line_id']) \
        .first()
    if line is not None:
        abort(409, "Line with id {} already exists".format(data['line_id']))

    new_line = Line(name=data['name'])
    db.session.add(new_line)
    db.session.commit()

    line_schema = LineSchema()
    return line_schema.dump(new_line).data, 201


def get(line_id):
    line = Line.query.filter(Line.line_id == line_id).first()

    if not line:
        abort(404, "Line with id {} was not found".format(line_id))

    line_schema = LineSchema()
    return line_schema.dump(line).data, 200
