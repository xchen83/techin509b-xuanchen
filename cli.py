# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import make_empty_board, printBoard, get_winner, other_player, modifyArray, leaveLoop, turnCounter, possibleNumbers, random

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'X'
    other_player = 'O'

    print("Welcome to Tic-Tac-Toe!")
    
    while(leaveLoop == False):
  ### It's the player turn
      if(turnCounter % 2 == 0):
        printBoard()
        numberPicked = int(input("\nChoose a number [1-9]: "))
        if(numberPicked >= 1 or numberPicked <= 9):
          modifyArray(numberPicked, 'X')
          possibleNumbers.remove(numberPicked)
        else:
          print("Invalid input. Please try again.")
        turnCounter += 1
  ### It's the computer's turn
      else:
        while(True):
          other_player_choice = random.choice(possibleNumbers)
          print("\nOther Player's Choice: ", other_player_choice)
          if(other_player_choice in possibleNumbers):
            modifyArray(other_player_choice, 'O')
            possibleNumbers.remove(other_player_choice)
            turnCounter += 1
            break
        winner = get_winner(board)
        if winner != "N" :
          print(winner, "won!")
          break
