import sys

import pygame
from random import randrange as rand

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


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.key.set_repeat(250, 25)
        pygame.display.set_caption('Tetris')

        self.gameover = False
        self.paused = False

        self.board = None
        self.stone = None
        self.stone_x = None
        self.stone_y = None

        self.init_game()

    def drop(self):
        if not self.gameover and not self.paused:
            self.stone_y += 1
            if self.check_collision(self.board,
                                    self.stone,
                                    (self.stone_x, self.stone_y)):
                self.board = self.join_matrices(
                    self.board,
                    self.stone,
                    (self.stone_x, self.stone_y))
                self.new_stone()
                while True:
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = self.remove_row(
                                self.board, i)
                            break
                    else:
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
            self.gameover = True

    def init_game(self):
        self.board = self.new_board()
        self.new_stone()

    # noinspection PyMethodMayBeStatic
    def quit(self):
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

        board += [[1 for _ in range(COLS)]]
        return board
