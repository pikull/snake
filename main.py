import time as t

import pygame as pg

from apple import Apple
from constants import *
from functions import *
from snake import Snake

# initalize pygame
pg.init()
screen = pg.display.set_mode((screen_size, screen_size))
pg.display.set_caption("Snake")
clock = pg.time.Clock()


# main loop
def main():
    apple = Apple()
    snake = Snake()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                direction(snake, event.key)

        if snake.body[0].colliderect(apple.rect):
            apple = Apple()
            snake.grow = True

        snake.update()

        if snake.dead:
            game_over(screen)
            t.sleep(2)
            running = False
            break

        draw_grid(screen)
        snake.draw(screen)
        apple.draw(screen)

        pg.display.update()
        clock.tick(tick_speed)

    pg.quit()


if __name__ == "__main__":
    main()
