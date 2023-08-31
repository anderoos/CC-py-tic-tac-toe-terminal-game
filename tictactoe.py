import time 
class TicTacToeBoard:
    # initializes an empty board with empty values
    # game_state = 0 "game ends"; game_state = 1 "game proceeding"
    def board_initialize(): 
        game_state = 1
        board=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        print(f"{board[0][0]} | {board[0][1]} | {board[0][2]} ")
        print("----------")
        print(f"{board[1][0]} | {board[1][1]} | {board[1][2]} ")
        print("----------")
        print(f"{board[2][0]} | {board[2][1]} | {board[2][2]} ")
        return game_state
    # resets board to empty values
    def reset_board():
        board=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        print("The board has been reset!")
    def game_terminate():
        if game_state == 0:
            repeat = str(input("Play again?"))
            if repeat == "Yes":
                TicTacToeGame.gameinit()
class TicTacToePlayer(TicTacToeBoard):
    # Returns board
    def return_board():
        print(f"{board[0][0]} | {board[0][1]} | {board[0][2]} ")
        print("----------")
        print(f"{board[1][0]} | {board[1][1]} | {board[1][2]} ")
        print("----------")
        print(f"{board[2][0]} | {board[2][1]} | {board[2][2]} ")
    # Player 1 actions
    # Needs work
    def p1_move():
        time.sleep(1)
        print("Player 1, its your turn!")
        time.sleep(1)
        print("Here are your moves:")
        time.sleep(1)
        print(list(move for move in moveset.keys()))
        time.sleep(1)
        move1 = str(input("Where would you like to put your X? "))
        if move1 == "top left":
            if board[0][0] == " ":
                board[0][0] = "X"
            else:
                print("This space is occupied, try again")  # !  Need to add redundancy function
        elif move1 == "top middle":
            if board[0][1] == " ":
                board[0][1] = "X"
        elif move1 == "top right":
            if board[0][2] == " ":
                board[0][2] = "X"
        elif move1 == "middle left":
            if board[1][0] == " ":
                board[1][0] = "X"
        elif move1 == "middle":
            if board[1][1] == " ":
                board[1][1] = "X"
        elif move1 == "middle right":
            if board[1][2] == " ":
                board[1][2] = "X"
        elif move1 == "bottom left":
            if board[2][0] == " ":
                board[2][0] = "X"
        elif move1 == "bottom middle":
            if board[2][1] == " ":
                board[2][1] = "X"
        elif move1 == "bottom right":
            if board[2][2] == " ":
                board[2][2] = "X"
        else:
            print("Check your spelling.")
    def p2_move():
        time.sleep(1)
        print("Player 2, its your turn!")
        time.sleep(1)
        print("Here are your moves:")
        time.sleep(1)
        print(list(move for move in moveset.keys()))
        time.sleep(1)
        move1 = str(input("Where would you like to put your O? "))
        if move1 == "top left":
            if board[0][0] == " ":
                board[0][0] = "O"
            else:
                print("This space is occupied, try again")  # !  Need to add redundancy function
        elif move1 == "top middle":
            if board[0][1] == " ":
                board[0][1] = "O"
        elif move1 == "top right":
            if board[0][2] == " ":
                board[0][2]== "O"
        elif move1 == "middle left":
            if board[1][0] == " ":
                board[1][0] = "O"
        elif move1 == "middle":
            if board[1][1] == " ":
                board[1][1] = "O"
        elif move1 == "middle right":
            if board[1][2] == " ":
                board[1][2] = "O"
        elif move1 == "bottom left":
            if board[2][0] == " ":
                board[2][0] = "O"
        elif move1 == "bottom middle":
            if board[2][1] == " ":
                board[2][1] = "O"
        elif move1 == "bottom right":
            if board[2][2] == " ":
                board[2][2] = "O"
        else:
            print("Check your spelling.")
class TicTacToeGame(TicTacToePlayer, TicTacToeBoard):
    def game_duration():
        print("Great! Lets start!")
        time.sleep(1)
        print("Setting up board... \n")
        time.sleep(1)
        TicTacToeBoard.board_initialize()
        while game_state == 1:
            TicTacToePlayer.p1_move()
            TicTacToePlayer.p2_move()
    def check_win_conditions():
        # All horizontal options
        if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O"):
            print("Looks like we have a winner!")
            game_state = 0
            game_terminate()
        elif (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O"):
            print("Looks like we have a winner!")
            game_state = 0
            game_terminate()
        elif (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
            print("Looks like we have a winner!")
            game_state = 0
            game_terminate()
        else:
            pass
        # All vertical options
        if (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O"):
            print("Looks like we have a winner!")
            game_terminate()
        elif (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O"):
            print("Looks like we have a winner!")
            game_terminate()
        elif (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
            print("Looks like we have a winner!")
            game_state = 0
            game_terminate()
        else:
            pass
        # All diagonal options
        if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
            print("Looks like we have a winner!")
            game_state = 0
            game_terminate()
        elif (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
            print("Looks like we have a winner!")
            game_state = 0
            game_terminate()
        else:
            pass


        
board=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
moveset = {
"top right": board[0][0],
"top middle": board[0][1],
"top left": board[0][2],
"middle left": board[1][0],
"middle": board[1][1],
"middle right": board[1][2],
"bottom left": board[2][0],
"bottom middle": board[2][1],
"bottom right": board[2][2]
}

print("Welcome! Lets play some Tic Tac Toe!")
print("You'll need two playeres for this game.")
ready_status = str(input("Are you ready to continue? "))
if ready_status == "Yes":
    TicTacToeGame.gameinit()
    
    TicTacToePlayer.p1_move()
    time.sleep(1)
    TicTacToePlayer.return_board()
    TicTacToePlayer.p2_move()
    time.sleep(1)
    TicTacToePlayer.return_board()
    TicTacToePlayer.p1_move()
    time.sleep(1)
    TicTacToePlayer.return_board()
    TicTacToePlayer.p2_move()
    time.sleep(1)
    TicTacToePlayer.return_board()
    TicTacToePlayer.p1_move()
    time.sleep(1)
    TicTacToePlayer.return_board()
    TicTacToePlayer.p2_move()
    time.sleep(1)
    TicTacToePlayer.return_board()
    TicTacToeGame.check_win_conditions()
else:
    print("See you later!")

