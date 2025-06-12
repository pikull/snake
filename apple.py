from constants import *
import pygame as pg
import random as r

class Apple:
    def __init__(self):
        loc = r.randint(0, grid_size - 1) * block_size
        self.rect = pg.Rect(loc, loc, block_size, block_size)

    def draw(self, surface):
        pg.draw.rect(surface, "red", self.rect)
