import time
import sys

board_status = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
moveset_disp = {
        0: "top right",
        1: "top middle",
        2: "top left",
        3: "middle left",
        4: "middle",
        5: "middle right",
        6: "bottom left",
        7: "bottom middle",
        8: "bottom right"}
    
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]} ")

def playagain():
    ready_status = str(input("Play again? "))
    if ready_status == "no" or ready_status == "No":
        print("Terminating game...")
        sys.exit()
    elif ready_status == "yes" or ready_status == "Yes":
        game_restart()

def game_menu():
    print("Welcome! Ready to play some tic tac toe?")
    print("You'll need two players for this game.")
    ready_status = str(input("Are you ready to continue? "))
    if ready_status == "no" or ready_status == "No":
        print("See you later!")
        sys.exit()
    elif ready_status == "yes" or ready_status =="Yes":
        game_start()
    else:
        print("So is that a yes or no?")

def check_win_conditions():
    # Declare winning combinations
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]
    # Checking for winning combinations
    for winning_set in winning_combos:
            if board_status[winning_set[0]] == board_status[winning_set[1]] == board_status[winning_set[2]] == "X":
                print("Player X Wins!")
                time.sleep(1)
                print("Player X Wins!")
                time.sleep(1)
                print("Player X Wins!")
                time.sleep(1)
                # Reset game status, ask players to play again
                playagain()
                return True
            elif board_status[winning_set[0]] == board_status[winning_set[1]] == board_status[winning_set[2]] == "O":
                print("Player O Wins!")
                time.sleep(1)
                print("Player O Wins!")
                time.sleep(1)
                print("Player O Wins!")
                time.sleep(1)
                # Reset game status, ask players to play again
                playagain()
                return True
            # Checks for empty spaces
            elif " " not in board_status:
                print("Tied!")
                time.sleep(1)
                playagain()
                return True
            else:
                return False
    
# Player X's move
def playerX():
    time.sleep(1)
    print("Player X, its your turn!")
    time.sleep(1)
    print("Here are your moves:")
    time.sleep(1)
    # Print moveset, asks for input
    print(list(move for move in moveset_disp.items()))
    moveX = int(input("Place your X: "))
    # Checks if space is occupied
    if board_status[moveX] == " ":
        board_status[moveX] = "X"
        print_board(board_status)
    else:
        print("That space seems occupied. Try again.")
        moveX = int(input("Place your X: "))
        if board_status[moveX] == " ":
            board_status[moveX] = "X"
            print_board(board_status)
        else:
            print("That space seems occupied. Try again.")
            moveX = int(input("Place your X: "))
# Player O's Move
def playerO():
    time.sleep(1)
    print("Player O, its your turn!")
    time.sleep(1)
    print("Here are your moves:")
    time.sleep(1)
    print(list(move for move in moveset_disp.items()))
    moveO = int(input("Place your O: "))
    if board_status[moveO] == " ":
        board_status[moveO] = "O"
        print_board(board_status)
    else:
        print("That space seems occupied. Try again.")
        moveO = int(input("Place your O: "))
        if board_status[moveO] == " ":
            board_status[moveO] = "O"
            print_board(board_status)
        else:
            print("That space seems occupied. Try again.")
            moveO = int(input("Place your O: "))

# Checks for win conditions, loops through check function and player turn
def game_start():
    check_win_conditions()
    while check_win_conditions() == False:
        playerX()
        check_win_conditions()
        playerO()
        check_win_conditions()

# Reset starting board and reinitializes game
def game_restart():
    global board_status
    board_status  = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    game_start()

# Initialize game
game_menu()





