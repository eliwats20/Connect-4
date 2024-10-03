from art import logo
import random

print(logo)

# Initialize the grid
global grid
grid = [
    ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫", "⚫"],
    ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫", "⚫"],
    ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫", "⚫"],
    ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫", "⚫"],
    ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫", "⚫"],
    ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫", "⚫"],
    ]

global row
global column

#Prints the Connect 4 grid with lines separating columns. 
def print_grid(grid):
    for row in grid:
        print(' | '.join(row))
        print('-' * (5 * len(row) - 1))  # Adjust for the length of the grid
    return grid


#Checks if the specified position on the grid is empty.
def isEmpty(grid, row, column):
    return grid[row][column] ==  "⚫"
            

#Drops game piece in the specific column
def drop_piece(grid, column, piece):
    
    for row in range(5, -1, -1):
        if isEmpty(grid, row, column):
            grid[row][column] = piece   
            return grid
    return grid


#Prompts the user to select game mode
def get_game_mode():
    play = int(input("Would you like to play single player against the CPU or multiplayer? Type 1 for single player or 2 for multiplayer or 3 to quit \n" ))
    
    while True:
        if play == 1:
            return 1
        elif play == 2:
            return 2
        elif play == 3:
            return 3
        else:
            play = input("I apologize but your input is invalid. Would you like to play single player against the CPU or multiplayer? Type 1 for single player or 2 for multiplayer. \n")




#Checks for a win condition in the grid for the given piece.
def win(piece):
    win = False

    #Vertical Check
    for row in range(3):
        for column in range(7):
            if grid[row][column] == piece and grid[row+1][column] == piece and grid[row+2][column] == piece and grid[row+3][column] == piece:
                win = True
    
    #Horizontal Check
    for row in range(6):
        for column in range(4):
            if grid[row][column] == piece and grid[row][column+1] == piece and grid[row][column+2] == piece and grid[row][column+3] == piece:
                win = True

    #Diagonal Checks

    #Column 1-4 bottom left to top right
    for row in range(4, 6):
        for column in range(4):
                if grid[row][column] == piece and grid[row-1][column+1] == piece and grid[row-2][column+2] == piece and grid[row-3][column+3] == piece:
                    win = True

    #Column 1-4 top right to bottom left
    for row in range(3):
        for column in range(4):
                if grid[row][column] == piece and grid[row+1][column-1] == piece and grid[row+2][column-2] == piece and grid[row+3][column-3] == piece:
                    win = True

    #Column 1-4 top left to bottom right
    for row in range(3):
        for column in range(4):
            if grid[row][column] == piece and grid[row+1][column+1] == piece and grid[row+2][column+2] == piece and grid[row+3][column+3] == piece:
                win = True
    
    #Column 1-4 bottom right to top left
    for row in range(3):
        for column in range(4):
            if grid[row][column] == piece and grid[row-1][column-1] == piece and grid[row-2][column-2] == piece and grid[row-3][column-3] == piece:
                win = True
    
    #Column 4-7 bottom left to top right

    #MUST STOP AT COLUMN 4 TO STAY INBOUND
    for row in range(4, 6):
        for column in range(4):
            if grid[row][column] == piece and grid[row-1][column+1] == piece and grid[row-2][column+2] == piece and grid[row-3][column+3] == piece:
                win = True

    #Column 4-7 top right to bottom left
    for row in range(3):
        for column in range(4, 7):
            if grid[row][column] == piece and grid[row+1][column-1] == piece and grid[row+2][column-2] == piece and grid[row+3][column-3] == piece:
                    win = True
                
    #Column 4-7 top left to bottom right
    for row in range(3):
        for column in range(4):
            if grid[row][column] == piece and grid[row+1][column+1] == piece and grid[row+2][column+2] == piece and grid[row+3][column+3] == piece:
                    win = True
    
    #Column 4-7 bottom right to top left
    for row in range(3):
        for column in range(4, 7):
            if grid[row][column] == piece and grid[row-1][column-1] == piece and grid[row-2][column-2] == piece and grid[row-3][column-3] == piece:
                    win = True
    
    
    return win
                    
#Assumes game is not finished on default, allowing user to play the game
game_finished = False

#Handles the single-player game mode against the CPU
def play_single():
    global game_finished

    connect4_grid = print_grid(grid)

    
    while not game_finished:
        column_drop = int(input("User's turn. Type # column 1 - 7 to drop your piece. \n"))

        while True: 
            if column_drop >= 1 and column_drop <= 7:
                if not isEmpty(grid, 0, column_drop-1):
                    column_drop = int(input("This column is full. Drop your piece in a column # 1 - 7. \n"))
                else:
                    break
            else:
                column_drop = int(input("Invalid input. Drop your piece in a column # 1 - 7. \n"))

        drop_piece(grid, column_drop-1, "🔴")
        connect4_grid = print_grid(grid)
        print("\n")

        if win("🔴") == True:
            print("Player 1 wins!")
            game_finished = True
            break
        print("\n")

        if game_finished:
           break

        #Computer generates a different column to drop a piece if the column is out of index or full.
        print("Computer's turn. Drop your piece in a column # 1 - 7. \n")
        column_drop = random.randint(1, 8)
        while True: 
            if column_drop >= 1 and column_drop <= 7:
                if not isEmpty(grid, 0, column_drop-1):
                    column_drop = random.randint(1,8)
                else:
                    break
            else:
                column_drop = random.randint(1,8)
        drop_piece(grid, column_drop-1, "🔵")
        connect4_grid = print_grid(grid)
        print("\n")

        if win("🔵"):
            print("Computer wins!")
            game_finished = True
            break
        print("\n")
        
        
        if game_finished:
            break




#Handles multiplayer game mode
def play_multi():
 
    global game_finished

    connect4_grid = print_grid(grid)
    
    while not game_finished:

        column_drop = int(input("Player 1's turn. Type # column 1 - 7 to drop your piece. \n"))

        while True: 
            if column_drop >= 1 and column_drop <= 7:
                if not isEmpty(grid, 0, column_drop-1):
                    column_drop = int(input("This column is full. Drop your piece in a column # 1 - 7. \n"))
                else:
                    break
            else:
                column_drop = int(input("Invalid input. Drop your piece in a column # 1 - 7. \n"))

        drop_piece(grid, column_drop-1, "🔴")
        connect4_grid = print_grid(grid)
        print("\n")

        if win("🔴") == True:
            print("Player 1 wins!")
            game_finished = True
            break
        print("\n")

        if game_finished:
           break
            

        column_drop = int(input("Player 2's turn. Type # column 1 - 7 to drop your piece. \n"))
        while True: 
            if column_drop >= 1 and column_drop <= 7:
                if not isEmpty(grid, 0, column_drop-1):
                    column_drop = int(input("This column is full. Drop your piece in a column # 1 - 7. \n"))
                else:
                    break
            else:
                column_drop = int(input("Invalid input. Drop your piece in a column # 1 - 7. \n"))
        drop_piece(grid, column_drop-1, "🔵")
        connect4_grid = print_grid(grid)
        print("\n")

        if win("🔵"):
            print("Player 2 wins!")
            game_finished = True
            break
        print("\n")
        
        
        if game_finished:
            break
    


    


play_again = True

print("Welcome to Connect 4! \n")


while play_again:

    game_mode = get_game_mode()

    while True:
            if game_mode == 1:
                play_single()
                break
            elif game_mode == 2:
                play_multi()
                break
            elif game_mode == 3:
                print("Thank you for playing, goodbye!")
                play_again = False
                break
            else:
                play = input("I apologize but your input is invalid. Would you like to play single player against the CPU or multiplayer? Type 1 for single player or 2 for multiplayer. \n")
                
    if play_again == False:
        break
    
