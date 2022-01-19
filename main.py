from brain import Brain
from graphics import Graphix
import time

# Graphics Class handles all artwork
graphics = Graphix()

print(graphics.title)
time.sleep(.6)
print("\nChoose a coordinate number to fill the tic-tac-toe in with your symbol.",
      "\nPlace three in a row to "
      "win!\n", graphics.tictactoe_display)
time.sleep(3)

# Brain Class does heavy lifting. It handles counting players, choosing symbols, and taking turns
cpu = Brain()

# Once 1 or 2 players are chosen (.player_count()), the first turn will commence
game_on = True
while game_on:
    cpu.first_turn(cpu.player_count())

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

# TODO 1. Fix time() stuff
