#!/usr/bin/python3
import time

users_size= int(input(" what size of board would you like? "))

for x in range(int(users_size)):
    print( " +---+ " * users_size)
    print(" |   | " * users_size)
    print(" +---+ " * users_size)
print("Now let's play!")
#pause
time.sleep(2)


def createGame():
    board=[[" "," "," "],[" "," "," "],[" "," "," "]]
    return board

def placeOnBoard(board,location,player):
    x , y = location
    if player==1:
        board[int(x)][int(y)]="X"
        return 2
    else:
        board[int(x)][int(y)]="O"
        return 1

def drawboardgame(board):
    print(board[0])
    print(board[1])
    print(board[2])

def DrawBoardGamev2(board):
    for row in range(len(board)):
        #top
        for element in range(len(board[row])):
            print(" +---+ ", end="")
        print()
        #middle
        for element in range(len(board[row])):
            print(" | "+str(board[row][element])+" | " , end="")
        print()
        #ending
        for element in range(len(board[row])):
            print( " +---+ ", end="")
        print()

def checkWinner (board):
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            print("player " + str(board[row][0]) + " has won!")
            return True
    for column in range(len(board)):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != " ":
            print("player "+ str(board[0][column]) + " has won!")
            return True
    for diagonal in range(len(board)):
        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] and board[1][1] != " ":
            print("player " + str(board[0][column]) + " has won!")
            return True
        else:
            print("nobody won yet")
            return False


#MAIN CODE
round=0
board=createGame()
currentPlayer=1
board=createGame()
over=False
while True:
    round+=1
    if currentPlayer==1:
        chosing=tuple(input("choose where to put X on the board: ").split())
        currentPlayer=placeOnBoard(board,chosing,currentPlayer)
        print("placed")
        DrawBoardGamev2(board)
        over=checkWinner(board)
    else:
        chosing=tuple(input("choose where to put 0 on the board: ").split())
        currentPlayer=placeOnBoard(board,chosing,currentPlayer)
        print("placed")
        DrawBoardGamev2(board)
        over=checkWinner(board)
    if over==True:
        print("game over on round: ")
        print(round)
        break
