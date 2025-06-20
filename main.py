from engine import GameEngine
from gui import Gui
from tkinter import Tk

if __name__ == "__main__":
    tk = Tk()
    game_engine = GameEngine()
    gui = Gui(tk, game_engine)
    tk.mainloop()