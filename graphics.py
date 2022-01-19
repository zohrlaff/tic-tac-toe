class Graphix:
    def __init__(self):
        self.title = '''
 _______  ___   _______         _______  _______  _______         _______  _______  _______ 
|       ||   | |       |       |       ||   _   ||       |       |       ||       ||       |
|_     _||   | |       | ____  |_     _||  |_|  ||       | ____  |_     _||   _   ||    ___|
  |   |  |   | |       ||____|   |   |  |       ||       ||____|   |   |  |  | |  ||   |___ 
  |   |  |   | |      _|         |   |  |       ||      _|         |   |  |  |_|  ||    ___|
  |   |  |   | |     |_          |   |  |   _   ||     |_          |   |  |       ||   |___ 
  |___|  |___| |_______|         |___|  |__| |__||_______|         |___|  |_______||_______|

'''
        self.p = [position for position in range(1, 10)]
        self.tictactoe_display = f"\n   |   | X \n" \
                                 "---|---|---\n" \
                                 f"   | O |   \n" \
                                 "---|---|---\n" \
                                 f" X |   |   \n\n"

    def set_box(self):
        self.p = [position for position in range(1, 10)]

    def draw_box(self):
        """
        Creates 3x3 graphic containing coordinates and already 'played' slots.
        """
        box = f"\n {self.p[0]} | {self.p[1]} | {self.p[2]} \n" \
              "---|---|---\n" \
              f" {self.p[3]} | {self.p[4]} | {self.p[5]} \n" \
              "---|---|---\n" \
              f" {self.p[6]} | {self.p[7]} | {self.p[8]} \n"

        print(box)

    def update_box(self, play_choice: int, play_symbol: str):
        """
        Update graphics with player choices.

        :param play_choice: Coordinate chose by player
        :param play_symbol: Player's symbol to be added to on-screen graphic
        """
        self.p[play_choice] = play_symbol
