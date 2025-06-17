import pygame as pg

from constants import *


class Snake:
    def __init__(self):
        self.tobexdir, self.tobeydir = 1, 0
        self.xdir, self.ydir = 0, 0
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
            return

        # self collision
        head = self.body[0]
        for i in range(1, len(self.body) - 1):
            if head.colliderect(self.body[i]):
                self.dead = True
                return
        
        # snake direction
        self.xdir = self.tobexdir
        self.ydir = self.tobeydir

        # snake movement
        new_head_x = self.body[0].x + self.xdir * block_size
        new_head_y = self.body[0].y + self.ydir * block_size
        new_head = pg.Rect(new_head_x, new_head_y, block_size, block_size)
        self.body.insert(0, new_head)
        if self.grow:
            self.grow = False
        else:
            self.body.pop()


    def draw(self, surface):
        for square in self.body:
            pg.draw.rect(surface, "green", square)
