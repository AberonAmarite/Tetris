from src.models.game import Game, LOGIN_PAGE, START_GAME_PAGE, GAME_PAGE
import pygame

from src.views.login_page import LoginPage
from src.views.play_info_window import PlayInfo
from src.views.play_window import PlayArea
from src.views.start_game_page import StartGamePage

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720


class GameView:
    class GameText:
        def __init__(self, text, color, font_size, x, y, game_view):
            self.screen = game_view.screen
            self.color = color
            self.font = pygame.font.Font('assets/fonts/FiraSans-Bold.ttf', font_size)
            self.text = game_view.font.render(text, True, color)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (x, y)

        def update(self, text=None):
            if text:
                self.text = self.font.render(text, True, self.color)
            self.screen.blit(self.text, self.text_rect)

    def __init__(self, model: Game) -> None:
        super().__init__()
        self.model = model

        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font = pygame.font.Font('assets/fonts/FiraSans-Bold.ttf', 32)
        self.play_info = PlayInfo(model, self)
        self.play_area = PlayArea(model, self)
        self.login_page = LoginPage(self)
        self.login_page.set_top_scores(self.model.top_scores)
        self.start_game_page = StartGamePage(self)

        pygame.event.set_blocked(pygame.MOUSEMOTION)  # We do not need

    def update_view(self):
        if self.model.state == LOGIN_PAGE:
            self.login_page.update()
        elif self.model.state == START_GAME_PAGE:
            self.start_game_page.update()
        elif self.model.state == GAME_PAGE:
            self.play_area.update()
            self.play_info.update()
        pygame.display.update()

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

    def update_user_text(self, user_text):
        self.login_page.user_text = user_text

    def quit(self):
        self.center_msg("Exiting...")
        pygame.display.update()

    def set_user(self, name):
        if name:
            self.start_game_page.set_username(name)
            self.start_game_page.set_scores(self.model.highest_score, self.model.recent_score)


