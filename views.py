''' Flask Extension '''
def init_app(app):
    @app.route("/")
    def index():
        return "hello coders"

    @app.route("/about")
    def about():
        return "delivery 2020"