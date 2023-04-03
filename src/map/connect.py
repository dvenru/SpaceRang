import pygame as pg

from src.map.planet_system import PlanetSystem


class Connect:
    def __init__(self, surface, start_system: PlanetSystem, end_system: PlanetSystem, is_open: bool = True):
        self.surface = surface
        self.connect_id = f"C{start_system.id}-{end_system.id}"
        self.start_system_id = start_system.id
        self.end_system_id = end_system.id
        self.start_system_position = start_system.position
        self.end_system_position = end_system.position
        self.is_open = is_open

        start_system.add_connect(end_system.id)
        end_system.add_connect(start_system.id)

    def set_state(self, new_state: bool):
        self.is_open = new_state

    def draw(self):
        pg.draw.line(self.surface, "white" if self.is_open else "red", self.start_system_position, self.end_system_position, 5)
