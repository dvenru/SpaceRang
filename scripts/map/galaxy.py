import pygame as pg

from scripts.map.planetsystem import PlanetSystem
from scripts.map.connect import Connect


class Galaxy:
    def __init__(self, surface: pg.Surface):
        self.surface = surface
        self.systems = {}
        self.connects = {}

    def generate_galaxy(self, size: int) -> None:
        pass

    def add_system(self, new_systems: list) -> None:
        for new_system in new_systems:
            self.systems[new_system.id] = new_system

    def add_connect(self, new_connects: list) -> None:
        for new_connect in new_connects:
            self.connects[new_connect.connect_id] = new_connect

    def search_system(self, system_id: str) -> str:
        try:
            return self.systems[system_id].name
        except KeyError:
            print("Такой системы не существует")

    def draw(self) -> None:
        for connect in self.connects.values():
            connect.draw()

        for system in self.systems.values():
            system.draw()
