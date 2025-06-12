import pygame as pg
import time as t

from constants import *


def draw_grid(surface):
    surface.fill("black")
    for i in range(grid_size - 1):
        pg.draw.line(
            surface,
            "#3b3b3c",
            (0, (i + 1) * block_size),
            (screen_size, (i + 1) * block_size),
        )
        pg.draw.line(
            surface,
            "#3b3b3c",
            ((i + 1) * block_size, 0),
            ((i + 1) * block_size, screen_size),
        )

def game_over(surface):
    surface.fill("black")

    pg.font.init()

    font = pg.font.SysFont("DIN Alternate", font_size)
    text = font.render("Game Over", True, "white")
    width, height = text.get_rect().w, text.get_rect().h

    ssc = screen_size / 2
    center = (ssc - width / 2, ssc - height / 2)
    surface.blit(text, center)

    pg.display.update()
    
def direction(snake, key):
    if snake.ydir != 1 and (key == pg.K_UP or key == pg.K_w):
        snake.xdir = 0
        snake.ydir = -1
    elif snake.ydir != -1 and (key == pg.K_DOWN or key == pg.K_s):
        snake.xdir = 0
        snake.ydir = 1
    elif snake.xdir != 1 and (key == pg.K_LEFT or key == pg.K_a):
        snake.xdir = -1
        snake.ydir = 0
    elif snake.xdir != -1 and (key == pg.K_RIGHT or key == pg.K_d):
        snake.xdir = 1
        snake.ydir = 0
