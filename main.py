

from src.controllers.game_controller import GameController
from src.models.game import Game
from src.views.game_view import GameView


def main() -> None:
    model = Game()
    view = GameView(model)
    controller = GameController(model, view)
    controller.run()


if __name__ == "__main__":
    main()

