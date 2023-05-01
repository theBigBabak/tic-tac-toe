class Player:
    """Model and manage players of the game."""
    VALID_MOVES = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

    def __init__(self, label):
        """Initialize a player attributes based on it's label."""
        self.label = label.upper()
        if self.label == 'X':
            self.name = 'PlayerX'
        elif self.label == 'O':
            self.name = 'PlayerO'
        self.move = ''
        self.score = 0

    def update_player_score(self, player_score):
        """Update the player score's value."""
        self.score = player_score

    def increment_player_score(self):
        """Increase the player score by one unit."""
        self.score += 1
