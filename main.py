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
cpu.first_turn(cpu.player_counts())

# Draw tictactoe box with coordinates
graphics.draw_box()

####
# TODO 1. FIGURE OUT HOW TO FIND WINNER, LOSER, AND TIE
####

# TODO 2. GUI
# TODO 3. Program CPU 'player'
# TODO 4. Refactor
