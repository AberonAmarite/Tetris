import sys

import pygame
from random import randrange as rand

from src.models.database import GameDatabase
from src.models.game_manager import GameManager

COLS = 10
ROWS = 20

TETRIS_SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

LOGIN_PAGE = "login"
START_GAME_PAGE = "start_game"
GAME_PAGE = "game"


class Game:
    def __init__(self) -> None:
        self.game_manager = GameManager()
        self.db = GameDatabase()
        self.top_scores = self.db.get_top_scores()
        self.highest_score = ""
        self.recent_score = ""

        self.state = LOGIN_PAGE
        self.username = ""
        pygame.init()
        pygame.key.set_repeat(250, 25)
        pygame.display.set_caption('Tetris')

        self.gameover = False
        self.paused = False

        self.board = None
        self.stone = None
        self.stone_x = None
        self.stone_y = None

        self.bgm = pygame.mixer.Sound("assets/sounds/BGM.mp3")
        self.sound_drop = pygame.mixer.Sound("assets/sounds/Drop.wav")
        self.sound_gameover = pygame.mixer.Sound("assets/sounds/Gameover.wav")
        self.sound_lineclear = pygame.mixer.Sound("assets/sounds/Lineclear.wav")

        self.bgm.play(-1)
        self.init_game()

    def set_user_scores(self, username):
        if username:
            self.highest_score = self.db.get_highest_score(username)
            self.recent_score = self.db.get_most_recent_score(username)

    def set_state(self, state):
        self.state = state

    def set_username(self, name):
        self.username = name

    def set_user(self, name):
        if name:
            self.set_username(name)
            self.set_user_scores(name)

    def drop(self):
        if not self.gameover and not self.paused:
            self.sound_drop.play(0)
            self.stone_y += 1
            if self.check_collision(self.board,
                                    self.stone,
                                    (self.stone_x, self.stone_y)):
                self.board = self.join_matrices(
                    self.board,
                    self.stone,
                    (self.stone_x, self.stone_y))
                self.new_stone()
                lines_removed = 0
                while True:
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = self.remove_row(
                                self.board, i)
                            lines_removed += 1
                            break
                    else:
                        if lines_removed:
                            self.game_manager.update_state(lines_removed)
                            self.sound_lineclear.play(0)
                        break

    def rotate_stone(self):
        if not self.gameover and not self.paused:
            new_stone = self.rotate_clockwise(self.stone)
            if not self.check_collision(self.board,
                                        new_stone,
                                        (self.stone_x, self.stone_y)):
                self.stone = new_stone

    def toggle_pause(self):
        self.paused = not self.paused

    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False

    def move(self, delta_x):
        if not self.gameover and not self.paused:
            new_x = self.stone_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > COLS - len(self.stone[0]):
                new_x = COLS - len(self.stone[0])
            if not self.check_collision(self.board,
                                        self.stone,
                                        (new_x, self.stone_y)):
                self.stone_x = new_x

    def new_stone(self):
        self.stone = TETRIS_SHAPES[rand(len(TETRIS_SHAPES))]
        self.stone_x = int(COLS / 2 - len(self.stone[0]) / 2)
        self.stone_y = 0

        if self.check_collision(self.board,
                                self.stone,
                                (self.stone_x, self.stone_y)):
            self.finish_game()

    def finish_game(self):
        self.gameover = True
        self.sound_gameover.play(0)
        if self.username:
            self.db.insert_score(self.username, self.game_manager.score)

    def init_game(self):
        self.board = self.new_board()
        self.new_stone()

    # noinspection PyMethodMayBeStatic
    def quit(self):
        self.finish_game()
        sys.exit()

    # noinspection PyMethodMayBeStatic
    def rotate_clockwise(self, shape):
        return [[shape[y][x]
                 for y in range(len(shape))]
                for x in range(len(shape[0]) - 1, -1, -1)]

    # noinspection PyMethodMayBeStatic
    def check_collision(self, board, shape, offset):
        off_x, off_y = offset
        for cy, row in enumerate(shape):
            for cx, cell in enumerate(row):
                try:
                    if cell and board[cy + off_y][cx + off_x]:
                        return True
                except IndexError:
                    return True
        return False

    # noinspection PyMethodMayBeStatic
    def remove_row(self, board, row):
        del board[row]
        return [[0 for _ in range(COLS)]] + board

    # noinspection PyMethodMayBeStatic
    def join_matrices(self, mat1, mat2, mat2_off):
        off_x, off_y = mat2_off
        for cy, row in enumerate(mat2):
            for cx, val in enumerate(row):
                mat1[cy + off_y - 1][cx + off_x] += val
        return mat1

    # noinspection PyMethodMayBeStatic
    def new_board(self, ):
        board = [[0 for _ in range(COLS)]
                 for _ in range(ROWS)]

        board += [[8 for _ in range(COLS)]]
        return board
