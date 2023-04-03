import pygame as pg

from scripts.entity.ship import Ship


class Player(Ship):
    def __init__(self, surface: pg.Surface):
        super().__init__(surface)
