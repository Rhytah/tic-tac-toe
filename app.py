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
if winner == "X " or winner =="O":
    print(winner + "won!!!")
elif winner ==None:
    print("It's a Tie")

    
def handle_turn(current_player):
    position = input("choose a position from 1-9: ")
    position = int(position)-1
    game_board[position]= 'x'
    display_game_board()
def check_if_game_over():
    check_if_win()
    check_if_draw()

def check_if_win():
    # checkrows
    # check columns
    # check diagonal
    pass
def change_player():
    pass
def check_if_draw():
    pass


play_game()