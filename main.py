from TicTacToe import TicTacToe
from tkinter import *


class Main_menu:
    def __init__(self):
        self.window = None
        self.menu()

    def tic_tac_toe(self):
        self.window.destroy()
        self.create()
        self.window.title("Tic Tac Toe dificulty selector")
        self.window.geometry("500x500")
        tictactoe_B1 = Button(self.window, text="Easy", fg='deep sky blue', width=500, font='summer', bd=5,
                              command=lambda: (self.window.destroy(), self.window.quit(), TicTacToe(self, 1)))
        tictactoe_B2 = Button(self.window, text="Medium", fg='deep sky blue', width=500, font='summer', bd=5,
                              command=lambda: (self.window.destroy(), self.window.quit(), TicTacToe(self, 2)))
        tictactoe_B3 = Button(self.window, text="Hard", fg='deep sky blue', width=500, font='summer', bd=5,
                              command=lambda: (self.window.destroy(), self.window.quit(), TicTacToe(self, 3)))
        tictactoe_B4 = Button(self.window, text="Back", fg='deep sky blue', width=500, pady=15, font='summer', bd=5,
                              command=lambda: (self.window.destroy(), self.window.quit(), Main_menu()))

        tictactoe_B1.pack(side='top', pady=15)
        tictactoe_B2.pack(side='top', pady=15)
        tictactoe_B3.pack(side='top', pady=15)
        tictactoe_B4.pack(side='top', pady=15)
        self.window.mainloop()

    def connect4(self, solo_choise):
        pass

    def solo(self):
        self.window.destroy()
        self.create()
        self.window.title("Solo game selector")
        self.window.geometry("500x500")
        solo_B1 = Button(self.window, text="Tic Tac Toe", fg='deep sky blue', width=500, font='summer', bd=5,
                         command=lambda: self.tic_tac_toe())
        solo_B2 = Button(self.window, text="Connect 4", fg='deep sky blue', width=500, font='summer', bd=5,
                         command=lambda: self.connect4())
        solo_B3 = Button(self.window, text="Back", fg='deep sky blue', width=500, font='summer', bd=5,
                         command=lambda: (self.window.destroy(), self.window.quit(), Main_menu()))
        solo_B1.pack(side='top', pady=15)
        solo_B2.pack(side='top', pady=15)
        solo_B3.pack(side='top', pady=15)
        self.window.mainloop()

    def multiplayer(self):
        self.window.destroy()
        self.create()
        self.window.title("Multiplayer game selector")
        self.window.geometry("500x500")
        multiplayer_B1 = Button(self.window, text="Tic Tac Toe", fg='deep sky blue', width=500, font='summer',
                                bd=5,
                                command=lambda: (self.window.destroy(), self.window.quit(), TicTacToe(self, 0)))
        multiplayer_B2 = Button(self.window, text="Connect 4", fg='deep sky blue', width=500, font='summer',
                                bd=5,
                                command=lambda: self.connect4())
        multiplayer_B3 = Button(self.window, text="Back", fg='deep sky blue', width=500, font='summer', bd=5,
                                command=lambda: (self.window.destroy(), Main_menu()))
        multiplayer_B1.pack(side='top', pady=15)
        multiplayer_B2.pack(side='top', pady=15)
        multiplayer_B3.pack(side='top', pady=15)
        self.window.mainloop()

    def menu(self):
        self.create()
        self.window.title("main menu ")
        head = Button(self.window, text="---Welcome to the main menu---", fg='deep sky blue', width=500, pady=20,
                      font='summer',
                      bd=5)
        B1 = Button(self.window, text="solo", fg='deep sky blue', width=500, pady=15, font='summer', bd=5,
                    command=lambda: self.solo())
        B2 = Button(self.window, text="multiplayer", fg='deep sky blue', width=500, pady=15, font='summer', bd=5,
                    command=lambda: self.multiplayer())
        B3 = Button(self.window, text="Exit", fg='deep sky blue', width=500, pady=15, font='summer', bd=5,
                    command=self.window.quit)

        head.pack(side='top', pady=15)
        B1.pack(side='top', pady=15)
        B2.pack(side='top', pady=15)
        B3.pack(side='top', pady=15)
        self.window.mainloop()

    def create(self):
        self.window = Tk()
        width = 600
        height = 600
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)


# Call main function
if __name__ == '__main__':
    Main_menu()
