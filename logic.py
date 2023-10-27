import random

possibleNumbers = [1,2,3,4,5,6,7,8,9]
board = [[1,2,3],[4,5,6],[7,8,9]]
rows = 3
cols = 3
leaveLoop = False
turn = 'X'
turnCounter = 0

def make_empty_board():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

def printBoard():
    for x in range(rows):
        print("\n-|---|---|---|-")
        print(" |", end="")
        for y in range(cols):
            print("", board[x][y],end=" |")
    print("\n-|---|---|---|-")

def get_winner(board):
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2]:
            return board[x][0]
        elif board[0][x] == board[1][x] == board[2][x]:
            return board[0][x]
        # Check for diagonal
        elif board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
    # If there's no winner
    return "N"

def other_player(player):
    return "O" if player == "X" else "X"

#define modifyArray
def modifyArray(num, turn):
    num -= 1
    if(num == 0):
      board[0][0] = turn
    elif(num == 1):
      board[0][1] = turn
    elif(num == 2):
      board[0][2] = turn
    elif(num == 3):
      board[1][0] = turn
    elif(num == 4):
      board[1][1] = turn
    elif(num == 5):
      board[1][2] = turn
    elif(num == 6):
      board[2][0] = turn
    elif(num == 7):
      board[2][1] = turn
    elif(num == 8):
      board[2][2] = turn
