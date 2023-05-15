import pygame

from src.models.game import Game, COLS, ROWS

COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 120, 0),
    (255, 255, 0),
    (180, 0, 255),
    (0, 220, 220),
]
GAME_BORDER_COLOR = (0, 0, 0)
GAME_BG_COLOR = (50, 50, 50)

STONE_BORDER_COLOR = (0, 0, 0)
CELL_SIZE = 30


class PlayArea:
    def __init__(self, model: Game, game_view) -> None:
        self.model = model
        self.game_view = game_view
        self.screen = game_view.screen

        self.width = CELL_SIZE * COLS
        self.height = CELL_SIZE * ROWS

        self.window_size = pygame.display.get_window_size()

        self.board_offset = (
            (self.window_size[0] / 2 - self.width) / 2,
            (self.window_size[1] - self.height) / 2,
        )

    def update(self):
        self.screen.fill(GAME_BG_COLOR)
        pygame.draw.rect(
            self.screen,
            GAME_BORDER_COLOR,
            pygame.Rect(self.board_offset[0], self.board_offset[1], self.width, self.height), 5)

        if self.model.gameover:
            self.game_view.center_msg("""Game Over! Press space to continue""")
        else:
            if self.model.paused:
                self.game_view.center_msg("Paused")
            else:
                self.draw_matrix(self.model.board, (0, 0))
                self.draw_matrix(self.model.stone,
                                 (self.model.stone_x,
                                  self.model.stone_y))

    def draw_matrix(self, matrix, offset):
        off_x, off_y = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val and val != 8:
                    rect_info = ((off_x + x) * CELL_SIZE + self.board_offset[0],
                                 (off_y + y) * CELL_SIZE + self.board_offset[1],
                                 CELL_SIZE,
                                 CELL_SIZE)
                    pygame.draw.rect(
                        self.screen,
                        COLORS[val],
                        pygame.Rect(rect_info), 0)
                    pygame.draw.rect(
                        self.screen,
                        STONE_BORDER_COLOR,
                        pygame.Rect(rect_info), 5)
