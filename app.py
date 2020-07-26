import views
from flask import Flask


def create_app():
    ''' Main Factory '''
    app = Flask(__name__)
    views.init_app(app)
    return app

