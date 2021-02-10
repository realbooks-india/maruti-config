from flask import Blueprint


reportService = Blueprint('report', __name__, template_folder='templates')

from . import controller  # noqa:E401
from app.report.sync_status import controller  # noqa:E401
