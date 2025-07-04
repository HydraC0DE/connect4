from flask import Blueprint, render_template

game = Blueprint("game", __name__)

@game.route("/game")
def game_page():
    return render_template("game.html")
