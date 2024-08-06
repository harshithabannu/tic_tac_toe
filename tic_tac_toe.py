import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x400")  # Adjusted height to fit buttons
        self.window.resizable(False, False)  # prevent resizing
        self.center_window()  # center the window

        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()

        name_label = tk.Label(self.window, text="Enter player names:", font=("Arial", 12), fg="blue")
        name_label.grid(row=0, column=0, columnspan=2, pady=10)

        player1_label = tk.Label(self.window, text="Player 1 (X):", font=("Arial", 12), fg="blue")
        player1_label.grid(row=1, column=0, padx=10, sticky='e')
        player1_entry = tk.Entry(self.window, textvariable=self.player1_name, width=20, font=("Arial", 12))
        player1_entry.grid(row=1, column=1, padx=10)

        player2_label = tk.Label(self.window, text="Player 2 (O):", font=("Arial", 12), fg="blue")
        player2_label.grid(row=2, column=0, padx=10, sticky='e')
        player2_entry = tk.Entry(self.window, textvariable=self.player2_name, width=20, font=("Arial", 12))
        player2_entry.grid(row=2, column=1, padx=10)

        start_button = tk.Button(self.window, text="Start Game", command=self.start_game, width=20, font=("Arial", 12), fg="green")
        start_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.buttons = []
        self.player_turn = "X"
        self.game_over = False

    def center_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        width = 300
        height = 400  # Adjusted height
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def start_game(self):
        # Remove previous widgets
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                widget.grid_forget()

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=3, width=6, font=("Arial", 12), fg="blue", bg="white")
                button.grid(row=i, column=j, padx=5, pady=5)  # Add padding for better spacing
                row.append(button)
            self.buttons.append(row)

        reset_button = tk.Button(self.window, text="Reset", command=self.reset, width=20, font=("Arial", 12), fg="red")
        reset_button.grid(row=3, column=0, columnspan=3, pady=10)  # Adjusted to span the entire width

    def click(self, row, column):
        if self.game_over:
            return
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                self.game_over = True
                messagebox.showinfo("Game Over", f"{self.player1_name.get() if self.player_turn == 'X' else self.player2_name.get()} wins!")
                self.window.title(f"Tic Tac Toe - Game Over")
            elif self.check_draw():
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.title(f"Tic Tac Toe - Game Over")
            else:
                self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        # Check rows and columns for win
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True
        # Check diagonals for win
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def check_draw(self):
        # Check if the board is full
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == "":
                    return False
        return True

    def reset(self):
        self.game_over = False
        self.start_game()
        self.window.title("Tic Tac Toe")

if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()
