from sys import exit
import pygame as pg

from settings import *
from src.map.galaxy import Galaxy
from src.map.planet_system import PlanetSystem
from src.map.connect import Connect


class Game:

    def __init__(self):
        pg.init()

        self.main_surface = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("SpaceRang")
        # pg.display.set_icon()

        self.clock = pg.time.Clock()

        self.galaxy = Galaxy(self.main_surface)

        unix_1 = PlanetSystem(self.main_surface, "normal", "test", 0, (100, 100), "unix_1")
        unix_2 = PlanetSystem(self.main_surface, "normal", "test", 0, (200, 100), "unix_2")
        unix_3 = PlanetSystem(self.main_surface, "normal", "test", 0, (100, 200), "unix_3")
        unix_4 = PlanetSystem(self.main_surface, "normal", "test", 0, (200, 200), "unix_4")

        unix_connect_1 = Connect(self.main_surface, unix_1, unix_2)
        unix_connect_2 = Connect(self.main_surface, unix_2, unix_4)
        unix_connect_3 = Connect(self.main_surface, unix_1, unix_3, False)
        unix_connect_4 = Connect(self.main_surface, unix_2, unix_3)

        self.galaxy.add_system([unix_1, unix_2, unix_3, unix_4])
        self.galaxy.add_connect([unix_connect_1, unix_connect_2, unix_connect_3, unix_connect_4])

        print(self.galaxy.systems)
        print(self.galaxy.connects)

    def run(self):
        running = True

        while running:

            # Обработка событий
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            # Отрисовка
            self.main_surface.fill((100, 100, 100))
            self.galaxy.draw()
            pg.display.flip()

            # Задаем количество кадров в секунду
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
