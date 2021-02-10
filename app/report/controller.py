from app import db
from . import reportService
from flask_jwt_extended import jwt_required
import logging
# import uuid

logger = logging.getLogger(__name__)

@reportService.before_request
def before_request():
    logger.info("Report Before request!")



@reportService.route("/")
@jwt_required
def show():
    return {"Say":"Hi Master"}
    # return render_template("index2.html")

