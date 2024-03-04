import random
from pathlib import Path
import math
import tkinter as tk
from tkinter import messagebox, font, PhotoImage

class Connect4:

    def __init__(self, main_menu_instance, difficulty):
        self.difficulty = difficulty
        self.main_menu_instance = main_menu_instance
        self.c4_game = tk.Tk()
        self.label = None
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.player = ''
        self.pc = ''
        self.turn = ''
        self.winner = ''
        self.coin_toss()
        self.main_menu()

    def main_menu(self):
        """Function that creates a menu with start button before actual game."""
        self.c4_game.title("Start Menu")
        width = 600
        height = 600
        screenwidth = self.c4_game.winfo_screenwidth()
        screenheight = self.c4_game.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.c4_game.geometry(alignstr)
        self.c4_game.resizable(width=False, height=False)

        self.start_button = tk.Button(self.c4_game, width=100, height=100, text="Start", font=("Arial Black", 25),
                                      command=self.ui)
        self.start_button.pack(pady=20)
        self.c4_game.mainloop()

    def ui(self):
        """Function that creates the board and UI"""
        self.c4_game.destroy()
        self.c4_game = tk.Tk()
        self.c4_game.title("Connect_4")
        width = 525
        height = 550
        screenwidth = self.c4_game.winfo_screenwidth()
        screenheight = self.c4_game.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.c4_game.geometry(alignstr)
        self.c4_game.resizable(width=False, height=False)
        blue_frame = tk.Frame(self.c4_game, bg="blue")
        blue_frame.place(relx=0, rely=0, relwidth=1, relheight=0.93)

        for row in range(6):
            self.c4_game.rowconfigure(row, weight=1, minsize=50)
            for col in range(7):
                if col != 6:
                    self.c4_game.columnconfigure(col, weight=1, minsize=75)
                else:
                    self.c4_game.columnconfigure(col, minsize=75)
                self.board[row][col] = tk.Button(self.c4_game,
                                                 bg='white',
                                                 width=30,
                                                 height=30,
                                                 command=lambda x=row, y=col: self.button(x, y))
                self.board[row][col].grid(row=row, column=col, padx=5, pady=5)

        if self.difficulty != 0:
            self.label = tk.Label(text="It's " + self.turn + " turn ", font=('arial', 20, 'bold'))
        else:
            self.label = tk.Label(text="It's " + self.player + " turn ", font=('arial', 20, 'bold'))
        self.label.grid(row=6, column=1, columnspan=5)
        self.initialize_game()

    def initialize_game(self):
        """Function that initializes the game with a pc"""
        if self.turn == 'pc':
            if self.difficulty == 1:
                self.pc1_turn()
            elif self.difficulty == 2:
                self.pc2_turn()
            elif self.difficulty == 3:
                self.pc3_turn()

    def button(self, x, y):
        for i in range(len(self.board) - 1, -1, -1):
            if self.board[i][y]['bg'] == 'white':
                if self.player == 'red':
                    self.board[i][y]['bg'] = 'red'
                    self.next_player()
                    self.label['text'] = ("It's " + self.player + " turn ")
                else:
                    self.board[i][y]['bg'] = 'yellow'
                    self.next_player()
                    self.label['text'] = ("It's " + self.player + " turn ")
                break
        if self.win_msg():
            pass

    def check_winner(self):
        # Check rows
        for row in self.board:
            for col in range(len(row) - 3):
                if row[col]['bg'] == row[col + 1]['bg'] == row[col + 2]['bg'] == row[col + 3]['bg'] != 'white':
                    return True

        # Check cols
        for col in range(len(self.board[0])):
            for row in range(len(self.board) - 3):
                if self.board[row][col]['bg'] == self.board[row + 1][col]['bg'] == self.board[row + 2][col]['bg'] == \
                        self.board[row + 3][col]['bg'] != 'white':
                    return True

        # Check pos diagonals
        for col in range(len(self.board[0]) - 3):
            for row in range(len(self.board) - 3):
                if (
                        self.board[row][col]['bg'] == self.board[row + 1][col + 1]['bg'] == self.board[row + 2][col + 2]['bg'] == self.board[row + 3][col + 3]['bg'] != 'white'
                ):
                    return True


        # Check neg diagonals
        for col in range(len(self.board[0]) - 3):
            for row in range(3, len(self.board)):
                if (
                        self.board[row][col]['bg'] == self.board[row - 1][col + 1]['bg'] == self.board[row - 2][col + 2]['bg'] == self.board[row - 3][col + 3]['bg'] != 'white'
                ):
                    return True

        # No Winners
        return False

    def check_draw(self):
        """Function that checks for a draw"""
        for row in self.board:
            for col in row:
                if col['bg'] == 'white':
                    return False
        return True

    def win_msg(self):
        """Function that gives the winning/tie message if there is a winner/tie or false for None"""
        if self.check_winner():
            if self.difficulty == 0:
                self.next_player()
                messagebox.showinfo("Connect-4 ", "Player {} wins!".format(self.player))
            else:
                messagebox.showinfo("Connect-4 ", "{} wins!".format(self.turn))
            self.c4_game.quit()
            self.c4_game.destroy()
            self.main_menu_instance.menu()
        elif self.check_draw():
            messagebox.showinfo("Connect-4", "It's a draw!")
            self.c4_game.quit()
            self.c4_game.destroy()
            self.main_menu_instance.menu()
        else:
            return False

    def coin_toss(self):
        """Function that determines what player goes first as X and what player gets 0"""
        tmp = random.randint(1, 2)
        if self.difficulty == 0:
            if tmp == 1:
                self.player = 'red'
            else:
                self.player = 'yellow'
        else:
            if tmp == 1:
                self.player = 'red'
                self.pc = 'yellow'
                self.turn = 'player'
            else:
                self.player = 'yellow'
                self.pc = 'red'
                self.turn = 'pc'

    def next_player(self):
        """Function that changes the next player to play"""
        if self.player == 'red':
            self.player = 'yellow'
        else:
            self.player = 'red'

    def next_turn(self):
        """Function that changes the turn from pc to player or vice-versa"""
        if self.turn == 'pc':
            self.turn = 'player'
            self.label['text'] = ("It's " + self.turn + " turn ")
        else:
            self.turn = 'pc'
            self.label['text'] = ("It's " + self.turn + " turn ")
