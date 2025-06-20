from tkinter import Tk, Button, Label, messagebox, Radiobutton, IntVar
from engine import GameEngine

class Gui:
    def __init__(self, tk_root, game_engine_obj):
        """
        GUI class with 3 normal buttons: O/X for choosing symbols and quit for terminate the app
        9 buttons for every cell of the grid
        2 radiobuttons for difficulty
        and 5 labels

        Controls the app

        :param tk_root: tkinter Tk() class from out of class
        :param game_engine_obj: custom GameEngine class from out of class
        """
        self.engine = game_engine_obj
        self.root = tk_root
        self.root.title("TicTackToe")
        self.root.geometry("500x500")
        self.root.resizable(width=False, height=False)
        self.root.config(padx=135, pady=20)

        self.white_colour = "white"
        self.main_colour = "#00809D"
        self.secondary_colour = "#00809D"

        # Simple message with hint about picking a symbol
        self.symbol_pick = messagebox.Message(master=self.root, title="Prepare!",
                                         message="Pick the symbol or just start the game.\nDefault player's symbol is 'X'",
                                         default="ok")
        self.symbol_pick.show()

        # Simple dict for params of the cells on the grid
        self.cell_style = {
            "background": self.white_colour,
            "foreground": self.main_colour,
            "activebackground": self.secondary_colour,
            "activeforeground": self.white_colour,
            "highlightthickness": 2,
            "highlightbackground": self.main_colour,
            "highlightcolor": "WHITE",
            "width": 5,
            "height": 2,
            "border": 1,
            "cursor": "hand2",
            "font": ("Arial", 16, "bold"),
            "padx": 0,
            "pady": 0,
        }

        
        #--------- Labels ---------#

        # Changes for winners name before new game (except 1st game)
        self.title = Label(
            text="TicTackToe",
            foreground=self.main_colour,
            font=("Arial", 25, "bold"),
            pady=10,
        )
        self.title.grid(column=0, row=0, columnspan=3)

        self.player_name = Label(
            text="Player",
            foreground=self.main_colour,
            font=("Arial", 16, "bold"),
            pady=10
        )
        self.player_name.grid(column=0, row=1)

        # Changes every time when Bot or Player wins, if Tie - doesnt change
        self.score = Label(
            text="0 | 0",
            foreground=self.main_colour,
            font=("Arial", 20, "bold"),
            pady=10
        )
        self.score.grid(column=1, row=1)

        self.bot_name = Label(
            text="Bot",
            foreground=self.main_colour,
            font=("Arial", 16, "bold"),
            pady=10
        )
        self.bot_name.grid(column=2, row=1)

        self.difficulty_label = Label(
            text="Difficulty",
            foreground=self.main_colour,
            font=("Arial", 12, "bold"),
        )
        self.difficulty_label.grid(column=1, row=2, pady=5)


        # --------- Grid ---------#

        # Short way to create a dict with symbols for grid buttons(cells)
        self.grid_symbols = dict.fromkeys(range(1, 10), " ")

        self.player_symbol = "X"
        self.computer_symbol = "O"

        # Short way to create a grid with 9 buttons
        self.grid: dict[int, Button] = {}
        for i in range(1, 10):
            btn = Button(text=" ", **self.cell_style, command=lambda j=i: self.press_cell(j))
            row = 3 + (i - 1) // 3
            col = (i - 1) % 3
            btn.grid(row=row, column=col)
            self.grid[i] = btn

        # --------- Difficulty ---------#

        # Variable for difficulty 0 - EASY, 1 - HARD
        self.difficulty = IntVar()

        self.difficulty_hard_button = Radiobutton(
            background=self.white_colour,
            foreground=self.main_colour,
            activebackground=self.secondary_colour,
            activeforeground=self.white_colour,
            highlightthickness=2,
            highlightbackground=self.main_colour,
            highlightcolor=self.white_colour,
            selectcolor=self.main_colour,
            width=6,
            height=1,
            border=1,
            cursor="hand2",
            text="HARD",
            font=("Arial", 10, "bold"),
            command=self.change_difficulty_btn,
            value=1,
            variable=self.difficulty,
            indicatoron=False,
        )
        self.difficulty_hard_button.grid(column=2, row=2, pady=5)

        self.difficulty_easy_button = Radiobutton(
            background=self.white_colour,
            foreground=self.main_colour,
            activebackground=self.secondary_colour,
            activeforeground=self.white_colour,
            highlightthickness=2,
            highlightbackground=self.main_colour,
            highlightcolor=self.white_colour,
            selectcolor=self.main_colour,
            width=6,
            height=1,
            border=1,
            cursor="hand2",
            text="EASY",
            font=("Arial", 10, "bold"),
            command=self.change_difficulty_btn,
            value=0,
            variable=self.difficulty,
            indicatoron=False,
        )
        self.difficulty_easy_button.grid(column=0, row=2, pady=5)

        # When app starts pushing the EASY button
        self.difficulty_easy_button.select()
        self.change_difficulty_btn()

        # --------- Buttons ---------#
        self.quit_button = Button(
            background=self.white_colour,
            foreground=self.main_colour,
            activebackground=self.secondary_colour,
            activeforeground=self.white_colour,
            highlightthickness=2,
            highlightbackground=self.main_colour,
            highlightcolor="WHITE",
            width=5,
            height=2,
            border=1,
            cursor="hand2",
            text="quit",
            font=("Arial", 10, "bold"),
            command=self.close,
        )
        self.quit_button.grid(column=1, row=6, pady=10)

        self.x_button = Button(
            background=self.white_colour,
            foreground=self.main_colour,
            activebackground=self.secondary_colour,
            activeforeground=self.white_colour,
            highlightthickness=2,
            highlightbackground=self.main_colour,
            highlightcolor="WHITE",
            width=3,
            height=1,
            border=1,
            cursor="hand2",
            text="X",
            font=("Arial", 12, "bold"),
            command=lambda :self.choose_symbol("X")
        )
        self.x_button.grid(column=0, row=6, pady=10)

        self.o_button = Button(
            background=self.white_colour,
            foreground=self.main_colour,
            activebackground=self.secondary_colour,
            activeforeground=self.white_colour,
            highlightthickness=2,
            highlightbackground=self.main_colour,
            highlightcolor="WHITE",
            width=3,
            height=1,
            border=1,
            cursor="hand2",
            text="O",
            font=("Arial", 12, "bold"),
            command=lambda: self.choose_symbol("O")
        )
        self.o_button.grid(column=2, row=6, pady=10)

    # --------- Scripts ---------#

    def change_difficulty_btn(self):
        """
        Just for controlling radiobutton's font color
        """
        if self.difficulty.get() == 0:
            self.difficulty_hard_button.config(foreground=self.main_colour)
            self.difficulty_easy_button.config(foreground=self.white_colour)
        elif self.difficulty.get() == 1:
            self.difficulty_easy_button.config(foreground=self.main_colour)
            self.difficulty_hard_button.config(foreground=self.white_colour)


    def press_cell(self, cell_nr: int):
        """
        When player press any unoccupied cell - pass the cell number to the engine,
        changes cell button's symbol, makes pressed cell unavailable,
        disables buttons for choosing symbols, tries to find a winner,
        updating grid, if there is no winner - passes move to bot else -
        shows win combo, shows winner name and after 2 seconds starts a new game

        :param cell_nr: comes from pressed grid (cell) buttons
        :return:
        """
        self.engine.player_move(cell_nr)
        self.grid_symbols[cell_nr] = self.player_symbol
        self.grid[cell_nr].config(command="")

        if self.x_button["state"] != "disabled":
            self.o_button.config(state="disabled")
            self.x_button.config(state="disabled")

        self.engine.find_winner()
        self.update_grid()

        if not self.engine.winner:
            self.ai_press_cell()
        else:
            self.show_win_combo(self.engine.winning_combo)
            self.congratulation()
            self.root.after(2000, self.new_game)

    def ai_press_cell(self):
        """
        Function for BOT's move. It checks the difficulty and (depends on difficulty ) trigger engine
        to calculate move.
        Change grids button to unavailable, tries to find a winner, update grid, if there is a winner -
        show winner, show combo, after 2 seconds start a new game
        """
        if self.difficulty.get() == 0:
            ai_cell = self.engine.choose_ai_move_easy()
        else:
            ai_cell = self.engine.choose_ai_move_hard()

        self.grid[ai_cell].config(command="")
        self.engine.ai_move(ai_cell)
        self.grid_symbols[ai_cell] = self.computer_symbol

        self.engine.find_winner()
        self.update_grid()

        if self.engine.winner:
            self.show_win_combo(self.engine.winning_combo)
            self.congratulation()
            self.root.after(2000, self.new_game)

    def close(self):
        """
        Terminate entire app
        """
        self.root.destroy()

    def choose_symbol(self, symbol: str):
        """
        It changes a Bot's and Player's symbols, if player pick an 'O' -
        starts a game and trigger Bot's Move.
        :param symbol: comes from buttons
        """
        if symbol == "X":
            self.player_symbol = "X"
            self.computer_symbol = "O"
        elif symbol == "O":
            self.computer_symbol = "X"
            self.player_symbol = "O"
            self.ai_press_cell()

        self.o_button.config(state="disabled")
        self.x_button.config(state="disabled")


    def update_grid(self):
        """
        Changing every cell's symbol on the grid, reference = separate dict of grid's symbols
        """
        for i in range(1, 10):
            self.grid[i].config(text=self.grid_symbols[i])

    def reset(self):
        """
        Reset of every element in the app (except score)
        """
        self.grid_symbols = dict.fromkeys(range(1, 10), " ")
        self.player_symbol = "X"
        self.computer_symbol = "O"
        self.engine.clean_data()
        self.update_grid()

        self.o_button.config(state="normal")
        self.x_button.config(state="normal")

        self.title.config(text="TicTackToe")

        for i in range(1, 10):
            self.grid[i].config(command=lambda j=i: self.press_cell(j))

    def show_win_combo(self, combo: list[int]):
        """
        Deleting every symbol on the grid and leaves only symbols from winner's combo
        :param combo: comes from engine
        """
        if self.engine.winner == "Bot":
            for i in range(1, 10):
                if i in combo:
                    self.grid_symbols[i] = self.computer_symbol
                else:
                    self.grid_symbols[i] = " "
        elif self.engine.winner == "Player":
            for i in range(1, 10):
                if i in combo:
                    self.grid_symbols[i] = self.player_symbol
                else:
                    self.grid_symbols[i] = " "

        self.update_grid()


    def new_game(self):
        """
        Start's a new game by reset everything and updating the score
        """
        self.score.config(text=f"{self.engine.player_score} | {self.engine.computer_score}")
        self.reset()

    def congratulation(self):
        """
        Changes a title label to show winner's name or Tie
        """
        if self.engine.winner == "Tie":
            self.title.config(text="Tie!")
        else:
            self.title.config(text=f"{self.engine.winner} wins!")






if __name__ == "__main__":
    tk = Tk()
    game_engine = GameEngine()
    gui = Gui(tk, game_engine)
    tk.mainloop()