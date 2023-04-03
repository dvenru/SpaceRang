import pygame as pg
from random import randint

from src.settings import *


class PlanetSystem:
    def __init__(self, surface, system_type: str, system_name: str, planet_count: int, position: tuple = (int, int), set_id: str = None):
        self.surface = surface
        self.id = f"PS{str(randint(100, 1000))}" if set_id is None else set_id
        self.name = system_name
        self.type = system_type
        self.planet_count = planet_count
        self.position = position
        self.connects = []

    def add_connect(self, system_id: str) -> None:
        self.connects.append(system_id)

    def del_connect(self, system_id: str = None) -> None:
        if system_id is None:
            self.connects = []
        else:
            self.connects.remove(system_id)

    def get_connect(self) -> list:
        return self.connects

    def draw(self):
        pg.draw.circle(self.surface, 'white', self.position, 20)
