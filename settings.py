class Settings:
    """Model and manage all settings of the tic-tac-toe game."""

    def __init__(self):
        """Initialize all settings of the game."""
        # Table settings:
        self.fg_color = '\033[38;2;0;0;0m'
        self.bg_color = '\033[48;2;243;229;171m'
        self.cell_number_color = '\033[38;2;192;192;192m'
        self.playerX_color = '\033[38;2;255;0;0m'
        self.playerO_color = '\033[38;2;0;0;255m'