import random


NUM_OF_COL = 7
NUM_OF_ROW = 6

PLAYER_1 = 1
PLAYER_2 = 2

GAME_STATUS_WIN = 1
GAME_STATUS_DRAW = -1
GAME_INCOMPLETE = 0
INVALID_MOVE = 2
COUNT_TO_WIN = 4

class ConnectFour(object):
    def __init__(self, num_of_col=NUM_OF_COL, num_of_row=NUM_OF_ROW, count_to_win=COUNT_TO_WIN):
        self.num_of_col = num_of_col
        self.num_of_row = num_of_row
        self.count_to_win = count_to_win
        row = [0] * num_of_col
        self.board = []
        for _ in range(NUM_OF_ROW):
            self.board.append(list(row))

    def move(self, player, col):
        print('Player {} dropped on column {}'.format(player, col))
        col_index = col - 1
        row_index = self.play(player, col_index)
        if row_index == -1:
            print("Invalid Move")
            return INVALID_MOVE

        game_status = self.check_game_status(player, row_index, col_index)
        print('Current Board:')
        self.draw_board()
        if game_status == GAME_STATUS_WIN:
            print('Game won by Player {}'.format(player))
        elif game_status == GAME_STATUS_DRAW:
            print('Game is draw')
        return game_status

    def play(self, player, col_index):
        if not self.is_move_possible(col_index):
            return -1

        for row_index in range(self.num_of_row-1, -1, -1):
            if self.board[row_index][col_index] == 0:
                self.board[row_index][col_index] = player
                return row_index

    def is_move_possible(self, col_index):
        # Invalid column
        if col_index < 0 or col_index >= self.num_of_col:
            return False

        # Column is already full
        if self.board[0][col_index] != 0:
            return False
        return True

    def draw_board(self):
        for i in range(self.num_of_row):
            row = []
            for j in range(self.num_of_col):
                if self.board[i][j] == PLAYER_1:
                    display = 'X'
                elif self.board[i][j] == PLAYER_2:
                    display = 'O'
                else:
                    display = '-'
                row.append(display)
            print('| {} |'.format(' | '.join(row)))

    def check_game_status(self, player, row_index, col_index):
        game_status = GAME_INCOMPLETE
        if self.row_win(player, row_index, col_index) or self.col_win(player, row_index, col_index) or \
            self.horizontal_win_down(player, row_index, col_index) or self.horizontal_win_up(player, row_index, col_index):
            game_status = GAME_STATUS_WIN
        elif self.is_game_draw():
            game_status = GAME_STATUS_DRAW
        return game_status

    def is_game_draw(self):
        for i in range(self.num_of_row):
            for j in range(self.num_of_col):
                if self.board[i][j] == 0:
                    return False
        return True

    # Checking game win condition usin DP
    def check_count(self, player, row_index, col_index, row_direction, col_direction):
        if row_index < 0 or row_index >= self.num_of_row:
            return 0
        if col_index < 0 or col_index >= self.num_of_col:
            return 0

        if self.board[row_index][col_index] == player:
            return 1 + self.check_count(
                player, 
                row_index+row_direction, 
                col_index+col_direction, 
                row_direction=row_direction, 
                col_direction=col_direction
            )
        else:
            return 0
        
    def row_win(self, player, row_index, col_index, recursion=0):
        count = 1 + self.check_count(
            player, 
            row_index, 
            col_index-1, 
            row_direction=0, 
            col_direction=-1
            ) + self.check_count(
                player,
                row_index,
                col_index+1,
                row_direction=0,
                col_direction=1
            )
        if count >= self.count_to_win:
            return True
        return False

    def col_win(self, player, row_index, col_index, recursion=0):
        count = 1 + self.check_count(
            player, 
            row_index-1, 
            col_index, 
            row_direction=-1, 
            col_direction=0
            ) + self.check_count(
                player,
                row_index+1,
                col_index,
                row_direction=1,
                col_direction=0
            )
        if count >= self.count_to_win:
            return True
        return False

    def horizontal_win_down(self, player, row_index, col_index):
        count = 1 + self.check_count(
            player, 
            row_index-1, 
            col_index-1, 
            row_direction=-1, 
            col_direction=-1
            ) + self.check_count(
                player,
                row_index+1,
                col_index+1,
                row_direction=1,
                col_direction=1
            )
        if count >= self.count_to_win:
            return True
        return False

    def horizontal_win_up(self, player, row_index, col_index):
        count = 1 + self.check_count(
            player, 
            row_index+1, 
            col_index-1, 
            row_direction=1, 
            col_direction=-1
            ) + self.check_count(
                player,
                row_index-1,
                col_index+1,
                row_direction=-1,
                col_direction=1
            )
        if count >= self.count_to_win:
            return True
        return False


def play_game():
    connect_four = ConnectFour()
    connect_four.move(PLAYER_1, 1)
    connect_four.move(PLAYER_2, 1)
    connect_four.move(PLAYER_1, 1)
    connect_four.move(PLAYER_2, 1)
    connect_four.move(PLAYER_1, 1)
    connect_four.move(PLAYER_2, 1)

    connect_four.move(PLAYER_1, 7)
    connect_four.move(PLAYER_2, 2)
    connect_four.move(PLAYER_1, 3)
    connect_four.move(PLAYER_2, 3)
    connect_four.move(PLAYER_1, 4)
    connect_four.move(PLAYER_2, 4)
    connect_four.move(PLAYER_1, 2)
    connect_four.move(PLAYER_2, 4)
    connect_four.move(PLAYER_1, 5)
    connect_four.move(PLAYER_2, 5)
    connect_four.move(PLAYER_1, 5)
    connect_four.move(PLAYER_2, 5)

def play_game_random():
    # Both player will try random move until it fins a valid movement. 
    connect_four = ConnectFour()
    continue_play = True
    turn = PLAYER_1
    while continue_play:
        status = connect_four.move(turn, get_random_move())
        if status != INVALID_MOVE:
            turn = get_next_player(turn)
        if status in [GAME_STATUS_WIN, GAME_STATUS_DRAW]:
            continue_play = False

def get_next_player(current_turn):
    if current_turn == PLAYER_1:
        return PLAYER_2
    else:
        return PLAYER_1

def get_random_move():
    return random.randint(1, 7)

if __name__ == '__main__':
    # print('Playing regular game')
    # play_game()
    print('Playing random game by both player')
    play_game_random()

