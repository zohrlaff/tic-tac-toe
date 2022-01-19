import random
import time

from graphics import Graphix

graphics = Graphix()


class Brain:
    def __init__(self):
        # Player names
        self.CPU = "CPU"
        self.player_1 = "Player 1"
        self.player_2 = "Player 2"
        # Coordinates and the symbols in them
        self.already_played = {}

    def player_count(self):
        """
        Inquires the user with how many players will play the game.
        Only 1 or 2 players can be chosen.
        Error handling will discard invalid inputs and re-prompt the user automatically.
        :return: integer type object with number of players
        """
        # Error handling loop helper
        choose_player_count = True
        while choose_player_count:
            try:
                try_player_count = int(input("How many players are there? 1 or 2?   "))
                if try_player_count < 1 or try_player_count > 2:
                    raise ValueError
            except ValueError:
                print("That's not a valid player count!")
            else:
                return try_player_count

    def first_turn(self, player_count: int):
        """
        Starts game of tictactoe. Depending on how many players are chosen the player(s) may or may not have a choice
        in their symbol (X, O). i.e. if there's only one player and the CPU goes first then Player 1 will get the
        leftover symbol.
        :param player_count: Takes an integer type object holding the amount of players in a game
        """

        # Reset graphic coordinates to starting position
        graphics.set_box()

        against_cpu = [self.CPU, self.player_1]
        two_players = [self.player_1, self.player_2]

        match player_count:
            case 1:
                # Randomly choose first player
                first_player = random.choice(against_cpu)
                # Remove name of player who starts from list of players
                against_cpu.pop(against_cpu.index(first_player))
                # Assign name of second player with the value left in list of players
                second_player = against_cpu[0]
                time.sleep(1)
                print(f"\n{first_player} will go first.\n")
                # Run choose_symbol method to let players choose their symbol, then, assign outcome to player_symbols
                player_symbols = self.choose_symbol(first_player, second_player)
                # This dictionary will store the player order and their chosen symbol
                player_order = {first_player: player_symbols[0], second_player: player_symbols[1]}
                # player_battle method begins the actual PvP game
                self.player_battle(player_order)
            case 2:
                first_player = random.choice(two_players)
                two_players.pop(two_players.index(first_player))
                second_player = two_players[0]
                print(f"{first_player} will go first.\n")
                player_symbols = self.choose_symbol(first_player, second_player)
                player_order = {first_player: player_symbols[0], second_player: player_symbols[1]}
                self.player_battle(player_order)

    def choose_symbol(self, first_player: str, second_player: str):
        """
        Allows players to choose what symbol they want to use to play.
        If the game is only being played by 1 player and the first turn is assigned to the CPU,
        then the symbols the players will use are assigned automatically.

        :param first_player: string type object that holds the name of the player who got the first turn
        :param second_player: string type object that holds the name of the player who got the second turn
        :return: string type object with symbols chosen by players
        """
        # Available symbols
        symbols = ["X", "O"]

        match first_player:
            case "CPU":
                # If the first turn goes to the CPU, a symbol is randomly chosen for them
                cpu_symbol = random.choice(symbols)
                # The symbol assigned to the CPU is removed from the list of symbols
                symbols.pop(symbols.index(cpu_symbol))
                # Player 1 gets the value left in the list of symbols
                player_symbol = symbols[0]
                # Prints the symbols assigned to CPU and player
                time.sleep(1)
                print(f"{first_player} is {cpu_symbol}, {second_player} is {player_symbol}\n")
                # Returns outcome of chosen symbols
                return cpu_symbol, player_symbol
            case _:
                # Error handling loop
                symbol_error = False
                while not symbol_error:
                    try:
                        # Let first player choose their symbol
                        symbol_choice = input(f"{first_player}, X or O?:    ").upper()
                        # Checks if value chosen is valid
                        if symbol_choice not in symbols:
                            raise ValueError
                    except ValueError:
                        print("Choose between X or O only.")
                    else:
                        first_player_choice = symbol_choice
                        match first_player_choice:
                            case "X":
                                # Print symbol outcome
                                time.sleep(1)
                                print(f"\n{second_player}, you are O\n")
                                # Returns outcome of chosen symbols
                                return "X", "O"
                            case "O":
                                # Print symbol outcome
                                time.sleep(1)
                                print(f"\n{second_player}, you are X\n")
                                # Returns outcome of chosen symbols
                                return "O", "X"

    def player_battle(self, players):
        """
        Executes the actual game of tic-tac-toe with error checking. Checks the order of players and lets them
        continually choose coordinates until a winner is found or the game ends in tie. Provides 'CPU' functionality
        for single player games.
        :param players: Dictionary with order of players and their chosen symbols
        """
        time.sleep(1)
        print(f"It's time to play!")
        graphics.draw_box()
        time.sleep(1)

        # Player info unpacking
        player_order = []
        for player in players.keys():
            player_order.append(player)

        # Turn counter to facilitate symbol display
        turn = 1
        play_game = True
        while play_game:
            # Turn taking mechanism
            if turn % 2 != 0:
                current_player = player_order[0]
            else:
                current_player = player_order[1]

            invalid_choice = False
            while not invalid_choice:
                try:
                    # If game is single player, allow the 'CPU' to choose coordinates
                    if current_player == "CPU":
                        valid_cpu_choice = False
                        while not valid_cpu_choice:
                            # 'CPU' will choose a coordinate that isn't in the list of already chosen coordinates
                            cpu_choice = random.choice(range(1, 10))
                            if cpu_choice not in list(self.already_played.keys()):
                                print(f"CPU chose: {cpu_choice}")
                                time.sleep(.5)
                                coordinate_choice = cpu_choice
                                valid_cpu_choice = True
                    # Two player coordinate choice and error checking
                    else:
                        coordinate_choice = int(input(f"{current_player}, choose a coordinate:    "))
                        time.sleep(.5)
                        if coordinate_choice < 1 or coordinate_choice > 9:
                            raise ValueError
                except ValueError:
                    print("That's not a valid coordinate.")
                else:
                    play_choice = coordinate_choice
                    self.already_played[coordinate_choice] = current_player

                    # Update tic-tac-toe on-screen graphics
                    graphics.update_box(play_choice - 1, players[current_player])
                    graphics.draw_box()

                    # Check if someone has won or the game is tied
                    if turn >= 9:
                        print("No one WINS. Tie.")
                        play_game = False
                    elif turn >= 5:
                        if self.find_winner(self.already_played, current_player):
                            play_game = False

                    turn += 1

                    invalid_choice = True

    def find_winner(self, all_played_symbols, current_player):
        """
        Finds winner of the game. Checks if one of the two players has fulfilled one of the eights ways of winning
        the game.

        :param all_played_symbols: List of coordinates that have already been chosen by players
        :param current_player: Name of the player currently choosing a coordinate
        """

        try:
            if all_played_symbols[1] == current_player and all_played_symbols[2] == current_player and \
                    all_played_symbols[3] == current_player:
                print(f"{current_player} WINS!\n")
                return True
        except KeyError:
            pass

        try:
            if all_played_symbols[4] == current_player and all_played_symbols[5] == current_player and \
                    all_played_symbols[6] == current_player:
                print(f"{current_player} WINS!\n")
                return True
        except KeyError:
            pass

        try:
            if all_played_symbols[7] == current_player and all_played_symbols[8] == current_player and \
                    all_played_symbols[9] == current_player:
                print(f"{current_player} WINS!\n")
                return True
        except KeyError:
            pass

        try:
            if all_played_symbols[1] == current_player and all_played_symbols[4] == current_player and \
                    all_played_symbols[7] == current_player:
                print(f"{current_player} WINS!\n")
                return True
        except KeyError:
            pass

        try:
            if all_played_symbols[2] == current_player and all_played_symbols[5] == current_player and \
                    all_played_symbols[8] == current_player:
                print(f"{current_player} WINS!\n")
                return True
        except KeyError:
            pass

        try:
            if all_played_symbols[3] == current_player and all_played_symbols[6] == current_player and \
                    all_played_symbols[9] == current_player:
                print(f"{current_player} WINS!\n")
                return True
        except KeyError:
            pass

        try:
            if all_played_symbols[1] == current_player and all_played_symbols[5] == current_player and \
                    all_played_symbols[9] == current_player:
                print(f"{current_player} WINS!\n")
                return True
        except KeyError:
            pass

        try:
            if all_played_symbols[3] == current_player and all_played_symbols[5] == current_player and \
                    all_played_symbols[7] == current_player:
                print(f"{current_player} WINS!\n")
                return True
        except KeyError:
            pass
