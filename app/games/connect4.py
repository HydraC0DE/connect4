from enum import Enum

class Player(Enum):
    RED = 2
    YELLOW = 1

class Connect4:
    ##6rowsx7columns board
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = Player.YELLOW ##yellow goes first according to connect4 rules
        self.move_count = 0
        self.game_over = False 

    def make_move(self, column):
        if getattr(self, "game_over", False):
            raise ValueError("Game is already over.")
        
        # Drop piece into column
        # Return (row, col) of move or raise error if full
        if column < 7 and column>-1:
            if self.board[0][column] != 0:
                raise ValueError("Column is full")            
            for row in range(5,-1,-1): ##iterating "upwards"
                if self.board[row][column] == 0:
                    self.board[row][column] = self.current_player.value
                    self.move_count += 1
                    if self.is_terminal_win(row, column, self.current_player.value):
                        self.finalizeMatchWin(self.current_player) ##give back winner information, maybe other stuff
                    elif self.is_terminal_draw():
                        self.finalizeMatchDraw()
                    else:
                        self.switch_player()
                    return row, column

    def is_terminal_win(self, current_row_pos, current_col_pos, colorValue):
        return (
        self.check_horizontal(current_row_pos, current_col_pos, colorValue)
        or self.check_vertical(current_row_pos, current_col_pos, colorValue)
        or self.check_diagonal1(current_row_pos, current_col_pos, colorValue)
        or self.check_diagonal2(current_row_pos, current_col_pos, colorValue)
        # dont check for draw we do that somewhere different
        )
    
    def is_terminal_draw(self):
        return self.move_count == self.rows * self.cols
            
    def finalizeMatchWin(self, winner_color):
        self.winner = winner_color
        self.game_over = True

    def finalizeMatchDraw(self):
        self.winner = None
        self.game_over = True

    def check_horizontal(self, current_row_pos, current_col_pos, colorValue):
        #check left then right and sum
        x=-1
        sameColorCount = 1
        while 0 <= current_col_pos + x < 7 and sameColorCount < 4:
            if self.board[current_row_pos][current_col_pos+x] == colorValue:
                sameColorCount+=1
                x-=1
            else:
                break

        x=1
        while 0 <= current_col_pos + x < 7 and sameColorCount < 4:
            if self.board[current_row_pos][current_col_pos+x] == colorValue:
                sameColorCount+=1
                x+=1
            else:
                break


        return sameColorCount >= 4

    def check_vertical(self, current_row_pos, current_col_pos, colorValue):
        y=1
        sameColorCount = 1
        while 0 <= current_row_pos + y < 6 and sameColorCount < 4:
            
            if self.board[current_row_pos+y][current_col_pos] == colorValue:
                sameColorCount+=1
                y+=1
            else:
                break
        
        
        return sameColorCount >= 4    


    def check_diagonal1(self, current_row_pos, current_col_pos, colorValue):
        sameColorCount = 1
        x = -1
        y = -1
        while 0 <= current_row_pos + y < 6  and 0 <= current_col_pos + x < 7 and sameColorCount < 4:
            if self.board[current_row_pos+y][current_col_pos+x] == colorValue:
                sameColorCount+=1
                y-=1
                x-=1
            else:
                break
        
        x = 1
        y = 1
        while 0 <= current_row_pos + y < 6  and 0 <= current_col_pos + x < 7 and sameColorCount < 4:
            if self.board[current_row_pos+y][current_col_pos+x] == colorValue:
                sameColorCount+=1
                y+=1
                x+=1
            else:
                break

        return sameColorCount >= 4

    def check_diagonal2(self, current_row_pos, current_col_pos, colorValue):
        sameColorCount = 1
        x,y = -1,1
        while 0 <= current_row_pos + y < 6  and 0 <= current_col_pos + x < 7 and sameColorCount < 4:
            if self.board[current_row_pos+y][current_col_pos+x] == colorValue:
                sameColorCount+=1
                y+=1
                x-=1
            else:
                break
        
        x,y = 1,-1
        while 0 <= current_row_pos + y < 6  and 0 <= current_col_pos + x < 7 and sameColorCount < 4:
            if self.board[current_row_pos+y][current_col_pos+x] == colorValue:
                sameColorCount+=1
                y-=1
                x+=1
            else:
                break

        return sameColorCount >= 4


    

    def switch_player(self):
        self.current_player = Player.RED if self.current_player == Player.YELLOW else Player.YELLOW

