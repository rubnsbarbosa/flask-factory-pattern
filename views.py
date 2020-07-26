from flask import Flask


''' Flask Extension '''
def init_app(app: Flask):

    @app.route("/")
    def index():
        return "hello coders"

    @app.route("/about")
    def about():
        return "delivery 2020"
