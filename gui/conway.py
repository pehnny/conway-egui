import pygame
from dataclasses import dataclass
from game.Conway import Conway

@dataclass
class GUIConway:
    conway: Conway
    rectangle: pygame.Rect
