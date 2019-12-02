import sys
from test import test1 as test
from connexion import request
from config import db
from models import Clerk


def search(qparam):
    print(f"{qparam=}")
    print(request.args)


def post():
    print(request.data)
    # new_clerk = Clerk(name=request.)
