from flask import Flask
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from api import config

def app_create():
    app = Flask(__name__)
    app.config.from_object(config.configs['development'])
    return app