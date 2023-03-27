from sys import exit
import pygame as pg

from settings import *


class Game:

    def __init__(self):
        pg.init()

        self.main_surface = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("SpaceRang")
        # pg.display.set_icon()

        self.clock = pg.time.Clock()

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def draw(self):
        self.main_surface.fill((100, 100, 100))
        pg.display.flip()

    def run(self):
        running = True

        while running:

            self.update()

            self.draw()

            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
