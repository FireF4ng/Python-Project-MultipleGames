import random
import math
import tkinter as tk
from tkinter import messagebox


class Connect4:

    def __init__(self, main_menu_instance, difficulty):
        self.difficulty = difficulty
        self.main_menu_instance = main_menu_instance
        self.c4_game = tk.Tk()
        self.start_button = None
        self.label = None
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.player = ''
        self.pc = ''
        self.turn = ''
        self.winner = ''
        self.tmp = 0
        self.depth = 6
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
                                                 command=lambda y=col: self.button(y))
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

    def button(self, col):
        """Function that takes place whenever a button is pressed on the board"""
        if self.difficulty == 0:
            for i in range(len(self.board) - 1, -1, -1):
                if self.board[i][col]['bg'] == 'white':
                    if self.player == 'red':
                        self.board[i][col]['bg'] = 'red'
                        self.next_player()
                        self.label['text'] = ("It's " + self.player + " turn ")
                    else:
                        self.board[i][col]['bg'] = 'yellow'
                        self.next_player()
                        self.label['text'] = ("It's " + self.player + " turn ")
                    break
            if self.win_msg():
                pass

        elif self.difficulty != 0:
            if self.turn == 'player':
                if self.find_empty_row(col) is not None:
                    self.board[self.find_empty_row(col)][col]['bg'] = self.player
                    if self.win_msg():
                        pass
                    else:
                        self.next_turn()
                        self.label['text'] = ("It's " + self.turn + " turn ")
                        self.initialize_game()
            else:
                self.initialize_game()

    def pc1_turn(self):
        """Easy bot that plays against player. It makes random moves on the board"""
        tmp = False
        while not tmp:
            col = random.randint(0, 6)
            if self.find_empty_row(col) is not None:
                self.board[self.find_empty_row(col)][col]['bg'] = self.pc
                tmp = True
        if not self.win_msg():
            self.next_turn()
            self.label['text'] = ("It's " + self.turn + " turn ")

    def pc2_turn(self):
        """Intermediary bot that tries to block the player from making the winning move if nothing to block
            it makes random choice"""
        for col in range(len(self.board[0])):
            row = self.find_empty_row(col)
            if row is not None:
                self.board[row][col]['bg'] = self.player
                if self.check_winner() and self.board[row + 1][col]['bg'] != 'white':
                    self.board[row][col]['bg'] = self.pc
                    if not self.win_msg():
                        self.next_turn()
                        self.label['text'] = ("It's " + self.turn + " turn ")
                    return
                else:
                    self.board[row][col]['bg'] = 'white'
        self.pc1_turn()

    def pc3_turn(self):
        """Advance bot using the MINIMAX algorithm with alpha-beta pruning to make the best possible move"""
        col, minimax_score = self.minimax(self.depth, -math.inf, math.inf, True)

        if self.find_empty_row(col[1]) is not None:
            row = self.find_empty_row(col[1])
            self.board[row][col[1]]['bg'] = self.pc

            if not self.win_msg():
                print(self.tmp)
                self.next_turn()
                self.label['text'] = ("It's " + self.turn + " turn ")
        else:
            self.pc3_turn()

    def minimax(self, depth, alpha, beta, maximizingplayer):
        """The MINIMAX algorithm using the Negamax variant with alpha-beta pruning for optimisation"""
        self.tmp += 1
        valid_locations = [(self.find_empty_row(col), col) for col in range(len(self.board[0])) if
                           self.find_empty_row(col) is not None
                           and self.board[self.find_empty_row(col)][col]['bg'] == 'white']

        is_terminal = self.check_winner() or len(valid_locations) == 0
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.winner == self.pc:
                    return None, 100000000000000
                elif self.winner == self.player:
                    return None, -10000000000000
                else:  # Game is over, no more valid moves
                    return None, 0
            else:  # Depth is zero
                return None, self.score_position()

        if maximizingplayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.find_empty_row(col[1])
                self.board[row][col[1]]['bg'] = self.pc
                new_score = self.minimax(depth - 1, alpha, beta, False)[1]
                self.board[row][col[1]]['bg'] = 'white'
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.find_empty_row(col[1])
                self.board[row][col[1]]['bg'] = self.player
                new_score = self.minimax(depth - 1, alpha, beta, True)[1]
                self.board[row][col[1]]['bg'] = 'white'
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def score_position(self):
        """Function that scores the current board position."""
        score = 0

        column_count = len(self.board[0])
        row_count = len(self.board)
        piece = self.pc
        window_length = 4

        # Score center column
        center_array = [self.board[i][column_count // 2]['bg'] for i in range(len(self.board))]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score Horizontal
        for r in range(row_count):
            row_array = [self.board[r][c]['bg'] for c in range(len(self.board[r]))]
            for c in range(column_count - 3):
                window = row_array[c:c + window_length]
                score += self.evaluate_window(window, piece)

        # Score Vertical
        for c in range(column_count):
            col_array = [self.board[r][c]['bg'] for r in range(len(self.board))]
            for r in range(row_count - 3):
                window = col_array[r:r + window_length]
                score += self.evaluate_window(window, piece)

        # Score positive sloped diagonal
        for r in range(row_count - 3):
            for c in range(column_count - 3):
                window = [self.board[r + i][c + i]['bg'] for i in range(window_length)]
                score += self.evaluate_window(window, piece)

        # Score negative sloped diagonal
        for r in range(row_count - 3):
            for c in range(column_count - 3):
                window = [self.board[r + 3 - i][c + i]['bg'] for i in range(window_length)]
                score += self.evaluate_window(window, piece)

        return score

    def evaluate_window(self, window, piece):
        """Function that evaluates the score of a window of 4 positions"""
        score = 0
        opponent_piece = 'yellow' if piece == 'red' else 'red'

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(None) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(None) == 2:
            score += 2

        if window.count(opponent_piece) == 3 and window.count(None) == 1:
            score -= 4

        return score

    def find_empty_row(self, col):
        """Function to find the empty row of a column"""
        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][col]['bg'] == 'white':
                return row
        return None

    def check_winner(self):
        """Function that checks the board for a winner. It checks colons, rows and diagonals and returns False if
                there are still moves to make and no winners, True if there is a winner"""
        # Check rows
        for row in self.board:
            for col in range(len(row) - 3):
                if row[col]['bg'] == row[col + 1]['bg'] == row[col + 2]['bg'] == row[col + 3]['bg'] != 'white':
                    self.winner = row[col]['bg']
                    return True

        # Check cols
        for col in range(len(self.board[0])):
            for row in range(len(self.board) - 3):
                if self.board[row][col]['bg'] == self.board[row + 1][col]['bg'] == self.board[row + 2][col]['bg'] == \
                        self.board[row + 3][col]['bg'] != 'white':
                    self.winner = self.board[row][col]['bg']
                    return True

        # Check pos diagonals
        for col in range(len(self.board[0]) - 3):
            for row in range(len(self.board) - 3):
                if (
                        self.board[row][col]['bg'] == self.board[row + 1][col + 1]['bg'] ==
                        self.board[row + 2][col + 2]['bg'] == self.board[row + 3][col + 3]['bg'] != 'white'
                ):
                    self.winner = self.board[row][col]['bg']
                    return True

        # Check neg diagonals
        for col in range(len(self.board[0]) - 3):
            for row in range(3, len(self.board)):
                if (
                        self.board[row][col]['bg'] == self.board[row - 1][col + 1]['bg'] ==
                        self.board[row - 2][col + 2]['bg'] == self.board[row - 3][col + 3]['bg'] != 'white'
                ):
                    self.winner = self.board[row][col]['bg']
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

if __name__ == '__main__':
    Connect4(None,3)