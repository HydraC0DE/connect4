from flask import Blueprint, render_template, jsonify

game = Blueprint("game", __name__)

@game.route("/game")
def game_page():
    return render_template("game.html")

@game.route("/game/state")
def game_state():
    # dummy board
    dummy_board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0],
        [0, 2, 1, 1, 2, 0, 0],
        [0, 1, 2, 1, 1, 2, 0],
        [0, 0, 0, 2, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    current_player = "YELLOW"
    return jsonify(board=dummy_board, current_player=current_player)