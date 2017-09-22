'''
T5 cargo generator
'''

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
