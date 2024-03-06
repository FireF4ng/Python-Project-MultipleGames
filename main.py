from TicTacToe.TicTacToe import TicTacToe
from Connect_4.Connect4 import Connect4
from tkinter import *


class Main_menu:
    def __init__(self):
        self.window = None
        self.menu()

    def tic_tac_toe(self):
        self.window.destroy()
        self.create()
        self.window.title("Tic Tac Toe difficulty selector")
        tictactoe_btn1 = Button(self.window,
                                text="Easy",
                                fg='deep sky blue',
                                width=500,
                                height=5,
                                font='summer',
                                bd=5,
                                command=lambda: (self.window.destroy(), self.window.quit(), TicTacToe(self, 1)))

        tictactoe_btn2 = Button(self.window,
                                text="Medium",
                                fg='deep sky blue',
                                width=500,
                                height=5,
                                font='summer',
                                bd=5,
                                command=lambda: (self.window.destroy(), self.window.quit(), TicTacToe(self, 2)))

        tictactoe_btn3 = Button(self.window,
                                text="Hard",
                                fg='deep sky blue',
                                width=500,
                                height=5,
                                font='summer',
                                bd=5,
                                command=lambda: (self.window.destroy(), self.window.quit(), TicTacToe(self, 3)))

        tictactoe_btn4 = Button(self.window,
                                text="Back",
                                fg='deep sky blue',
                                width=500,
                                height=2,
                                pady=15,
                                font='summer',
                                bd=5,
                                command=lambda: (self.window.destroy(), self.window.quit(), Main_menu()))

        tictactoe_btn1.pack(side='top', pady=15)
        tictactoe_btn2.pack(side='top', pady=15)
        tictactoe_btn3.pack(side='top', pady=15)
        tictactoe_btn4.pack(side='top', pady=15)
        self.window.mainloop()

    def connect4(self):
        self.window.destroy()
        self.create()
        self.window.title("Connect 4 difficulty selector")
        connect4_btn1 = Button(self.window,
                               text="Easy",
                               fg='deep sky blue',
                               width=500,
                               height=5,
                               font='summer',
                               bd=5,
                               command=lambda: (self.window.destroy(), self.window.quit(), Connect4(self, 1)))

        connect4_btn2 = Button(self.window,
                               text="Medium",
                               fg='deep sky blue',
                               width=500,
                               height=5,
                               font='summer',
                               bd=5,
                               command=lambda: (self.window.destroy(), self.window.quit(), Connect4(self, 2)))

        connect4_btn3 = Button(self.window,
                               text="Hard",
                               fg='deep sky blue',
                               width=500,
                               height=5,
                               font='summer',
                               bd=5,
                               command=lambda: (self.window.destroy(), self.window.quit(), Connect4(self, 3)))

        connect4_btn4 = Button(self.window,
                               text="Back",
                               fg='deep sky blue',
                               width=500,
                               height=2,
                               pady=15,
                               font='summer',
                               bd=5,
                               command=lambda: (self.window.destroy(), self.window.quit(), Main_menu()))

        connect4_btn1.pack(side='top', pady=15)
        connect4_btn2.pack(side='top', pady=15)
        connect4_btn3.pack(side='top', pady=15)
        connect4_btn4.pack(side='top', pady=15)
        self.window.mainloop()

    def solo(self):
        self.window.destroy()
        self.create()
        self.window.title("Solo game selector")
        solo_btn1 = Button(self.window,
                           text="Tic Tac Toe",
                           fg='deep sky blue',
                           width=500,
                           height=5,
                           font='summer',
                           bd=5,
                           command=lambda: self.tic_tac_toe())

        solo_btn2 = Button(self.window,
                           text="Connect_4",
                           fg='deep sky blue',
                           width=500,
                           height=5,
                           font='summer',
                           bd=5,
                           command=lambda: self.connect4())

        solo_btn3 = Button(self.window,
                           text="Back",
                           fg='deep sky blue',
                           width=500,
                           height=2,
                           font='summer',
                           bd=5,
                           command=lambda: (self.window.destroy(), self.window.quit(), Main_menu()))

        solo_btn1.pack(side='top', pady=15)
        solo_btn2.pack(side='top', pady=15)
        solo_btn3.pack(side='top', pady=15)
        self.window.mainloop()

    def multiplayer(self):
        self.window.destroy()
        self.create()
        self.window.title("Multiplayer game selector")
        multiplayer_btn1 = Button(self.window,
                                  text="Tic Tac Toe",
                                  fg='deep sky blue',
                                  width=500,
                                  height=5,
                                  font='summer',
                                  bd=5,
                                  command=lambda: (self.window.destroy(), self.window.quit(), TicTacToe(self, 0)))

        multiplayer_btn2 = Button(self.window,
                                  text="Connect_4",
                                  fg='deep sky blue',
                                  width=500,
                                  height=5,
                                  font='summer',
                                  bd=5,
                                  command=lambda: (self.window.destroy(), self.window.quit(), Connect4(self, 0)))

        multiplayer_btn3 = Button(self.window,
                                  text="Back",
                                  fg='deep sky blue',
                                  width=500,
                                  height=2,
                                  font='summer',
                                  bd=5,
                                  command=lambda: (self.window.destroy(), Main_menu()))

        multiplayer_btn1.pack(side='top', pady=15)
        multiplayer_btn2.pack(side='top', pady=15)
        multiplayer_btn3.pack(side='top', pady=15)
        self.window.mainloop()

    def menu(self):
        self.create()
        self.window.title("main menu ")

        head = Label(self.window,
                     text="---Welcome to the main menu---",
                     fg='deep sky blue',
                     width=500,
                     height=3,
                     pady=20,
                     font='summer',
                     bd=5)

        menu_btn1 = Button(self.window,
                           text="solo",
                           fg='deep sky blue',
                           width=500,
                           height=3,
                           pady=15,
                           font='summer',
                           bd=5,
                           command=lambda: self.solo())

        menu_btn2 = Button(self.window,
                           text="multiplayer",
                           fg='deep sky blue',
                           width=500,
                           height=3,
                           pady=15,
                           font='summer',
                           bd=5,
                           command=lambda: self.multiplayer())

        menu_btn3 = Button(self.window,
                           text="Exit",
                           fg='deep sky blue',
                           width=500,
                           height=2,
                           pady=15,
                           font='summer',
                           bd=5,
                           command=self.window.quit)

        head.pack(side='top', pady=15)
        menu_btn1.pack(side='top', pady=15)
        menu_btn2.pack(side='top', pady=15)
        menu_btn3.pack(side='top', pady=15)
        self.window.mainloop()

    def create(self):
        self.window = Tk()
        width = 500
        height = 500
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)
        self.window.configure(bg='black')


# Call main function
if __name__ == '__main__':
    Main_menu()
