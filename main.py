#Mason Inman
#Python 2 Spring 22
#TikTakToe game 3-in-a-row
#
#I did not cheat. This is my own unique work.
#I did not share my code with others.

def clear():
  return '\n' * 100
#
#sets the board to a 3x3 of empty spaces
#
def initializeBoard(table):
    for row in range(3):
        table.append(["_","_","_"])
#
#prints board without the list notation
#
def printBoard(table):
  print("  1 2 3")
  count = 1
  for row in table:
    print(count, end=" ")
    for col in row:
      print(col, end=" ")
    count = count + 1
    print()
#
#changes one spot of the gameboard to the appropiate symbol
#assumes cords enter is valid input(an empty spot on the board)
def updateBoard(table, r, c, isUser):
  if (isUser):
    table[r][c] = 'X'
  else:
    table[r][c] = 'O'
#
#gets user input and returns a list of cordinates to the gameboard
#
def userTurn(table):
  properInput = False
  
  while (not properInput):
    col = int(input("Enter the col: ")) - 1
    row = int(input("Enter the row: ")) - 1

    #checks if input is in bounds of board and space is empty
    if (row < 3 and row > -1):
      if (col < 3 and col > -1):
        if (table[row][col] == "_"):
          properInput = True
        else:
          print("Space already taken!")
      else: #improper col input
        print("\nPlease enter integers between 1 and 3\n")
    else: #improper row input
      print("\nPlease enter integers between 1 and 3\n")
      
  return [row, col]
#
#checks to see if there 3 in a row of any symbol
#
def checkWin(table):
    #check rows
  for row in table:
    if (row[0] == row[1] and row[0] == row[2] and not row[0] == "_"):
      return True
      
    #check cols
  for c in range(3):
      if(table[0][c] == table[1][c] and table[0][c] == table[2][c] and not table[0][c] == "_"):
        return True
        
    # check diagnols
  if ((table[0][0] == table[1][1] and table[0][0] == table[2][2] and not table[1][1] == "_") or (table[0][2] == table[1][1] and table[0][2] == table[2][0] and not table[1][1] == "_")):
    return True
  return False
#
#calculates the a move to play against the user and returns those cords
#
def CPUTurn(table):
  print("\n\nCPU Turn:")
  cords = []
  for r in range(3):
    for c in range(3):
      if (table[r][c] == "_"):
        table[r][c] = "O" #simulate if the spot will make the cpu win
        if (checkWin(table)):
          print("HAHAHHAHAHAHA")
          return [r, c]
        table[r][c] = "X" #simulate user playing there
        if (checkWin(table)):
          print("GET BLOCKED LOL")
          return [r, c] #if the user is going to win cpu should play at those cords
        else:
          cords = [r, c] #empty space that cpu can play on
        table[r][c] = "_" #reset the space that was simulated
  return cords
      
      
#
#main game loop
#
def tikTakToe(table):
  isFinished = False
  count = 0
  
  while (not isFinished and count < 5):
    print() #empty line to show next turn
    #USERS TURN
    cords = userTurn(table)
    updateBoard(table, cords[0], cords[1], True)
    printBoard(table) 
    if (checkWin(table)):
      isFinished = True
      print("X's Win!")
    count = count + 1
    
    #CPU TURN
    if (not isFinished and count < 5 ):
      cords = CPUTurn(table)
      updateBoard(table, cords[0], cords[1], False)
      printBoard(table) 
      if (checkWin(table)):
        isFinished = True
        print("O's Win!")
  if (count == 5):
    print("Tie game!")
def main():
  clear()
  board = [] #2d list
  initializeBoard(board)
  printBoard(board)
  tikTakToe(board)
  
main()