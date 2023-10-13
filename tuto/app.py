from flask import Flask
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = "bcc090e2-26b2-4c16-84ab-e766cc644320"

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