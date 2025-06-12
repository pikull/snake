import pygame as pg

from constants import *


class Snake:
    def __init__(self):
        self.xdir, self.ydir = 1, 0
        self.body = [
            pg.Rect(block_size * 2, block_size, block_size, block_size),
            pg.Rect(block_size, block_size, block_size, block_size),
        ]

        self.dead = False
        self.grow = False

    def update(self):
        # boundary check
        xpos, ypos = self.body[0].x / block_size, self.body[0].y / block_size
        if not (0 <= xpos < grid_size and 0 <= ypos < grid_size):
            self.dead = True

        # self collision
        head = self.body[0]
        for i in range(1, len(self.body) - 1):
            if head.x == self.body[i].x and head.y == self.body[i].y:
                self.dead = True

    def draw(self, surface):
        for square in self.body:
            pg.draw.rect(surface, "green", square)
