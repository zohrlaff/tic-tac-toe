import random
from graphics import Graphix

graphics = Graphix()


class Brain:
    def __init__(self):
        # Player names
        self.CPU = "CPU"
        self.player_1 = "Player 1"
        self.player_2 = "Player 2"
        # Coordinates with symbols in them
        self.already_played = {}

    def player_counts(self):
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
        against_cpu = [self.CPU, self.player_1]
        two_players = [self.player_1, self.player_2]

        match player_count:
            case 1:
                # Randomly choose first player
                who_starts = random.choice(against_cpu)
                # Remove name of player who starts from list of players
                against_cpu.pop(against_cpu.index(who_starts))
                # Assign name of second player with the value left in list of players
                second_player = against_cpu[0]
                print(f"{who_starts} will go first.\n")
                # Run choose_symbol method to let players choose their symbol, then, assign outcome to player_symbols
                player_symbols = self.choose_symbol(who_starts, second_player)
                # This dictionary will store the player order and their chosen symbol
                player_order = {who_starts: player_symbols[0], second_player: player_symbols[1]}
                # player_battle method begins the actual PvP game
                self.player_battle(player_order)
            case 2:
                who_starts = random.choice(two_players)
                two_players.pop(two_players.index(who_starts))
                second_player = two_players[0]
                print(f"{who_starts} will go first.\n")
                player_symbols = self.choose_symbol(who_starts, second_player)
                player_order = {who_starts: player_symbols[0], second_player: player_symbols[1]}
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
        # Error handling loop helper
        symbol_error = False
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
                print(f"{first_player} is {cpu_symbol}, {second_player} is {player_symbol}\n")
                # Returns outcome of chosen symbols
                return cpu_symbol, player_symbol
            case _:
                # Error handling loop
                while not symbol_error:
                    try:
                        # Let first player choose their symbol and capitalise
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
                                print(f"{second_player}, you are O\n")
                                # Returns outcome of chosen symbols
                                return "X", "O"
                            case "O":
                                # Print symbol outcome
                                print(f"{second_player}, you are X\n")
                                # Returns outcome of chosen symbols
                                return "O", "X"

    def player_battle(self, players):
        """
        INCOMPLETE
        :param players:
        :return:
        """

        print(f"It's time to play!")
        graphics.draw_box()

        # Player info unpacking
        player_order = []
        for player in players.keys():
            player_order.append(player)

        play_game = True
        # Turn counter to facilitate symbol display
        turn = 1
        while play_game:
            invalid_choice = False

            if turn % 2 != 0:
                current_player = player_order[0]
            else:
                current_player = player_order[1]

            while not invalid_choice:
                try:
                    if current_player == "CPU":
                        valid_cpu_choice = False
                        while not valid_cpu_choice:
                            cpu_choice = random.choice(range(1, 10))
                            if cpu_choice not in list(self.already_played.keys()):
                                print(f"CPU chose: {cpu_choice}")
                                coordinate_choice = cpu_choice
                                valid_cpu_choice = True
                    else:
                        coordinate_choice = int(input(f"{current_player}, choose a coordinate:    "))
                        if coordinate_choice < 1 or coordinate_choice > 9:
                            raise ValueError
                except ValueError:
                    print("That's not a valid coordinate.")
                else:
                    play_choice = coordinate_choice
                    self.already_played[coordinate_choice] = current_player

                    graphics.update_box(play_choice, players[current_player])

                    graphics.draw_box()

                    # Check if someone has won
                    if turn >= 9:
                        print("No one WINS. Tie.")
                        play_game = False
                    elif turn >= 5:
                        winner = self.find_winner(self.already_played, current_player)
                        if winner:
                            play_game = False

                    turn += 1

                    invalid_choice = True

    def find_winner(self, all_played_symbols, current_player):

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
