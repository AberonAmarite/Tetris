import sys

import pygame

from src.models.game import Game
from src.views.game_view import GameView

DELAY = 750
FPS = 60


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
        pygame.time.set_timer(pygame.USEREVENT + 1, DELAY)
        clock = pygame.time.Clock()
        while True:
            self.view.update_view()

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    self.model.drop()
                elif event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    for key in self.key_actions:
                        if event.key == eval("pygame.K_"
                                             + key):
                            self.key_actions[key]()

            clock.tick(FPS)

    def quit(self):
        self.view.quit()
        self.model.quit()

