from app import db
from . import masterService
import logging
# import uuid

logger = logging.getLogger(__name__)

@masterService.before_request
def before_request():
    logger.info("Master Before request!")



@masterService.route("/")
def show():
    return {"Say":"Hi Master"}
    # return render_template("index2.html")

