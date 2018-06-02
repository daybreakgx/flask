from flask import render_template, Blueprint

web_bp = Blueprint("web", __name__, template_folder="templates", static_folder="static")

@web_bp.route('/')
def index():
    return render_template('index.html')

