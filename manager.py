import flask_script
from app import create_app
import sys

if __name__ == "__main__":
    app = create_app()

    manger = flask_script.Manager(app)
    manger.run()