from flask import render_template, Blueprint, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from app.util.log import logger
from app.controller.user_controller import checkUserExists, addUser

web_bp = Blueprint("web", __name__, template_folder="templates", static_folder="static")

class NameForm(FlaskForm):
    name = StringField('what is your name', validators=[Required()])
    submit = SubmitField('Submit')

@web_bp.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        if checkUserExists(form.name.data):
            flash('Happy to meet you again.')
        else:
            addUser(form.name.data)
            flash('Nice to meet you.')
        session['username'] = form.name.data
        return redirect(url_for('web.index'))
    return render_template('index.html', user=session.get('username'), form=form)

@web_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@web_bp.before_request
def before_req():
    logger.info("%s method url(%s) from %s, args: %s" % \
        (request.method, request.full_path, request.remote_addr, request.data))
