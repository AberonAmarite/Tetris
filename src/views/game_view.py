from src.models.game import Game, COLS, ROWS

import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
CELL_SIZE = 20

COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 120, 0),
    (255, 255, 0),
    (180, 0, 255),
    (0, 220, 220)
]


class GameView:
    def __init__(self, model: Game) -> None:
        super().__init__()
        self.model = model

        self.width = CELL_SIZE * COLS
        self.height = CELL_SIZE * ROWS

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.event.set_blocked(pygame.MOUSEMOTION)  # We do not need

    def update_view(self):
        self.screen.fill((0, 0, 0))
        if self.model.gameover:
            self.center_msg("""Game Over!
    Press space to continue""")
        else:
            if self.model.paused:
                self.center_msg("Paused")
            else:
                self.draw_matrix(self.model.board, (0, 0))
                self.draw_matrix(self.model.stone,
                                 (self.model.stone_x,
                                  self.model.stone_y))
        pygame.display.update()

    def draw_matrix(self, matrix, offset):
        off_x, off_y = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(
                        self.screen,
                        COLORS[val],
                        pygame.Rect(
                            (off_x + x) *
                            CELL_SIZE,
                            (off_y + y) *
                            CELL_SIZE,
                            CELL_SIZE,
                            CELL_SIZE), 0)

    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image = pygame.font.Font(
                pygame.font.get_default_font(), 12).render(
                line, False, (255, 255, 255), (0, 0, 0))

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x //= 2
            msgim_center_y //= 2

            self.screen.blit(msg_image, (
                self.width // 2 - msgim_center_x,
                self.height // 2 - msgim_center_y + i * 22))

    def quit(self):
        self.center_msg("Exiting...")
        pygame.display.update()
