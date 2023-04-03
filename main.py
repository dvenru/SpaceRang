from sys import exit
import pygame as pg

from settings import *
from scripts.map.galaxy import Galaxy
from scripts.map.planetsystem import PlanetSystem
from scripts.map.connect import Connect
from datacontrol import DataControl

from scripts.UI.label import Label
from scripts.UI.cursorlabel import CursorLabel


class Game:

    def __init__(self):
        # инициализация PyGame
        pg.init()

        self.main_surface = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("SpaceRang")
        # pg.display.set_icon()

        self.clock = pg.time.Clock()
        # инициализация игровых элементов
        self.galaxy = Galaxy(self.main_surface)

        # инициализация интерефейса
        self.fps_label = Label(self.main_surface, (10, 10))
        self.cursor_label = CursorLabel(self.main_surface, color=(0, 0, 0))

        # Тест функционала
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

    def run(self) -> None:
        running = True

        while running:

            # Обработка событий
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    exit()

            # Отрисовка
            self.main_surface.fill((100, 100, 100))
            self.galaxy.draw()

            self.fps_label.set_text(str(int(self.clock.get_fps())))
            self.fps_label.draw()

            self.cursor_label.draw()
            pg.display.flip()

            # Задаем количество кадров в секунду
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
