from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.main import main
    from .routes.game import game

    app.register_blueprint(main)
    app.register_blueprint(game)

    return app