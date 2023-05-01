import copy

from settings import Settings


class Table:
    """Model and manage the table of a tic-tac-toe game."""
    R = '\033[0m'  # Reset color
    B = '\033[1m'  # Bold color

    def __init__(self):
        """Initialize the table's attributes."""
        self.settings = Settings()

        self.fg_color = self.settings.fg_color
        self.bg_color = self.settings.bg_color
        self.cell_number_color = self.settings.cell_number_color
        self.playerX_color = self.settings.playerX_color
        self.playerO_color = self.settings.playerO_color

        self.table = {}

    def create_table(self):
        """
        Makes a table with house numbers.
        Then assigns it to table attributes.
        """
        for number in range(1, 9 + 1):
            self.table[str(number)] = self.cell_number_color + str(number) + self.fg_color

    def clean_table(self):
        """Clean values of each key of table dictionary."""
        for key in self.table:
            self.table[key] = ' '
    
    def modify_table(self, player_label, player_move):
        """Modify the table based on the player marker."""
        if player_label.upper() == 'X':
            self.table[player_move] = 'X'
        elif player_label.upper() == 'O':
            self.table[player_move] = 'O'

    def colorify_table(self):
        """Colorify the table based on the player marker."""
        copy_table = copy.deepcopy(self.table)

        for key in copy_table:
            if copy_table[key] == 'X':
                copy_table[key] = (self.B + self.playerX_color + 'X' + self.R +
                                   self.bg_color + self.fg_color)
            elif copy_table[key] == 'O':
                copy_table[key] = (self.B + self.playerO_color + 'O' + self.R +
                                   self.bg_color + self.fg_color)
        return copy_table

    def display_table(self, which_table):
        """Display the game table on the screen."""
        fg = self.fg_color
        bg = self.bg_color

        print(f"         {bg + fg}     ╷     ╷     {self.R}")
        print(f"         {bg + fg}  {which_table['7']}  │  {which_table['8']}  │  {which_table['9']}  {self.R}")
        print(f"         {bg + fg}─────┼─────┼─────{self.R}")
        print(f"         {bg + fg}  {which_table['4']}  │  {which_table['5']}  │  {which_table['6']}  {self.R}")
        print(f"         {bg + fg}─────┼─────┼─────{self.R}")
        print(f"         {bg + fg}  {which_table['1']}  │  {which_table['2']}  │  {which_table['3']}  {self.R}")
        print(f"         {bg + fg}     ╵     ╵     {self.R}")

        print()
