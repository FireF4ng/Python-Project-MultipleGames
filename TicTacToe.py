import random
import tkinter as tk
from tkinter import messagebox
from main import *


class TicTacToe:

    def __init__(self):
        self.game = tk.Tk()
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.player = ''
        self.coin_toss()
        self.ui()

    def coin_toss(self):
        """Function that determines what player goes first as X and what player gets 0"""
        tmp = random.randint(1, 2)
        if tmp == 1:
            self.player = 'X'
        else:
            self.player = 'O'

    def ui(self):
        """Function that creates the board and UI"""
        width = 600
        height = 600
        screenwidth = self.game.winfo_screenwidth()
        screenheight = self.game.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.game.geometry(alignstr)
        self.game.resizable(width=False, height=False)

        for row in range(3):
            self.game.rowconfigure(row, weight=1, minsize=50)
            self.game.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                self.board[row][col] = tk.Button(self.game,
                                                 justify="center",
                                                 text=" ",
                                                 width=30,
                                                 height=30,
                                                 command=lambda x=row, y=col: self.button(x, y))
                self.board[row][col].grid(row=row, column=col)

    def button(self, x, y):
        print(self.board[x][y]['text'])
        if self.board[x][y]['text'] == " ":
            self.board[x][y]['text'] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe ", "Player {} wins!".format(self.player))
                self.game.destroy()
                Main_menu()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.game.destroy()
                Main_menu()
            else:
                self.next_player()

    def check_winner(self):
        """Function that checks the board for a winner. It checks colons, rows and diagonals and returns False if
        there are still moves to make and no winners, True if there is a winner"""
        # Check Rows
        for row in self.board:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != " ":
                return True

        # Check Cols
        for col in range(3):
            if self.board[0][col]['text'] == self.board[1][col]['text'] == self.board[2][col]['text'] != " ":
                return True

        # Check Diagonals
        if (
                self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != " "
                or self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != " "
        ):
            return True

        # No Winners
        return False

    def check_draw(self):
        """Function that checks for a draw"""
        for row in self.board:
            for btn in row:
                if " " in btn['text']:
                    return False
        return True

    def check_move(self, x, y):
        """Function that checks if the move is possible, it returns True if it's possible and False if it's not"""
        if self.board[x][y] == 0:
            return True
        return False

    def next_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'