import pygame
from dataclasses import dataclass
from patterns import Pattern
from gui import cell, layout

@dataclass
class GUIPattern:
    pattern: Pattern
    rectangle: pygame.Rect

    def get_pattern_rect(self, library: pygame.Rect, pattern: Pattern) -> pygame.Rect:
        pattern_size = pattern.get_size()
        cell_size = cell.get_cell_size(library, pattern_size, pattern_size)
        offset = cell.get_grid_offset(library, pattern_size, pattern_size, cell_size)

        rect = pygame.Rect(
            library.left + offset.x,
            library.top + offset.y,
            library.width - 2*offset.x,
            library.height - 2*offset.y
        )

        return rect

    def update(self, pattern: Pattern, library: pygame.Rect):
        self.pattern = pattern
        self.rectangle = layout.get_library_rect(library, pattern)
        return
