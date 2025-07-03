class ConnectFourGame:
    def __init__(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]  # 6x7 board
        self.current_player = 1

    def play_turn(self, column):
        # Add logic to drop piece and switch player
        return {
            "board": self.board,
            "next_player": self.current_player
        }
