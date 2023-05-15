import pygame

from src.models.game import Game

actions = [
    "ESCAPE: QUIT_GAME",
    "ARROW LEFT: MOVE LEFT",
    "ARROW RIGHT: MOVE RIGHT",
    "ARROW DOWN: GO DOWN",
    "ARROW UP: ROTATE",
    "p: PAUSE",
    "SPACE: RESTART",
    "RIGHT SHIFT: GO BACK"
]


class PlayInfo:
    def __init__(self, model: Game, game_view) -> None:
        self.model = model
        self.game_view = game_view
        self.screen = game_view.screen
        self.window_size = pygame.display.get_window_size()
        self.screen_offset = (self.window_size[0] / 2, 0)

        common_x = self.window_size[0] * 9 // 10
        self.score_text = game_view.GameText("Score: 0", (255, 255, 255), 32, common_x, 100, game_view,  "right")
        self.level_text = game_view.GameText("Level: 0", (255, 255, 255), 32, common_x, 180, game_view, "right")
        self.lines_text = game_view.GameText("Lines: 0", (255, 255, 255), 32, common_x, 260, game_view, "right")

        self.action_texts = [game_view.GameText(action, (0, 255, 0), 20, common_x, 350+index*50, game_view, "right")
                             for index, action in enumerate(actions)]

    def update(self):
        self.score_text.update("Score: " + str(self.model.game_manager.score))
        self.level_text.update("Level: " + str(self.model.game_manager.level))
        self.lines_text.update("Lines: " + str(self.model.game_manager.lines_cleared))

        for action_text in self.action_texts:
            action_text.update()

