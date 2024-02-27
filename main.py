import numpy as np
import random
import tkinter as tk

class TicTacToeGame:
    def __init__(self):
        self.window = tk.Tk()
        self._create_ui_menu()
        self.board = np.zeros((3, 3))
        self.player = 1
        self.state = 0
        self._cells = {}

    def turn(self):
        """Main Function of the games that works in turns"""
        self.player = self.coin_toss()
        while self.state == 0:
            x = int(input("Chose the Row you want to play: ")) - 1
            y = int(input("Chose the Column you want to play: ")) - 1
            tmp = True
            while not (tmp == False):
                if self.check_move(x, y):
                    self.board[x][y] = self.player
                    tmp = False
                    print(self.board)
                else:
                    print("Impossible because case already used")
                    print(self.board)
                    print("Re-chose the placement")
                    x = int(input("Chose the Row you want to play: ")) - 1
                    y = int(input("Chose the Column you want to play: ")) - 1
            self.state = self.check_winner()
            self.next_player()
        if self.state == 1:
            print("Player 1 wins")
        elif self.state == 2:
            print("Player 2 wins")
        else:
            print("Tie")

    def next_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def coin_toss(self):
        """Function that determines what player goes first as X and what player gets 0"""
        return random.randint(1, 2)

    def check_winner(self):
        """Function that checks the board for a winner. It checks colons, rows and diagonals and returns 0 if there are still
        moves to make and no winners, 1 if player 1 wins, 2 if player 2 wins and 3 if it is a tie"""
        # Check Rows
        for i in range(np.shape(self.board)[0]):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and np.all(
                    self.board != 0):
                return self.board[i][0]

        # Check Cols
        for i in range(np.shape(self.board)[1]):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and np.all(
                    self.board != 0):
                return self.board[0][i]

        # Check Diagonals
        if np.all(self.board.diagonal() == 1) or np.all(self.board.diagonal() == 2):
            return self.board[0][0]
        elif np.all(np.fliplr(self.board).diagonal() == 1) or np.all(np.fliplr(self.board).diagonal() == 2):
            return self.board[0][-1]

        # Check Tie
        if np.all(self.board != 0):
            return 3
        return 0

    def check_move(self, x, y):
        """Function that checks if the move is possible, it returns True if it's possible and False if it's not"""
        if self.board[x][y] == 0:
            return True
        return False

    def _create_ui_menu(self):
        width = 600
        height = 500
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)

        start_button = tk.Button(self.window)
        start_button["justify"] = "center"
        start_button["text"] = "Start"
        start_button.place(x=160, y=100, width=303, height=75)
        start_button["command"] = self.start_button

        difficulty_button = tk.Button(self.window)
        difficulty_button["justify"] = "center"
        difficulty_button["text"] = "Leave"
        difficulty_button.place(x=160, y=280, width=303, height=75)
        difficulty_button["command"] = self.difficulty_button()

        leave_button = tk.Button(self.window)
        leave_button["justify"] = "center"
        leave_button["text"] = "Difficulty: Easy"
        leave_button.place(x=160, y=190, width=303, height=75)
        leave_button["command"] = self.leave_button()
        self.window.mainloop()

    def start_button(self):
        grid_frame = tk.Frame(master=self.window)
        grid_frame.pack()
        width = 600
        height = 600
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)

        for row in range(3):
            self.window.rowconfigure(row, weight=1, minsize=50)
            self.window.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(self.window)
                button["justify"] = "center"
                button["text"] = "Button"
                button.place(x=0, y=0, width=200, height=200)
                button["command"] = self.button()

                # self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
        return "Hello"

    def difficulty_button(self):
        return "Hello"

    def leave_button(self):
        return "Hello"

    def button(self):
        return "Hello"


# Main Code (Temporary)
game = TicTacToeGame()
game.run()
