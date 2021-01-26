from flask import Blueprint


masterService = Blueprint('master', __name__, template_folder='templates')

from . import controller  # noqa:E401
from app.master.segmap import controller  # noqa:E401
from app.master.ledgermap import controller  # noqa:E401
from app.master.itemmap import controller  # noqa:E401
