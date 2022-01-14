class Graphix:
    def __init__(self):
        self.slots = 9
        self.title = '''
 _______  ___   _______         _______  _______  _______         _______  _______  _______ 
|       ||   | |       |       |       ||   _   ||       |       |       ||       ||       |
|_     _||   | |       | ____  |_     _||  |_|  ||       | ____  |_     _||   _   ||    ___|
  |   |  |   | |       ||____|   |   |  |       ||       ||____|   |   |  |  | |  ||   |___ 
  |   |  |   | |      _|         |   |  |       ||      _|         |   |  |  |_|  ||    ___|
  |   |  |   | |     |_          |   |  |   _   ||     |_          |   |  |       ||   |___ 
  |___|  |___| |_______|         |___|  |__| |__||_______|         |___|  |_______||_______|

'''
        self.tictactoe_display = f"\n   |   | X \n" \
                                 "---|---|---\n" \
                                 f"   | X |   \n" \
                                 "---|---|---\n" \
                                 f" X |   |   \n\n"
        self.p = [position for position in range(1, 10)]

    def draw_box(self):
        box = f"\n {self.p[0]} | {self.p[1]} | {self.p[2]} \n" \
              "---|---|---\n" \
              f" {self.p[3]} | {self.p[4]} | {self.p[5]} \n" \
              "---|---|---\n" \
              f" {self.p[6]} | {self.p[7]} | {self.p[8]} \n"

        print(box)

    def update_box(self, play_choice: int, play_symbol: str):
        # Update box here with player choices
        self.p[play_choice - 1] = play_symbol
