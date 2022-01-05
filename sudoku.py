'''board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]'''
#solving sudoku using backtracking
board=[]
print("Welcome to The Suduko Solver Version 1.0")
print("Enter the numbers for your 9x9 suduko board, blank space is 0. Press enter after each line")

#get input in 9 lines
for _ in range(9):
  while True:
    line=input()
    if len(line) == 9:
      #break when a proper input for one line has been given
      break
    else:
      print("must be 9 integers long")
  board.append([int(i) for i in line])

#check if the entire board is valid before solving the board
def check_if_valid_board(board):
  for i in range(9):
    for j in range(9):
      if valid(board,board[i][j],(i,j))==False and board[i][j]!=0:
        print('The number',board[i][j],'at row',i+1,'and column',j+1,'is illegal')
        return False
        #return false if the board in invalid and print what number is causing the issue
  return True

#solve the board
def finish(bo):
  '''
  bo is short form for board
  col is column
  '''
  find = find_empty(bo)
  if not find:
    return True
    #this means the solution has been found as there are no more empty squares
  else:
    row, col = find
  #backtracking
  for i in range(1,10):
    if valid(bo, i, (row, col)):
      bo[row][col] = i

      if finish(bo):
        return True

      bo[row][col] = 0

  return False

#checks if the position of a number is valid based on the other numbers in the board
def valid(board, number, position):
  # Check row
  for i in range(len(board[0])):
    if board[position[0]][i] == number and position[1] != i and number!=0:
      return False

  # Check column
  for i in range(len(board)):
    if board[i][position[1]] == number and position[0] != i and number!=0:
      return False

  # Check box
  box_x = position[1] // 3
  box_y = position[0] // 3

  for i in range(box_y*3, box_y*3 + 3):
    for j in range(box_x * 3, box_x*3 + 3):
      if board[i][j] == number and (i,j) != position:
        return False
  #return true if the number at that position works
  return True

#print the board given a 2d list
def print_board(board):
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      #print dashes to signify 3 rows have been printed
      #dont print dashes on the first line
      print("- - - - - - - - - - - -  ")

    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        #print a line to seperate every third coloumn
        print(" | ", end="")

      if j == 8:
        #at the end of each row, print a new line
        print(board[i][j])
      else:
        #print the number with a space instead of a new line
        print(str(board[i][j]) + " ", end="")


def find_empty(board):
  #find 0's in the 2d list and return the row and column
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        return (i, j)  # row, col
  return None

'''
Print the original board 
Solve the board and print it only if the inputted board is valid
if the input is not valid, print no solution
'''

print("Original board:")
print_board(board)
#checks if board is valid as a boolean
if check_if_valid_board(board):
  finish(board)
  print("___________________\nsolved board:\n")
  print_board(board) 
else:
  print("NO SOLUTION")