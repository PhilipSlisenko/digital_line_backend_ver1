from config import db
from models import Clerk, Client, Line, LineClientLink
from api.lines_manipulations import add_client_to_line, add_clerk_to_line
from helpers.clerk_actions import call_next_client
import os
if os.path.exists('dline.db'):
    print("TTTTTTTTTTTTTTTRRRRRRRRRRRRRRUUUUUUUUUUUUEEEEEEEEEE")
    os.remove('dline.db')
db.create_all()
l1 = Line(name='line_1')
l2 = Line(name='line_2')
c1 = Client(name='client_1')
c2 = Client(name='client_2')
c3 = Client(name='client_3')
c4 = Client(name='client_4')
c5 = Client(name='client_5')
cle1 = Clerk(name="clerk_1")
cle2 = Clerk(name="clerk_2")
db.session.add_all([l1, l2, c1, c2, c3, c4, c5, cle1, cle2])
db.session.commit()
add_client_to_line(1, 1)
add_client_to_line(1, 2)
add_clerk_to_line(1, 1)
