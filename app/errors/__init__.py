from flask import Blueprint

bp = Blueprint('Errors', __name__)

from app.errors import handlers