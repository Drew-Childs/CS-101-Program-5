#Drew Childs, 11/7/19, Program 5
import sys

def winner(row, column, symbol, grid, player):
    row_counter = 0
    column_counter = 0
    diag_counter = 0
    diag2_counter = 0
    
    for each in range(4):
        if grid[row][each] == symbol:   #Checks Columns
            column_counter += 1
        else:
            comumn_counter = 0

        if grid[each][column] == symbol:    #Checks Rows
            row_counter += 1
        else:
            row_counter = 0

        if grid[each][each] == symbol:  #Checks top left to bottom right
            diag_counter += 1
        else:
            diag_counter = 0

        if grid[-each + 2][each] == symbol: #Checks bottom left to top right
            diag2_counter += 1
        else:
            diag2_counter = 0

        if row_counter == 3 or column_counter == 3 or diag_counter == 3 or diag2_counter == 3:  #Determines if player has winning combination
            print(player, "is the winner!")
            display(grid)
            sys.exit()

def display(grid):      #Prints grid
    for row in range(4):
        for col in range(4):
            print(grid[row][col]," ", end = "")
        print()

def playerInput(grid, symbol, player):      #Gathers location from user
    while True:
        row = int(input("Enter the row number [1 to 4]: ")) - 1
        column = int(input("Enter the column number [1 to 4]: ")) - 1

        try:
            if grid[row][column] == "-":    #replaces with appropriate symbol
                grid[row][column] = grid[row][column].replace("-", symbol)
                break
            else:
                print("The chosen location is populated, please try again.")
        except:
            print("Out of range, please try again.")
            
    winner(row, column, symbol, grid, player)
    return grid
        

grid = [["-", "-", "-", "-"],
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"]]

player_1 = str(input("Enter Player 1 name: "))
while True:
    player_2 = str(input("Enter Player 2 name: "))  #Makes sure player names are unique
    if player_1 == player_2:
        print("Player names are the same, please try again.")
    else:
        break

p1_symbol = str(input("Enter Player 1 symbol: "))
while True:
    p2_symbol = str(input("Enter Player 2 symbol: "))   #Makes sure player symbols are unique
    if p1_symbol == p2_symbol:
        print("Player symbols are the same, please try again.")
    else:
        break
    
display(grid)

counter = 0

while True:
    if counter % 2 == 0:                #Alternates turns
        print("%s's turn:" % player_1)
        grid = playerInput(grid, p1_symbol, player_1)
    else:
        print("%s's turn:" % player_2)
        grid = playerInput(grid, p2_symbol, player_2)
    display(grid)
    counter += 1
