import random
import math
import tkinter as tk
from tkinter import messagebox, font


class TicTacToe:

    def __init__(self, main_menu_instance, difficulty):
        self.difficulty = difficulty
        self.main_menu_instance = main_menu_instance
        self.ttt_game = tk.Tk()
        self.label = None
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.player = ''
        self.pc = ''
        self.turn = ''
        self.winner = ''
        self.tmp = 0
        self.coin_toss()
        self.main_menu()

    def main_menu(self):
        """Function that creates a menu with start button before actual game."""
        self.ttt_game.title("Start Menu")
        width = 600
        height = 600
        screenwidth = self.ttt_game.winfo_screenwidth()
        screenheight = self.ttt_game.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.ttt_game.geometry(alignstr)
        self.ttt_game.resizable(width=False, height=False)

        self.start_button = tk.Button(self.ttt_game, width=100, height=100, text="Start", font=("Arial Black", 25),
                                      command=self.ui)
        self.start_button.pack(pady=20)
        self.ttt_game.mainloop()

    def ui(self):
        """Function that creates the board and UI"""
        self.ttt_game.destroy()
        self.ttt_game = tk.Tk()
        self.ttt_game.title("Tic Tac Toe")
        width = 600
        height = 600
        screenwidth = self.ttt_game.winfo_screenwidth()
        screenheight = self.ttt_game.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.ttt_game.geometry(alignstr)
        self.ttt_game.resizable(width=False, height=False)

        for row in range(3):
            self.ttt_game.rowconfigure(row, weight=1, minsize=50)
            self.ttt_game.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                self.board[row][col] = tk.Button(self.ttt_game,
                                                 justify="center",
                                                 text=" ",
                                                 width=30,
                                                 font=("Arial Black", 25),
                                                 fg="red",
                                                 height=30,
                                                 command=lambda x=row, y=col: self.button(x, y))
                self.board[row][col].grid(row=row, column=col)
        if self.difficulty != 0:
            self.label = tk.Label(text="It's " + self.turn + " turn ", font=('arial', 20, 'bold'))
        else:
            self.label = tk.Label(text="It's " + self.player + " turn ", font=('arial', 20, 'bold'))
        self.label.grid(row=3, column=0, columnspan=3)
        self.initialize_game()

    def initialize_game(self):
        """Function that initialises the game with a pc"""
        if self.turn == 'pc':
            if self.difficulty == 1:
                self.pc1_turn()
            elif self.difficulty == 2:
                self.pc2_turn()
            elif self.difficulty == 3:
                self.pc3_turn()

    def coin_toss(self):
        """Function that determines what player goes first as X and what player gets 0"""
        tmp = random.randint(1, 2)
        if self.difficulty == 0:
            if tmp == 1:
                self.player = 'X'
            else:
                self.player = 'O'
        else:
            if tmp == 1:
                self.player = 'X'
                self.pc = 'O'
                self.turn = 'player'
            else:
                self.player = 'O'
                self.pc = 'X'
                self.turn = 'pc'

    def button(self, row, col):
        """Function that takes place whenever a button is pressed on the board"""
        if self.board[row][col]['text'] == " " and self.difficulty == 0:
            self.board[row][col]['text'] = self.player
            if self.player == 'X':
                self.board[row][col]['fg'] = "red"
            else:
                self.board[row][col]['fg'] = "blue"
            if self.win_msg():
                pass
            else:
                self.next_player()
                self.label['text'] = ("It's " + self.player + " turn ")

        elif self.board[row][col]['text'] == " " and self.difficulty != 0:
            if self.turn == 'player':
                self.board[row][col]['text'] = self.player
                if self.win_msg():
                    pass
                else:
                    self.next_turn()
                    self.label['text'] = ("It's " + self.turn + " turn ")
            if self.player == 'X':
                self.board[row][col]['fg'] = "red"
            else:
                self.board[row][col]['fg'] = "blue"
            self.initialize_game()

    def pc1_turn(self):
        """Easy bot that plays against player. It makes random moves on the board"""
        tmp = False
        while not tmp:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.board[x][y]['text'] == ' ':
                self.board[x][y]['text'] = self.pc
                if self.pc == 'X':
                    self.board[x][y]['fg'] = "red"
                else:
                    self.board[x][y]['fg'] = "blue"
                tmp = True
        if not self.win_msg():
            self.next_turn()
            self.label['text'] = ("It's " + self.turn + " turn ")

    def pc2_turn(self):
        """Intermediary bot that tries to block the player from making the winning move if nothing to block
            it makes random choice"""
        for row in range(3):
            for col in range(3):
                if self.board[row][col]['text'] == ' ':
                    self.board[row][col]['text'] = self.player
                    if self.check_winner():
                        self.board[row][col]['text'] = self.pc
                        if self.pc == 'X':
                            self.board[row][col]['fg'] = "red"
                        else:
                            self.board[row][col]['fg'] = "blue"
                        if not self.win_msg():
                            self.next_turn()
                            self.label['text'] = ("It's " + self.turn + " turn ")
                        return
                    else:
                        self.board[row][col]['text'] = ' '
        self.pc1_turn()

    def pc3_turn(self):
        """Advance bot using the MINIMAX algorithm with alpha-beta pruning to make the best possible move"""
        best_score = -math.inf
        best_move = None

        empty_positions = [(row, col) for row in range(len(self.board)) for col in range(len(self.board[0])) if
                           self.board[row][col]['text'] == ' ']

        for move in empty_positions:
            self.board[move[0]][move[1]]['text'] = self.pc
            score = self.minimax(best_score, +math.inf, False)
            self.board[move[0]][move[1]]['text'] = ' '
            if score > best_score:
                best_score = score
                best_move = move

        if best_move is not None:
            self.board[best_move[0]][best_move[1]]['text'] = self.pc
            if self.pc == 'X':
                self.board[best_move[0]][best_move[1]]['fg'] = "red"
            else:
                self.board[best_move[0]][best_move[1]]['fg'] = "blue"
            if not self.win_msg():
                print(self.tmp)
                self.next_turn()
                self.label['text'] = ("It's " + self.turn + " turn ")

    def minimax(self, alpha, beta, is_max_turn):
        """The MINIMAX algorithm with alpha-beta pruning for optimisation"""
        if self.check_winner():
            if self.winner == self.pc:
                return 1
            elif self.winner == self.player:
                return -1
        elif self.check_draw():
            return 0

        scores = []
        empty_positions = [(row, col) for row in range(len(self.board)) for col in range(len(self.board[0])) if
                           self.board[row][col]['text'] == ' ']

        for move in empty_positions:
            if is_max_turn:
                self.board[move[0]][move[1]]['text'] = self.pc
            else:
                self.board[move[0]][move[1]]['text'] = self.player

            score = self.minimax(alpha, beta, not is_max_turn)
            scores.append(score)
            self.board[move[0]][move[1]]['text'] = ' '
            if is_max_turn:
                alpha = max(alpha, score)
                if beta <= alpha:
                    self.tmp += 1
                    break
            else:
                beta = min(beta, score)
                if beta <= alpha:
                    self.tmp += 1
                    break

        return max(scores) if is_max_turn else min(scores)

    def check_winner(self):
        """Function that checks the board for a winner. It checks colons, rows and diagonals and returns False if
        there are still moves to make and no winners, True if there is a winner"""
        # Check Rows
        for row in self.board:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != " ":
                self.winner = row[0]['text']
                return True

        # Check Cols
        for col in range(3):
            if self.board[0][col]['text'] == self.board[1][col]['text'] == self.board[2][col]['text'] != " ":
                self.winner = self.board[0][col]['text']
                return True

        # Check Diagonals
        if (
                self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != " "
                or self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != " "
        ):
            self.winner = self.board[1][1]['text']
            return True

        # No Winners
        return False

    def check_draw(self):
        """Function that checks for a draw"""
        for row in self.board:
            for col in row:
                if " " in col['text']:
                    return False
        return True

    def win_msg(self):
        """Function that gives the winning/tie message if there is a winner/tie or false for None"""
        if self.check_winner():
            if self.difficulty == 0:
                messagebox.showinfo("Tic Tac Toe ", "Player {} wins!".format(self.player))
            else:
                messagebox.showinfo("Tic Tac Toe ", "{} wins!".format(self.turn))
            self.ttt_game.quit()
            self.ttt_game.destroy()
            self.main_menu_instance.menu()
        elif self.check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            self.ttt_game.quit()
            self.ttt_game.destroy()
            self.main_menu_instance.menu()
        else:
            return False

    def next_player(self):
        """Function that changes the next player to play"""
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def next_turn(self):
        """Function that changes the turn from pc to player or vice-versa"""
        if self.turn == 'pc':
            self.turn = 'player'
        else:
            self.turn = 'pc'