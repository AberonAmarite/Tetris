import pygame

INPUT_FIELD_WIDTH = 400
INPUT_FIELD_HEIGHT = 100

BG_COLOR = (0, 0, 0)


class LoginPage:
    def __init__(self, game_view) -> None:
        self.window_size = pygame.display.get_window_size()
        self.input_field = pygame.Rect(self.window_size[0] // 2 - INPUT_FIELD_WIDTH // 2,
                                       self.window_size[1] // 2 - INPUT_FIELD_HEIGHT // 2,
                                       INPUT_FIELD_WIDTH,
                                       INPUT_FIELD_HEIGHT)
        self.game_view = game_view
        self.screen = game_view.screen
        self.user_text = ""
        self.user_text_component = game_view.GameText(self.user_text, (0, 0, 255), 32, self.input_field.x + 15, self.input_field.y + INPUT_FIELD_HEIGHT // 2, game_view)
        self.label = game_view.GameText("Enter your username", (0, 255, 0), 32, game_view.width / 2, 200, game_view)
        self.label_continue = game_view.GameText("Press enter to continue", (0, 255, 0), 32, game_view.width / 2, 500, game_view)
        self.label_best_scores = game_view.GameText("Top 10", (0, 255, 0), 20, 50, 50, game_view, "left")
        self.labels_top_scores = []
        # text, color, font_size, x, y, game_view

    def update(self):
        self.screen.fill(BG_COLOR)
        self.label.update()
        self.label_continue.update()
        self.label_best_scores.update()
        for top_score in self.labels_top_scores:
            top_score.update()
        pygame.draw.rect(self.screen, (255, 0, 0), self.input_field)
        self.user_text_component.update(self.user_text)

    def set_top_scores(self, top_scores):
        common_x = 50
        self.labels_top_scores = [self.game_view.GameText(score, (0, 255, 0), 20, common_x, 100 + index * 50, self.game_view, "left") for index, score in enumerate(top_scores)]
