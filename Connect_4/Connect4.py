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
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        # self.red = PhotoImage(file="red.png")
        # self.yellow = PhotoImage(file="yellow.png")
        self.player = ''
        self.pc = ''
        self.turn = ''
        self.winner = ''
        self.coin_toss()
        self.game()
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

    def game(self):
        while not self.check_winner() and not self.check_draw():
            self.next_player()
            self.show_board()
            print("It's ", self.player, " turn")
            x = int(input("Enter col you want to play: ")) - 1
            for i in range(len(self.board) - 1, -1, -1):
                if self.board[i][x] == 0:
                    if self.player == 'red':
                        self.board[i][x] = 1
                    else:
                        self.board[i][x] = 2
                    break
        if self.check_winner():
            self.show_board()
            print("Winner", self.player)
        elif self.check_draw():
            self.show_board()
            print('Draw!')

    def check_winner(self):
        # Check rows
        for row in self.board:
            tmp = 0
            for elem in range(len(row) - 1):
                if row[elem] == row[elem + 1] != 0:
                    tmp += 1
            if tmp == 3:
                return True

        # Check cols
        for row in range(len(self.board)):
            tmp = 0
            for col in range(len(self.board[0]) - 2):
                if self.board[col][row] == self.board[col + 1][row] != 0:
                    tmp += 1
            if tmp == 3:
                return True

        # Check pos diagonals
        for col in range(len(self.board[0]) - 3):
            for row in range(len(self.board) - 3):
                if (
                        self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] != 0
                ):
                    return True


        # Check neg diagonals
        for col in range(len(self.board[0]) - 3):
            for row in range(3, len(self.board)):
                if (
                        self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3] != 0
                ):
                    return True

        # No Winners
        return False

    def check_draw(self):
        """Function that checks for a draw"""
        for i in self.board:
            if 0 not in i:
                return True
        return False

    def show_board(self):
        for i in self.board:
            print(i)
        print(" ", end="")
        for i in range(1, len(self.board[0]) + 1):
            print(i, end='  ')
        print('')

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
