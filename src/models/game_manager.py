FPS = 60

level_to_total_lines = {
    0: 10,
    1: 30,
    2: 60,
    3: 100,
    4: 150,
    5: 210,
    6: 280,
    7: 360,
    8: 450,
    9: 550,
    10: 650,
    11: 700,
    12: 800,
    13: 900,
    14: 1050,
    15: 1150,
    16: 1260,
    17: 1380,
    18: 1510,
    19: 1650,
    20: 1800,
    21: 1960,
    22: 2130,
    23: 2310,
    24: 2500,
    25: 2700,
    26: 2900,
    27: 3100,
    28: 3300
    # level >= 29 : total_lines += 200
}
level_to_NTSC_FpC = {
    0: 48,
    1: 43,
    2: 38,
    3: 33,
    4: 28,
    5: 23,
    6: 18,
    7: 13,
    8: 8,
    9: 6,
    10: 5,
    11: 5,
    12: 5,
    13: 4,
    14: 4,
    15: 4,
    16: 3,
    17: 3,
    18: 3
    # level >= 19: 2
}
level_to_delay = {key: value * 1000 / FPS for key, value in level_to_NTSC_FpC.items()}


class GameManager:
    def __init__(self) -> None:
        self.level = 0
        self.score = 0
        self.lines_cleared = 0
        self.lines_needed = 10

        self.fps = FPS
        self.delay = int(level_to_delay[self.level])

    def calculate_score(self, lines_cleared):
        lines_to_constant = {
            1: 40,
            2: 100,
            3: 300,
            4: 1200
        }
        return lines_to_constant[lines_cleared] * (self.level + 1)

    def update_lines_cleared(self, lines):
        self.lines_cleared += lines

    def update_score(self, lines_cleared):
        self.score += self.calculate_score(lines_cleared)

    def update_level(self):
        if self.level in level_to_total_lines.keys():
            self.lines_needed = level_to_total_lines[self.level]
        else:
            self.lines_needed += 200
        if self.lines_cleared >= self.lines_needed:
            self.level += 1
            self.update_delay()

    def update_delay(self):
        self.delay = level_to_delay[self.level]

    def update_state(self, lines_cleared):
        if lines_cleared:
            self.update_lines_cleared(lines_cleared)
            self.update_score(lines_cleared)
            self.update_level()
