import pygame

from src.models.game import Game, LOGIN_PAGE, START_GAME_PAGE, GAME_PAGE
from src.views.game_view import GameView

LOGIN_PAGE = "login"
START_GAME_PAGE = "start_game"
GAME_PAGE = "game"


class GameController:
    def __init__(self, model: Game, view: GameView) -> None:
        self.model = model
        self.view = view
        self.key_actions = {
            'ESCAPE': model.quit,
            'LEFT': lambda: model.move(-1),
            'RIGHT': lambda: model.move(+1),
            'DOWN': model.drop,
            'UP': model.rotate_stone,
            'p': model.toggle_pause,
            'SPACE': model.start_game
        }

    def run(self):
        pygame.time.set_timer(pygame.USEREVENT + 1, self.model.game_manager.delay)
        clock = pygame.time.Clock()
        user_text = ''
        while True:
            self.view.update_view()
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    if self.model.state == GAME_PAGE:
                        self.model.drop()
                elif event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if self.model.state == LOGIN_PAGE:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            if len(user_text) < 20:
                                user_text += event.unicode
                            if event.key == eval("pygame.K_RETURN"):
                                user_text = user_text[:-1]
                                self.model.set_user(user_text)
                                self.view.set_user(user_text)
                                self.model.set_state(START_GAME_PAGE)
                        self.view.update_user_text(user_text)
                    elif self.model.state == START_GAME_PAGE:
                        if event.key == eval("pygame.K_RETURN"):
                            self.model.set_state(GAME_PAGE)
                        elif event.key == eval("pygame.K_RSHIFT"):
                            self.model.set_state(LOGIN_PAGE)
                    elif self.model.state == GAME_PAGE:
                        for key in self.key_actions:
                            if event.key == eval("pygame.K_"
                                                 + key):
                                self.key_actions[key]()
                        if event.key == eval("pygame.K_RSHIFT"):
                            self.model.set_state(START_GAME_PAGE)

            clock.tick(self.model.game_manager.fps)

    def quit(self):
        self.view.quit()
        self.model.quit()
