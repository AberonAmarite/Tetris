import pygame

BG_COLOR = (0, 0, 0)


class StartGamePage:
    def __init__(self, game_view) -> None:
        self.game_view = game_view
        self.window_size = pygame.display.get_window_size()
        self.screen = game_view.screen
        self.label = game_view.GameText("Press enter to continue", (0, 255, 0), 20, game_view.width / 2, 200, game_view)

        self.label_highest_score = None
        self.label_recent_score = None

        self.username = ""
        self.username_text = None

    def update(self):
        self.screen.fill(BG_COLOR)
        self.label.update()
        if self.username:
            self.username_text.update()
            self.label_highest_score.update()
            self.label_recent_score.update()

    def set_username(self, name):
        self.username = name
        self.username_text = self.game_view.GameText(self.username, (0, 255, 0), 20, self.game_view.width / 2, 100,
                                                     self.game_view)

    def set_scores(self, highest, recent):
        self.label_highest_score = self.game_view.GameText(highest, (0, 255, 0), 20, self.game_view.width / 2, 300,
                                                           self.game_view)
        self.label_recent_score = self.game_view.GameText(recent, (0, 255, 0), 20, self.game_view.width / 2, 400,
                                                          self.game_view)
