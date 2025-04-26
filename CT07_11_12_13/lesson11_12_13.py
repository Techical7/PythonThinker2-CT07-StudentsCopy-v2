# print("Hello from lesson 11_12_13")

# var1 = 500
# def f():
#     global var1
#     var1 = 200
#     var2 = 300
#     print("var1 = " + str(var1))

# f()
# print("var1 = " + str(var1))

# Task 1a + 1b (lesson 11)
##################################
# def initialiseBoard():
#      grid=[]
#      row=[]
#      for i in range(3):
#           row()
#           for i in range(3):
#                row.append(" ")

          
#           return grid
     
# board = initialiseBoard()
# board[0][1] = "x"

# print(board)

##################################

##################################

# # ( | )

# Board = []
# Board_Layout: [] # type: ignore

# def initialiseBoard():

#      grid=[]
#      row=[]
#      for i in range(9):
#           row()
#           for i in range(9):
#                row.append(" ")

          
#           return grid
     
# board = ()
# board[0][1] = "x"

# print(board)
# print(" | 1"  " | 2")

# #Board Layout:
# #cell_number
# #\n

##################################







# Task ??? (lesson 12)
# 1, 2, 3 --> Row (1-1/3) (2-1/3) (3-1/3) / / /
# 4, 5, 6 --> Row (4-1/3) (5-1/3) (6-1/3) / / /
# 7, 8, 9 --> Row (7-1/3) (8-1/3) (9-1/3) / / /

import random

def initialise_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def get_player_move(board):
    while True:
        choice = input("Player 1, enter your move (1-9): ")
        if not choice.isdigit():
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        move = int(choice)
        if move < 1 or move > 9:
            print("Number must be between 1 and 9.")
            continue

        move -= 1
        row, col = divmod(move, 3)

        if board[row][col] == ' ':
            board[row][col] = 'X'
            break
        else:
            print("Cell already taken. Try a different spot.")

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def checkWin(board):
    win_lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for line in win_lines:
        if line[0] == line[1] == line[2] and line[0] != ' ':
            return line[0]
    return None

def board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_ai_move(board, level):
    print(f"AI (Level {level}) is thinking...")

    if level == 1:
        move = random.choice(get_empty_cells(board))

    elif level == 2:
        move = None
        for r, c in get_empty_cells(board):
            board[r][c] = 'O'
            if checkWin(board) == 'O':
                return board[r].__setitem__(c, 'O')
            board[r][c] = ' '
            board[r][c] = 'X'
            if checkWin(board) == 'X':
                move = (r, c)
            board[r][c] = ' '
        if not move:
            move = random.choice(get_empty_cells(board))

    elif level == 3:
        _, move = minimax(board, True)

    if move:
        r, c = move
        board[r][c] = 'O'

def minimax(board, is_maximizing):
    winner = checkWin(board)
    if winner == 'O':
        return 1, None
    elif winner == 'X':
        return -1, None
    elif board_full(board):
        return 0, None

    if is_maximizing:
        best_score = -float('inf')
        best_move = None
        for r, c in get_empty_cells(board):
            board[r][c] = 'O'
            score, _ = minimax(board, False)
            board[r][c] = ' '
            if score > best_score:
                best_score = score
                best_move = (r, c)
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for r, c in get_empty_cells(board):
            board[r][c] = 'X'
            score, _ = minimax(board, True)
            board[r][c] = ' '
            if score < best_score:
                best_score = score
                best_move = (r, c)
        return best_score, best_move

# ----------------------
# Game Entry Point
# ----------------------

def main():
    board = initialise_board()

    while True:
        level = input("Choose AI difficulty (1 = Easy, 2 = Medium, 3 = Hard): ")
        if level in ['1', '2', '3']:
            ai_level = int(level)
            break
        else:
            print("Invalid input. Please select 1, 2, or 3.")

    while True:
        print_board(board)
        get_player_move(board)
        if checkWin(board) == 'X':
            print_board(board)
            print("Congratulations, you win!")
            break
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        get_ai_move(board, ai_level)
        if checkWin(board) == 'O':
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
