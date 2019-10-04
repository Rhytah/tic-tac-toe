game_board = ["_","_","_",
"_","_","_",
"_","_","_"]
# if a game is still continuing
game_continues=True

winner = None
current_player="X"


def display_game_board():
    print(game_board[0]+ "|"+game_board[1]+"|"+game_board[2])
    print(game_board[3]+ "|"+game_board[4]+"|"+game_board[5])
    print(game_board[6]+ "|"+game_board[7]+"|"+game_board[8])

def play_game():
# start by displaying board
    display_game_board()

    while game_continues:

        handle_turn(current_player)
        check_if_game_over()
        change_player()

# scenario when game has ended
    if winner == "X" or winner =="O":
        print(winner + " wins this game!!!")
    elif winner == None:
        print("It's a Tie")


def handle_turn(player):
    print(player + " plays")
    position = input("choose a position from 1-9: ")
    position = int(position)-1
    
    game_board[position]= player
    display_game_board()


def check_if_game_over():
    check_if_win()
    check_if_draw()


def check_if_win():
    # set up global variable
    global winner
    # check rows
    horizontal_win = check_horizontal()
    # check columns
    vertical_win = check_vertical()
    # check diagonal
    diagonal_win = check_diagonal()

    if vertical_win:
        winner=vertical_win
    elif horizontal_win:
        winner=horizontal_win
    elif diagonal_win:
        winner=diagonal_win
    else:
        winner = None


def check_vertical():
    
    global game_continues
    first_column = game_board[0] == game_board[3] == game_board[6] !="_"
    second_column=game_board[1] == game_board[4] == game_board[7] !="_"
    third_column=game_board[2]== game_board[5] == game_board[8] !="_"

    if first_column or second_column or third_column:
        game_continues=False
    if first_column:
        return game_board[0]
    elif second_column:
        return game_board[1]
    elif third_column:
        return game_board[2]
    else:
        return None


def check_horizontal():

    global game_continues
    first_row = game_board[0] == game_board[1] == game_board[2] !="_"
    second_row=game_board[3] == game_board[4] == game_board[5] !="_"
    third_row=game_board[6]== game_board[7] == game_board[8] !="_"

    if first_row or second_row or third_row:
        game_continues=False
    if first_row:
        return game_board[0]
    elif second_row:
        return game_board[3]
    elif third_row:
        return game_board[6]
    else:
        return None

def check_diagonal():
    
    global game_continues
    left_diagonal = game_board[0] == game_board[4] == game_board[8] !="_"
    right_diagonal = game_board[6] == game_board[4] == game_board[2] !="_"

    if left_diagonal or right_diagonal:
        game_continues=False
    if left_diagonal:
        return game_board[0]
    elif right_diagonal:
        return game_board[6]
    else:
        return None


def change_player():

    global current_player
    if current_player =="X":
        current_player="O"
    elif current_player =="O":
        current_player="X"

def check_if_draw():
  global game_continues
  # If board is full
  if "_" not in game_board:
    game_continues = False
    return True
  # Else there is no tie
  else:
    return False


play_game()