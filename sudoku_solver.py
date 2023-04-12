# display function
from ast import Continue


def display(puzzle):
    for i in range(len(puzzle)):
        if i%3 == 0 and i != 0 :
            print("------+------+------")
        for j in range(len(puzzle[0])):
            if j%3 == 0 and j != 0:
                print("|", end="")
            if j == len(puzzle)-1:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j])+" ", end="")

# find next empty cell
def nextEmpty(puzzle):
    min_vals = float('Inf')
    min_cell = (0,0)
    for row in range(len(puzzle)):
        for column in range(len(puzzle[0])):
            if puzzle[row][column] == 0:
                vals = [x for x in range(1,10) if isAvailable(puzzle,row,x)]
                if len(vals) < min_vals:
                    min_vals = len(vals)
                    min_cell = (row, column)
    return None

# determine if a number from 1 to 9 can be placed in empty cell
def isAvailable(puzzle, coordinate, number):
    row = coordinate[0]
    column = coordinate[1]
    
    if number in puzzle[row]:
            return False
    
    for i in range(len(puzzle)):
        if number == puzzle[i][column]:
            return False

    row = (row//3)*3
    column = (column//3)*3 
    for i in range(3):
        for j in range(3):
            if puzzle[row+i][column+j] == number:
                return False
            
    return True

# backtracking to determine correct value of each cell
def backtrack(puzzle):
    coordinate = nextEmpty(puzzle)
    if coordinate is None:
        return True
    else:
        row = coordinate[0]
        column = coordinate[1]
        
    # for each number, check if it is available and if yes make a recursive call
    # if call returns False, set location as empty and continue with the next number
    for number in range (1,10):
        if isAvailable(puzzle, coordinate, number):
            puzzle[row][column] = number
            if backtrack(puzzle):
                return True
            else:
                puzzle[row][column] = 0
    return False

# solve input puzzle
def solve(puzzle):
    print()
    print("Your input:")
    display(puzzle)
    print()
    print("Solving...")
    print()
    if backtrack(puzzle):
        display(puzzle)
        print()
        print("Puzzle solved.")
        print()
    else: print("No solution")
    
# input puzzle 
def inputPuzzle(puzzle):       
    print("Please input your puzzle.")
    print("Input all numbers. For blanks input 0.")
    print("Leave a space ' ' between numbers and enter between lines.")
    print()

    #convert string input into nested list
    for i in range (0,9):
        x = input()
        puzzle.append(x.split(" "))
    for i in range (0,9):
        for j in range (0,9):
            puzzle[i][j] = int(puzzle[i][j])

# check if continue program
def repeat():
    char = input("Do you want to continue? Y/N\n")
    if char == "N":
        print("Exiting program...")
        quit()

# main
print("Sudoku puzzle solver.")
print()
while True:
    puzzle = []
    inputPuzzle(puzzle)
    solve(puzzle)
    repeat()
