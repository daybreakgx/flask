from flask import render_template, Blueprint, request
from app.util.log import logger

web_bp = Blueprint("web", __name__, template_folder="templates", static_folder="static")

@web_bp.route('/<user>')
def index(user):
    return render_template('index.html', user=user)

@web_bp.before_request
def before_req():
    logger.info("%s method, path %s from %s, args:%s" % \
                (request.method, request.full_path, request.remote_addr, request.data))
