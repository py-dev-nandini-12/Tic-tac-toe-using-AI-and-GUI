import tkinter as tk
import random
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Initialize the game board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Create buttons for the board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text=' ', font=('normal', 24), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        # Initialize the current player (X goes first)
        self.current_player = 'X'
        self.game_over = False

    def make_move(self, row, col):
        if not self.game_over and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.check_winner()
            self.switch_player()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        if not self.game_over and self.current_player == 'O':
            self.ai_move()

    def check_winner(self):

        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.game_over = True
                self.display_winner(self.board[i][0], i, 0, i, 2)
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.game_over = True
                self.display_winner(self.board[0][i], 0, i, 2, i)
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.game_over = True
            # self.display_winner(self.board[0][0], 0, 0, 2, 2)
            winner_name = self.board[0][0]

            self.buttons[0][0].config(highlightbackground='light pink')
            self.buttons[1][1].config(highlightbackground='light pink')
            self.buttons[2][2].config(highlightbackground='light pink')
            messagebox.showinfo(f"The winner is {winner_name}")

            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.game_over = True
            self.display_winner(self.board[0][2], 0, 2, 2, 0)
            self.buttons[0][2].config(highlightbackground='light blue')
            self.buttons[1][1].config(highlightbackground='light blue')
            self.buttons[2][0].config(highlightbackground='light blue')

            return

        # Check for a tie (no empty spaces left)
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            self.game_over = True
            self.display_message("It's a tie!")

    def highlight_winner(self, start_row, start_col, end_row, end_col):
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                self.buttons[i][j].configure(highlightbackground='light green')

    def display_message(self, message):
        messagebox.showinfo("Game Over", message)
        # self.root.quit()  # Close the game window when the game is over

    def display_winner(self, winner, start_row, start_col, end_row, end_col):
        self.highlight_winner(start_row, start_col, end_row, end_col)
        message = f"{winner} wins!"
        self.display_message(message)

    def ai_move(self):
        # Implement your AI player logic here
        # For a simple example, we'll make random moves
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)


# if __name__ == '__main__':
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
