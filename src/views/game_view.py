from src.models.game import Game, COLS, ROWS

import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
CELL_SIZE = 30

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
GAME_BORDER_COLOR = (255, 215, 0)
GAME_BG_COLOR = (109, 109, 109)

STONE_BORDER_COLOR = (255, 215, 0)


class GameView:
    def __init__(self, model: Game) -> None:
        super().__init__()
        self.model = model

        self.width = CELL_SIZE * COLS
        self.height = CELL_SIZE * ROWS

        self.board_offset = (
            (WINDOW_WIDTH/2 - self.width) / 2,
            (WINDOW_HEIGHT - self.height) / 2,
        )

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.event.set_blocked(pygame.MOUSEMOTION)  # We do not need

    def update_view(self):
        self.screen.fill(GAME_BG_COLOR)
        pygame.draw.rect(
            self.screen,
            GAME_BORDER_COLOR,
            pygame.Rect(self.board_offset[0], self.board_offset[1], self.width, self.height), 1)

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
                        pygame.Rect(rect_info), 1)

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
