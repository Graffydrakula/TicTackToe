from random import choice
from typing import Optional, List

class GameEngine:
    def __init__(self):
        """
        winning combos - 2d array for all winning combos

        player/computer moves - dynamic array for keeping track of every move

        winner - name of the winner
        winning_combo - after victory stores and pass to gui winning combo

        player/computer_score - stores scores
        """
        self.winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.player_moves = []
        self.computer_moves = []

        self.winner = None
        self.winning_combo = None
        self.player_score = 0
        self.computer_score = 0


    def clean_data(self):
        """
        Cleans all the data in GameEngine class (for new game)
        """
        self.player_moves = []
        self.computer_moves = []
        self.winner = None
        self.winning_combo = None

    def find_winner(self):
        """
        Iterate though every combo in winning combos, compare moves to combos and looks for winning one.

        If all 9 cells was pressed (filled with symbols) - Tie
        """
        for combo in self.winning_combos:
            computer_result = all(tile in self.computer_moves for tile in combo)
            player_result = all(tile in self.player_moves for tile in combo)
            if computer_result:
                self.winner = "Bot"
                self.update_score()
                self.winning_combo = combo
                break
            elif player_result:
                self.winner = "Player"
                self.update_score()
                self.winning_combo = combo
                break
            elif len(self.player_moves) + len(self.computer_moves) == 9:
                self.winner = "Tie"
                break
            else:
                self.winner = None

    def update_score(self):
        """
        Checking self.winner and update the score
        """
        if self.winner == "Bot":
            self.computer_score += 1
        elif self.winner == "Player":
            self.player_score += 1

    def ai_move(self, ai_cell: int):
        """
        Updates computer's moves
        :param ai_cell: comes from gui buttons
        :return:
        """
        self.computer_moves.append(ai_cell)

    def player_move(self, cell_nr: int):
        """
        Updates player's moves
        :param cell_nr: comes from gui buttons
        :return:
        """
        self.player_moves.append(cell_nr)

    # Hard LEVEL AI

    def minimax(self, is_maximizing: bool, player_moves: list[int], computer_moves: List[int]) -> int:
        """
        Iterates over every combo to find winner/tie, in not found - by recurse checking every possible move
        to predict every move and choose the perfect move

        In every cycle it adds +1 move to player or computer and simulates game

        :param is_maximizing: it's keeping track of turns if True - next recursive cycle will be with +computer move
                                False - +player move
        :param player_moves: list of player's moves
        :param computer_moves: list of computer's moves
        :return: the best possible outcome for catch most effective move
        """
        for combo in self.winning_combos:
            if all(tile in computer_moves for tile in combo):
                return 1
            if all(tile in player_moves for tile in combo):
                return -1
        if len(player_moves) + len(computer_moves) == 9:
            return 0

        best_score = -float("inf") if is_maximizing else float("inf")
        for move in range(1, 10):
            if move not in player_moves and move not in computer_moves:
                if is_maximizing:
                    score = self.minimax(
                        False,
                        player_moves,
                        computer_moves + [move]
                    )
                    best_score = max(score, best_score)
                else:
                    score = self.minimax(
                        True,
                        player_moves + [move],
                        computer_moves
                    )
                    best_score = min(score, best_score)
        return best_score

    def choose_ai_move_hard(self) -> int:
        """
        Start recursive function and when recursion is over:
        :return: first best possible move
        """
        best_score = -float("inf")
        best_move = None

        for move in range(1, 10):
            if move not in self.player_moves and move not in self.computer_moves:
                score = self.minimax(
                    False,
                    self.player_moves[:],
                    self.computer_moves + [move]
                )
                if score > best_score:
                    best_score = score
                    best_move = move
        return best_move



    # EASY LEVEL AI

    def check_for_chance_and_risk(self) -> Optional[int]:
        """
        Look's for cell which can lead to lose or win and
        :return: it
        """
        for combo in self.winning_combos:
            chance_cell = [tile for tile in combo if tile not in self.computer_moves]
            if len(chance_cell) == 1 and chance_cell[0] not in self.player_moves:
                return chance_cell[0]

            risk_cell = [tile for tile in combo if tile not in self.player_moves]
            if len(risk_cell) == 1 and risk_cell[0] not in self.computer_moves:
                return risk_cell[0]

        return None

    def choose_ai_move_easy(self) -> int:
        """
        First check's for chance/risk cell, then tries to make a move on a middle of the grid,
        then on random available corner then pick's a random available cell
        """
        move = self.check_for_chance_and_risk()
        if move:
            return move

        if 5 not in self.computer_moves and 5 not in self.player_moves:
            return 5

        corners = [i for i in [1, 3, 7, 9] if i not in self.player_moves and i not in self.computer_moves]
        if corners:
            return choice(corners)

        return choice([i for i in range(1, 10) if i not in self.player_moves and i not in self.computer_moves])