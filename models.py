from config import db
from config import ma
print('models were touched')

### DB Models ###


class Line(db.Model):
    line_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    clerks = db.relationship(
        'Clerk', secondary='line_clerk_link', backref='lines')
    clients = db.relationship(
        'Client',
        secondary='line_client_link',
        backref='lines',
    )
    # how many people in particular line
    people_in_line = db.Column(db.Integer, default=0)
    # each client has their number, which determines place in line
    # number to give to a new client in line
    number_for_new_client = db.Column(db.Integer, default=1)
    # number of client who will be served next
    next_client_to_serve = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<Line {}>'.format(self.name)


class Clerk(db.Model):
    clerk_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Clerk {}>'.format(self.name)


class Client(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def notify_me(message: str):
        pass

    def __repr__(self):
        return '<Client {}>'.format(self.name)


class LineClerkLink(db.Model):
    line_id = db.Column(db.Integer, db.ForeignKey(
        'line.line_id'), primary_key=True)
    clerk_id = db.Column(db.Integer, db.ForeignKey(
        'clerk.clerk_id'), primary_key=True)


class LineClientLink(db.Model):
    line_id = db.Column(db.Integer, db.ForeignKey(
        'line.line_id'), primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey(
        'client.client_id'), primary_key=True)
    client_place_in_line = db.Column(db.Integer)


# line_client = db.Table('line_client',
#                        db.Column('line_id', db.Integer,
#                                  db.ForeignKey('line.line_id')),
#                        db.Column('client_id', db.Integer,
#                                  db.ForeignKey('client.client_id')),
#                        db.Column('client_place_in_line', db.Integer)
#                        )

### Marshmallow Schemas ###

class LineSchema(ma.ModelSchema):
    class Meta:
        model = Line
        sqla_session = db.session


class ClerkSchema(ma.ModelSchema):
    class Meta:
        model = Clerk
        sqla_session = db.session


class ClientSchema(ma.ModelSchema):
    class Meta:
        model = Client
        sqla_session = db.session


### App Models ###


db.create_all()

# class Client():
#     def __init__(self, id: str):
#         self.id: str = id
#         self.lines: List[Line] = []

#     def get_in_line(self, line: 'Line'):
#         line.add_client(self)

#     def short_form(self):
#         return self.id

#     def __str__(self):
#         return "I am client {} and I am in these lines: {}".format(self.id, list(map(lambda x: x.short_form(), self.lines)))


# class Clerk():
#     pass


# class Line():
#     def __init__(self, id: str):
#         self.id: str = id
#         self.clients: List[Client] = []

#     def add_client(self, client: Client):
#         if client not in self.clients:
#             self.clients.append(client)
#         print("Adde client {} to line {}".format(client, self))

#     def short_form(self):
#         return self.id

#     def notify_clients(self):
#         # get them from db
#         # notify I changed
#         pass

#     def __str__(self):
#         return "I am line {} and I have these clients: {}".format(self.id, list(map(lambda x: x.short_form(), self.clients)))


# class LinesManager():
#     def get_all_lines():
#         pass
