import pygame
from game.Grid import Grid

def get_cell_size(simulation: pygame.Rect, rows: int, cols: int) -> tuple[int, int]:
    cell_width = simulation.width // cols
    cell_height = simulation.height // rows

    cell_size = min(cell_width, cell_height)

    return (cell_size, cell_size)

def get_grid_offset(simulation: pygame.Rect, rows: int, cols: int, size: tuple[int, int]) -> pygame.Vector2:
    x, y = size

    max_height = y * rows
    max_width = x * cols

    offset = pygame.Vector2(
        (simulation.width - max_width) // 2,
        (simulation.height - max_height) // 2
    )

    return offset
