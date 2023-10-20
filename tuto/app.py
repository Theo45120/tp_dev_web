from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = "3b117cd7-bb11-4ff7-88b7-37e234f4d831"

import os.path
def mkpath (p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname ( __file__ ),
            p))
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy (app)


login_manager = LoginManager(app)