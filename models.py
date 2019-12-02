from config import db


class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    clerks = db.relationship('Clerk', secondary='line_clerk', backref='lines')
    clients = db.relationship(
        'Client', secondary='line_client', backref='lines')

    def __repr__(self):
        return '<Line {}>'.format(self.name)


class Clerk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Clerk {}>'.format(self.name)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Client {}>'.format(self.name)


line_clerk = db.Table('line_clerk',
                      db.Column('line_id', db.Integer,
                                db.ForeignKey('line.id')),
                      db.Column('clerk_id', db.Integer,
                                db.ForeignKey('clerk.id'))
                      )

line_client = db.Table('line_client',
                       db.Column('line_id', db.Integer,
                                 db.ForeignKey('line.id')),
                       db.Column('client_id', db.Integer,
                                 db.ForeignKey('client.id'))
                       )

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
