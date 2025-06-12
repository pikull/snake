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

        if snake.dead:
            game_over(screen)
            running = False
            break

        draw_grid(screen)
        apple.draw(screen)
        snake.draw(screen)

        pg.display.update()
        clock.tick(10)

    pg.quit()


if __name__ == "__main__":
    main()
