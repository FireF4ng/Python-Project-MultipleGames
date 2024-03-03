import random
import math
import tkinter as tk
from tkinter import messagebox, font, PhotoImage


class Connect4:

    def __init__(self, main_menu_instance, difficulty):
        self.difficulty = difficulty
        self.main_menu_instance = main_menu_instance
        # self.c4_game = tk.Tk()
        self.label = None
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.red = PhotoImage(file="red.png")
        self.yellow = PhotoImage(file="yellow.png")
        self.player = ''
        self.pc = ''
        self.turn = ''
        self.winner = ''
        self.coin_toss()
        # self.main_menu()

    # def main_menu(self):
    #     """Function that creates a menu with start button before actual game."""
    #     self.c4_game.title("Start Menu")
    #     width = 600
    #     height = 600
    #     screenwidth = self.c4_game.winfo_screenwidth()
    #     screenheight = self.c4_game.winfo_screenheight()
    #     alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    #     self.c4_game.geometry(alignstr)
    #     self.c4_game.resizable(width=False, height=False)
    #
    #     self.start_button = tk.Button(self.c4_game, width=100, height=100, text="Start", font=("Arial Black", 25),
    #                                   command=self.ui)
    #     self.start_button.pack(pady=20)
    #     self.c4_game.mainloop()
    #
    # def ui(self):
    #     """Function that creates the board and UI"""
    #     self.c4_game.destroy()
    #     self.c4_game = tk.Tk()
    #     self.c4_game.title("Connect_4")
    #     width = 525
    #     height = 550
    #     screenwidth = self.c4_game.winfo_screenwidth()
    #     screenheight = self.c4_game.winfo_screenheight()
    #     alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    #     self.c4_game.geometry(alignstr)
    #     self.c4_game.resizable(width=False, height=False)
    #
    #     for col in range(7):
    #         self.c4_game.rowconfigure(col, weight=1, minsize=50)
    #         self.c4_game.columnconfigure(col, weight=1, minsize=75)
    #         for row in range(6):
    #             self.board[row][col] = tk.Button(self.c4_game,
    #                                              image=self.red if self.board[row][col] == 'red' else self.yellow,
    #                                              #PhotoImage(width=1, height=1)
    #                                              width=30,
    #                                              height=30,
    #                                              command=lambda x=row, y=col: self.button(x, y))
    #             self.board[row][col].grid(row=row, column=col)
    #
    #     if self.difficulty != 0:
    #         self.label = tk.Label(text="It's " + self.turn + " turn ", font=('arial', 20, 'bold'))
    #     else:
    #         self.label = tk.Label(text="It's " + self.player + " turn ", font=('arial', 20, 'bold'))
    #     self.label.grid(row=6, column=1, columnspan=5)
    #     self.initialize_game()
    #
    # def initialize_game(self):
    #     """Function that initialises the game with a pc"""
    #     if self.turn == 'pc':
    #         if self.difficulty == 1:
    #             self.pc1_turn()
    #         elif self.difficulty == 2:
    #             self.pc2_turn()
    #         elif self.difficulty == 3:
    #             self.pc3_turn()
    #
    # def button(self, x, y):
    #     print("Button clicked at:", x, y)


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
        else:
            self.turn = 'pc'

if __name__ == '__main__':
    Connect4(None, 0)