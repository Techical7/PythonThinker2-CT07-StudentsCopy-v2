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

# def getPlayerMove(gird):

#     userChoice = ""
#     while(userChoice.isdigit() == False):
#         userChoice = input("Player 1 Please key in your choice.")
# if(userChoice.isdigit() == False or int(userChoice)<1 or int(userChoice)>9):
        

def get_player_move(board):
    move_input = input("Enter your move (1-9): ")
    move - int(move_input) - 1
    row = move //3
    col - move % 3
    if(grid[row][col] == ' '):
    board[row][col] = "X"
    break
else:
    print("Please Key in your choice again as this spot is taken")


while get_player_move == True
