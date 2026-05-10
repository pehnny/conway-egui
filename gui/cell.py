import pygame
from game import grid

def get_cell_size(simulation: pygame.Rect, grid: grid.Grid) -> int:
    cell_width = simulation.width // grid.cols
    cell_height = simulation.height // grid.rows

    return min(cell_width, cell_height)

def get_offset(simulation: pygame.Rect, grid: grid.Grid) -> pygame.Vector2:
    cell_size = get_cell_size(simulation, grid)
    
    max_height = cell_size * grid.rows
    max_width = cell_size * grid.cols

    offset = pygame.Vector2(
        (simulation.width - max_width) // 2,
        (simulation.height - max_height) // 2
    )

    return offset
