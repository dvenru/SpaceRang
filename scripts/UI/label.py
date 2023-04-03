import pygame as pg

from settings import *


class Label:
    def __init__(self, surface: pg.Surface, position: tuple = (0, 0), text: str = "-", size: int = 20, color: tuple = (255, 255, 255)):
        self.surface = surface
        self.text = text
        self.size = size
        self.color = color
        self.position = position

        self.font = pg.font.Font(DEFAULT_FONT, size)
        self.render_text = self.font.render(text, False, color)

    def draw(self) -> None:
        self.surface.blit(self.render_text, self.position)

    def set_text(self, text: str, color: tuple = None) -> None:
        self.render_text = self.font.render(text, False, self.color if color is None else color)
