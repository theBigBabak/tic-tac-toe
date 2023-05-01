import sys

from tic_tac_toe import TicTacToe


def first_round():
    """Run the first round of the game."""
    game.the_table.create_table()

    game.welcome()
    game.display_round()
    game.display_first_player()
    run_game_core()
    play_again()

def next_round():
    """Run other rounds of the game."""
    game.the_table.create_table()
    game.display_round()
    game.the_table.display_table(game.the_table.table)
    game.display_first_player()
    run_game_core()
    play_again()

def run_game_core():
    """
    Run the core of each round of the game:
    - Get first player move and the apply it to the table.
    - Display the table.
    - Check for the winner.
    - Check for the tie situation.
    - Do above for another player.
    """
    while True:
        game.get_player_move(game.game_first_player)
        game.the_table.modify_table(game.game_first_player.label, game.game_first_player.move)
        game.the_table.display_table(game.the_table.colorify_table())
        if game.winner_checker():
            break
        if game.tie_checker():
            break

        game.get_player_move(game.game_second_player)
        game.the_table.modify_table(game.game_second_player.label, game.game_second_player.move)
        game.the_table.display_table(game.the_table.colorify_table())
        if game.winner_checker():
            break
    
def play_again():
    """run the game again if the play want or quit the game if player want to quit."""
    print('=' * game.WIDTH)
    print("Do you want to play again? (y/n)")
    response = input().lower()
    if response == 'y':
        print('=' * game.WIDTH)
        next_round()
    elif response == 'n':
        sys.exit()
    else:
        print("Invalid input! You should enter 'y' or 'n'.")
        play_again()

def main():
    first_round()
    play_again()


# ------------------------------------------------
game = TicTacToe()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
