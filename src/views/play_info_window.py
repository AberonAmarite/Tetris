import pygame

from src.models.game import Game


class PlayInfo:
    def __init__(self, model: Game, game_view) -> None:
        self.model = model
        self.game_view = game_view
        self.screen = game_view.screen
        self.window_size = pygame.display.get_window_size()
        self.screen_offset = (self.window_size[0] / 2, 0)

    def update(self):

        score_text = self.game_view.font.render('Score: ' + str(self.model.game_manager.score), True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (self.window_size[0] * 3 // 4, self.window_size[1] / 2)
        self.screen.blit(score_text, score_text_rect)

        level_text = self.game_view.font.render('Level: ' + str(self.model.game_manager.level), True, (255, 255, 255))
        level_text_rect = level_text.get_rect()
        level_text_rect.center = (self.window_size[0] * 3 // 4, self.window_size[1] * 3 // 4)
        self.screen.blit(level_text, level_text_rect)