#initialize empty board, variables
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

row, column = "", ""
error = 0

print("\n")

#printing function
def printBoard(ticBoard):
    for x in range(3):
        print(ticBoard[x])
    print("\n---------------\n")

def findWinner(ticBoard):


    #vertical win conditions
    if ticBoard[0][0] == "X" and ticBoard[1][0] == "X" and ticBoard[2][0] == "X":
        return True
    elif ticBoard[0][0] == "O" and ticBoard[1][0] == "O" and ticBoard[2][0] == "O":
        return True
    
    elif ticBoard[0][1] == "X" and ticBoard[1][1] == "X" and ticBoard[2][1] == "X":
        return True
    elif ticBoard[0][1] == "O" and ticBoard[1][1] == "O" and ticBoard[2][1] == "O":
        return True
    
    elif ticBoard[0][2] == "X" and ticBoard[1][2] == "X" and ticBoard[2][2] == "X":
        return True
    elif ticBoard[0][2] == "O" and ticBoard[1][2] == "O" and ticBoard[2][2] == "O":
        return True
    
    #horizontal win conditions
    elif ticBoard[0][0] == "X" and ticBoard[0][1] == "X" and ticBoard[0][2] == "X":
        return True
    elif ticBoard[0][0] == "O" and ticBoard[0][1] == "O" and ticBoard[0][2] == "O":
        return True
    
    elif ticBoard[1][0] == "X" and ticBoard[1][1] == "X" and ticBoard[1][2] == "X":
        return True
    elif ticBoard[1][0] == "O" and ticBoard[1][1] == "O" and ticBoard[1][2] == "O":
        return True
    
    elif ticBoard[2][0] == "X" and ticBoard[2][1] == "X" and ticBoard[2][2] == "X":
        return True
    elif ticBoard[2][0] == "O" and ticBoard[2][1] == "O" and ticBoard[2][2] == "O":
        return True
    
    #diagonal win conditions
    elif ticBoard[0][0] == "X" and ticBoard[1][1] == "X" and ticBoard[2][2] == "X":
        return True
    elif ticBoard[0][0] == "O" and ticBoard[1][1] == "O" and ticBoard[2][2] == "O":
        return True
    
    elif ticBoard[0][2] == "X" and ticBoard[1][1] == "X" and ticBoard[2][0] == "X":
        return True
    elif ticBoard[0][2] == "O" and ticBoard[1][1] == "O" and ticBoard[2][0] == "O":
        return True

#show empty board
printBoard(board)


#game loop
for x in range(9):
    if(findWinner(board)):
        break
    #player 1
    error = 1
    while error == 1:
        error = 0
        print("PLAYER 1 | Enter a row (from 1-3) and a column (from 1-3)\n")
        row = int(input())
        column = int(input(""))
        if(board[row-1][column-1] != " "):
            print("ALREADY USED, TRY AGAIN")
            error = 1
        else:
            error = 0
            board[row-1][column-1] = "X"
            printBoard(board)
            if(findWinner(board)):
                print("\nWINNER WINNER CHICKEN DINNER!")
                break

    #player 2
    
    if(findWinner(board)):
        break
    error = 1
    while error == 1:
        error = 0
        print("PLAYER 2 | Enter a row (from 1-3) and a column (from 1-3)\n")
        row = int(input())
        column = int(input(""))
        if(board[row-1][column-1] != " "):
            print("ALREADY USED, TRY AGAIN")
            error = 1
        else:
            error = 0
            board[row-1][column-1] = "O"
            printBoard(board)
            if(findWinner(board)):
                print("\nWINNER WINNER CHICKEN DINNER!")
                break

