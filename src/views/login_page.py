import pygame

INPUT_FIELD_WIDTH = 400
INPUT_FIELD_HEIGHT = 100


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
        self.user_text_component = game_view.GameText(self.user_text, (0, 0, 255), 30, self.input_field.x + 15, self.input_field.y + INPUT_FIELD_HEIGHT // 2, game_view)
        self.label = game_view.GameText("Enter your username", (0, 255, 0), 20, game_view.width / 2, 200, game_view)
        self.label_continue = game_view.GameText("Press enter to continue", (0, 255, 0), 20, game_view.width / 2, 500, game_view)

        # text, color, font_size, x, y, game_view

    def update(self):
        self.label.update()
        self.label_continue.update()
        pygame.draw.rect(self.screen, (255, 0, 0), self.input_field)
        self.user_text_component.update(self.user_text)
       # text_surface = self.game_view.font.render(self.user_text, True, (255, 255, 255))
      #  self.screen.blit(text_surface, (self.input_field.x + 5, self.input_field.y + 5))

