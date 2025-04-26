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

def initialiseBoard():
    return [[' ' for _ in range(3)] for _ in range(3)]

def printBoard(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def getPlayerMove(board):
    while True:
        userChoice = input("Player 1, please key in your choice (1-9): ")
        if not userChoice.isdigit():
            print("Please enter a valid number.")
            continue
        move = int(userChoice)
        if move < 1 or move > 9:
            print("Please enter a number between 1 and 9.")
            continue

        move -= 1
        row = move // 3
        col = move % 3

        if board[row][col] == ' ':
            board[row][col] = "X"
            break
        else:
            print("Spot taken, choose another one.")

def getAIMove(board):
    print("AI is making a move...")
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"

def checkWin(board):
    winning_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for condition in winning_conditions:
        if condition[0] == condition[1] == condition[2] and condition[0] != ' ':
            return True
    return False

def isBoardFull(board):
    return all(cell != ' ' for row in board for cell in row)

board = initialiseBoard()
while True:
    printBoard(board)
    getPlayerMove(board)
    if checkWin(board):
        printBoard(board)
        print("Player 1 wins!")
        break
    if isBoardFull(board):
        printBoard(board)
        print("It's a draw!")
        break

    getAIMove(board)
    if checkWin(board):
        printBoard(board)
        print("AI wins!")
        break
    if isBoardFull(board):
        printBoard(board)
        print("It's a draw!")
        break

    # Difficulty levels for AI:
    # Easy: Choose a random empty cell each time. 
    # Medium: Prioritise blocking human player from winning. 
    # Hard: Implement the algorithm you have created for
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
    if check_winner(board) == 'X'
        print_board(board)
        print("Congratulations, you win!")
        break
    if board_full(board):
        print_board(board)
        print("It's a draw!")
        break

    get_ai_move