import pygame
from dataclasses import dataclass
from game import Conway

@dataclass
class GUIConway:
    conway: Conway
    rectangle: pygame.Rect
