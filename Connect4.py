import tkinter as tk
from tkinter import messagebox
import random

# Constants for the board
ROWS = 6
COLS = 7
EMPTY = None  # No text in the cell
PLAYER_1 = "🔴"
PLAYER_2 = "🔵"

# Initialize the board
board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# Create the root window
root = tk.Tk()
root.title("Connect 4")

# Initialize the current player
current_player = PLAYER_1

# Initialize the mode (True for multiplayer, False for singleplayer)
is_multiplayer = True  # Default to multiplayer

# Function to check if the current player has won
def check_win():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == current_player:
                # Horizontal check
                if col + 3 < COLS and all(board[row][col+i] == current_player for i in range(4)):
                    return True
                # Vertical check
                if row + 3 < ROWS and all(board[row+i][col] == current_player for i in range(4)):
                    return True
                # Diagonal (top-left to bottom-right) check
                if row + 3 < ROWS and col + 3 < COLS and all(board[row+i][col+i] == current_player for i in range(4)):
                    return True
                # Diagonal (top-right to bottom-left) check
                if row + 3 < ROWS and col - 3 >= 0 and all(board[row+i][col-i] == current_player for i in range(4)):
                    return True
    return False

# Function to drop a piece into the selected column
def drop_piece(col):
    global current_player

    # Find the first empty row in the selected column
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = current_player
            update_board()
            # Check for win after the move
            if check_win():
                messagebox.showinfo("Game Over", f"Player {1 if current_player == PLAYER_1 else 2} wins!")
                reset_board()
            else:
                # Switch players (for multiplayer) or proceed to AI (for singleplayer)
                if is_multiplayer:
                    current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1
                else:
                    if current_player == PLAYER_1:
                        current_player = PLAYER_2
                        ai_move()
            break

# AI (Player 2) makes a random move
def ai_move():
    global current_player
    while True:
        col = random.randint(0, COLS-1)
        for row in range(ROWS-1, -1, -1):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_2
                update_board()
                if check_win():
                    messagebox.showinfo("Game Over", "Player 2 (AI) wins!")
                    reset_board()
                else:
                    # Switch back to Player 1 (human)
                    current_player = PLAYER_1
                return

# Function to update the board in the GUI
def update_board():
    for row in range(ROWS):
        for col in range(COLS):
            label = board_labels[row][col]
            if board[row][col] == PLAYER_1:
                label.config(bg="red")  # Entire square becomes red for Player 1
            elif board[row][col] == PLAYER_2:
                label.config(bg="blue")  # Entire square becomes blue for Player 2
            else:
                label.config(bg="white")  # Empty cells are white

# Function to reset the board
def reset_board():
    global board, current_player
    board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    current_player = PLAYER_1
    update_board()

# Function to select game mode (multiplayer or singleplayer)
def select_game_mode(mode):
    global is_multiplayer
    is_multiplayer = mode
    reset_board()
    mode_label.config(text="Multiplayer Mode" if is_multiplayer else "Singleplayer Mode")

# Create the GUI grid
board_labels = []
for row in range(ROWS):
    label_row = []
    for col in range(COLS):
        label = tk.Label(root, text="", width=6, height=3, bg="white", borderwidth=1, relief="solid", font=("Arial", 24),
                         anchor="center")
        label.grid(row=row, column=col)
        label.bind("<Button-1>", lambda event, col=col: drop_piece(col))
        label_row.append(label)
    board_labels.append(label_row)

# Add buttons for selecting game mode
mode_label = tk.Label(root, text="Multiplayer Mode", font=("Arial", 16))
mode_label.grid(row=ROWS, column=0, columnspan=COLS, sticky="nsew")

multiplayer_button = tk.Button(root, text="Multiplayer", command=lambda: select_game_mode(True), font=("Arial", 16))
multiplayer_button.grid(row=ROWS+1, column=0, columnspan=3, sticky="nsew")

singleplayer_button = tk.Button(root, text="Singleplayer", command=lambda: select_game_mode(False), font=("Arial", 16))
singleplayer_button.grid(row=ROWS+1, column=3, columnspan=4, sticky="nsew")

# Add a reset button to restart the game
reset_button = tk.Button(root, text="Restart Game", command=reset_board, font=("Arial", 16))
reset_button.grid(row=ROWS+2, column=0, columnspan=COLS, sticky="nsew")

# Start the main loop
root.mainloop()
