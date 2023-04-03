import pygame as pg

from src.map.planet_system import PlanetSystem
from src.map.connect import Connect


class Galaxy:
    def __init__(self, surface):
        self.surface = surface
        self.systems = {}
        self.connects = {}

    def generate_galaxy(self, size: int):
        pass

    def add_system(self, new_systems: list):
        for new_system in new_systems:
            self.systems[new_system.id] = new_system

    def add_connect(self, new_connects: list):
        for new_connect in new_connects:
            self.connects[new_connect.connect_id] = new_connect

    def draw(self):
        for connect in self.connects.values():
            connect.draw()

        for system in self.systems.values():
            system.draw()
