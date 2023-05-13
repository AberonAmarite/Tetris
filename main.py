import pygame

BG_COLOR = (109, 109, 109)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
green = (0, 255, 0)
blue = (0, 0, 128)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    pygame.display.set_caption('Tetris')

    font = pygame.font.Font('assets/fonts/FiraSans-Bold.ttf', 32)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('Tetris', True, green)

    text_rect = text.get_rect()
    text_rect .center = (SCREEN_WIDTH // 5, SCREEN_HEIGHT // 10)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(BG_COLOR)
        screen.blit(text, text_rect )

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()