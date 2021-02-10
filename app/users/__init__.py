from flask import Blueprint


usersService = Blueprint('users', __name__, template_folder='templates')

from . import controller  # noqa:E401
from app.users.users import controller  # noqa:E401
