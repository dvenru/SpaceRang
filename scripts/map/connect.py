import pygame as pg

from scripts.map.planetsystem import PlanetSystem
from settings import *


class Connect:
    def __init__(self, surface: pg.Surface, start_system: PlanetSystem, end_system: PlanetSystem, is_open: bool = True):
        self.surface = surface
        self.connect_id = f"C{start_system.id}-{end_system.id}"
        self.start_system = start_system
        self.end_system = end_system
        self.start_system_position = start_system.position
        self.end_system_position = end_system.position
        self.is_open = is_open

        start_system.set_connect(end_system.id, is_open)
        end_system.set_connect(start_system.id, is_open)

    def set_state(self, new_state: bool) -> None:
        self.is_open = new_state
        self.start_system.set_connect(self.end_system.id, new_state)
        self.end_system.set_connect(self.start_system.id, new_state)

    def draw(self) -> None:
        pg.draw.line(self.surface, "white" if self.is_open else "red", self.start_system_position, self.end_system_position, WIDTH_LINE)
