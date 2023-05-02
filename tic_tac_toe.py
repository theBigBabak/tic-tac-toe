import sys
import random
import copy

try:
    import colorama
except ModuleNotFoundError:
    print(
        "Module 'colorama' not installed on your system.\nPlease install it first then run the game again."
    )
    sys.exit()

from settings import Settings
from table import Table
from player import Player


class TicTacToe:
    """Model and manage a tic-tac-toe game."""

    WIDTH = 35

    def __init__(self):
        """Initialize a tic-tac-toe game attributes."""
        colorama.init()

        self.settings = Settings()
        self.the_table = Table()
        self.player1 = Player(self.settings.LABELS[0])
        self.player2 = Player(self.settings.LABELS[1])

        if random.randint(0, 1):  # Determine the player who starts the game in first round.
            self.game_first_player = self.player2
            self.game_second_player = self.player1
        else:
            self.game_first_player = self.player1
            self.game_second_player = self.player2

        self.round = 0

    def welcome(self):
        """
        Display a welcome statement.
        Display a statement and the table that say how to enter their move.
        """
        print(("-" * 13).center(self.WIDTH))
        print("│Tic-Tac-Toe│".center(self.WIDTH))
        print(("-" * 13).center(self.WIDTH))
        print("Welcome")
        self._how_to_play()
        print("You can enter 'q' for quit or 's' for settings anytime.")
        print("Are you ready? (y)es/(q)uit/(s)ettings")
        self._starter_input()

    def _how_to_play(self):
        """Display a statement and the table that say how to enter their move."""
        print("This is the game table.")
        self.the_table.display_table(self.the_table.table)
        print("Enter the cell number you want to choose.\n")
        print("=" * self.WIDTH)

    def _starter_input(self):
        """Check user input for start the game."""
        while True:
            user_input = input()
            if user_input.lower() == "q":
                sys.exit()
            elif user_input.lower() == "y":
                break
            elif user_input.lower() == "s":
                pass
            else:
                print("You should enter 'y' or 'q' or 's'")

    def display_round(self):
        """
        Increase the value of round attribute by one unit.
        Then displays the number of  current round.
        """
        self._increment_round()
        print(f"***round{self.round}***".center(self.WIDTH))

    def _increment_round(self):
        """Increments the round attribute."""
        self.round += 1

    def display_first_player(self):
        """Print a statement that says who starts the game."""
        print(f"!!!{self.game_first_player.name} starts the game!!!")
        print("=" * self.WIDTH)

    def display_scores(self):
        """Display each player's score."""
        print("Total scores:")
        print(f"- {self.player1.name}: {self.player1.score}")
        print(f"- {self.player2.name}: {self.player2.score}")
        print()

    def change_first_player(self):
        """Change the game first and second player for next rounds."""
        self.game_first_player, self.game_second_player = (
            self.game_second_player,
            self.game_first_player,
        )

    def get_player_move(self, which_player):
        """Get the player's move."""
        player_move = input(f"{which_player.name} enter your move: ")
        if player_move == "q":
            sys.exit()
        elif player_move == "s":
            pass
        elif (not player_move.isnumeric()) or (
            player_move not in self.settings.VALID_MOVES
        ):
            print("Invalid input! Enter a number between 1 to 9.")
            self.get_player_move(which_player)
        elif self.the_table.table[player_move] in self.settings.LABELS:
            print("This cell is taken. Enter another cell.")
            self.get_player_move(which_player)
        else:
            which_player.move = player_move

    def winner_checker(self):
        """Determines the winner of the game."""
        if (
            self.the_table.table["1"]
            == self.the_table.table["2"]
            == self.the_table.table["3"]
            == self.player1.label
            or self.the_table.table["4"]
            == self.the_table.table["5"]
            == self.the_table.table["6"]
            == self.player1.label
            or self.the_table.table["7"]
            == self.the_table.table["8"]
            == self.the_table.table["9"]
            == self.player1.label
            or self.the_table.table["1"]
            == self.the_table.table["4"]
            == self.the_table.table["7"]
            == self.player1.label
            or self.the_table.table["2"]
            == self.the_table.table["5"]
            == self.the_table.table["8"]
            == self.player1.label
            or self.the_table.table["3"]
            == self.the_table.table["6"]
            == self.the_table.table["9"]
            == self.player1.label
            or self.the_table.table["1"]
            == self.the_table.table["5"]
            == self.the_table.table["9"]
            == self.player1.label
            or self.the_table.table["3"]
            == self.the_table.table["5"]
            == self.the_table.table["7"]
            == self.player1.label
        ):
            print(f"{self.player1.name} wins.\n")
            self.player1.increment_player_score()
            self.display_scores()
            self.game_first_player = self.player1
            self.game_second_player = self.player2
            return True
        elif (
            self.the_table.table["1"]
            == self.the_table.table["2"]
            == self.the_table.table["3"]
            == self.player2.label
            or self.the_table.table["4"]
            == self.the_table.table["5"]
            == self.the_table.table["6"]
            == self.player2.label
            or self.the_table.table["7"]
            == self.the_table.table["8"]
            == self.the_table.table["9"]
            == self.player2.label
            or self.the_table.table["1"]
            == self.the_table.table["4"]
            == self.the_table.table["7"]
            == self.player2.label
            or self.the_table.table["2"]
            == self.the_table.table["5"]
            == self.the_table.table["8"]
            == self.player2.label
            or self.the_table.table["3"]
            == self.the_table.table["6"]
            == self.the_table.table["9"]
            == self.player2.label
            or self.the_table.table["1"]
            == self.the_table.table["5"]
            == self.the_table.table["9"]
            == self.player2.label
            or self.the_table.table["3"]
            == self.the_table.table["5"]
            == self.the_table.table["7"]
            == self.player2.label
        ):
            print(f"{self.player2.name} wins.\n")
            self.player2.increment_player_score()
            self.display_scores()
            self.game_first_player = self.player2
            self.game_second_player = self.player1
            return True

    def tie_checker(self):
        """Print 'Tie! and return True if the game gets tie."""
        if set(self.the_table.table.values()) == {"O", "X"}:
            self.change_first_player()
            print("Tie!\n")
            self.display_scores()
            return True  # If the game gets Tie.
        else:
            return False  # If the game doesn't get tie.
