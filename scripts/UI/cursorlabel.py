import pygame as pg

from scripts.UI.label import Label


class CursorLabel(Label):
    def __init__(self, surface: pg.Surface, position: tuple = (int, int), text: str = "-", size: int = 20, color: tuple = (255, 255, 255)):
        super().__init__(surface, position, text, size, color)

    def draw(self) -> None:
        x_pos, y_pos = pg.mouse.get_pos()
        self.surface.blit(self.render_text, (x_pos, y_pos - 15))
