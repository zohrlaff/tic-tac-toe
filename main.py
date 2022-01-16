from brain import Brain
from graphics import Graphix

# Graphics Class handles all artwork
graphics = Graphix()

print(graphics.title, "\nChoose a coordinate number to fill the tic-tac-toe in with your symbol.",
      "\nPlace three in a row to "
      "win!\n", graphics.tictactoe_display)

# Brain Class does heavy lifting. It handles counting players, choosing symbols, and taking turns
cpu = Brain()

# Once 1 or 2 players are chosen (.player_counts()), the first turn will commence
game_on = True
while game_on:
    cpu.first_turn(cpu.player_counts())

    try:
        restart_game = input("Play again? Y or N:    \n").upper()
        if restart_game not in ["Y", "N"]:
            raise ValueError
    except ValueError:
        print("Choose between X or O only.")
    else:
        if restart_game == "Y":
            game_on = True
        else:
            game_on = False

# TODO 4. Refactor
