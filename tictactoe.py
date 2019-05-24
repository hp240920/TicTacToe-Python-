import random


def display_board(b):  # board is a list
    print("           |          |          ")
    print(f"     {b[7]}     |    {b[8]}     |    {b[9]}  ")
    print("           |          |          ")
    print("---------------------------------")
    print("           |          |          ")
    print(f"     {b[4]}     |    {b[5]}     |    {b[6]}  ")
    print("           |          |          ")
    print("---------------------------------")
    print("           |          |          ")
    print(f"     {b[1]}     |    {b[2]}     |    {b[3]}  ")
    print("           |          |          ")


def player_input():
    global player1
    player1 = input("Please pick a marker 'X' or 'O': ").upper()
    print(player1)
    while player1 != 'X' and player1 != "O":
        player1 = input("Please pick a marker 'X' or 'O': ").upper()
    global player2
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print()
    print(f"Player 1: {player1}")
    print("Player 2: {}".format(player2))
    print()


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[7] == board[5] == board[3] == mark:
        return True
    elif board[9] == board[5] == board[1] == mark:
        return True
    elif board[1] == board[2] == board[3] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[9] == board[6] == board[3] == mark:
        return True
    elif board[7] == board[4] == board[1] == mark:
        return True
    else:
        return False


def choose_first():
    first = str(random.randint(1, 2))
    return "Player" + first


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    return not (" " in board)


def player_choice(board):
    position = int(input("Enter next position number (1-9): "))
    while not(1 <= position <= 9) or not(space_check(board, position)):
        position = int(input("Enter next position number (1-9): "))
    return position


def replay():
    answer = input("Do you want to play again: ").lower()
    if answer == 'yes' or answer == 'y':
        return True
    else:
        return False


while True:
    global_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    print('Welcome to Tic Tac Toe!')
    first_check = True
    while True:
        display_board(global_board)
        if first_check:
            player_input()
            first_check = False
            check = choose_first()
        if check == "Player1":
            print("Player 1 turn!!!")
            pos = player_choice(global_board)
            place_marker(global_board, player1, pos)
            if win_check(global_board, player1):
                display_board(global_board)
                print("Player 1 won!!!")
                break
            if full_board_check(global_board):
                display_board(global_board)
                print("Tie Game!!!")
                break
            check = "Player2"
        elif check == "Player2":
            print("Player 2 turn!!!")
            pos = player_choice(global_board)
            place_marker(global_board, player2, pos)
            if win_check(global_board, player2):
                display_board(global_board)
                print("Player 2 won!!!")
                break
            if full_board_check(global_board):
                display_board(global_board)
                print("Tie Game!!!")
                break
            check = "Player1"
        else:
            pass
    if not replay():
        break
