from flask import Blueprint, render_template

main = Blueprint("main", __name__)


#controllers
@main.route("/")
def index():
    return render_template("index.html")

@main.route("/test")
def test():
    return render_template("test.html")


game = Blueprint("game", __name__)

@game.route("/game")
def game_page():
    return render_template("game.html")