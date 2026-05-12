import pygame
from config import config
from gui import cell
from game.Grid import Grid
from patterns.Pattern import Pattern

#   ---------------------------------
#   |              Menu             |
#   ---------------------------------
#   |               |               |
#   |               |               |
#   |   Simulation  |   Library     |
#   |               |               |
#   |               |               |
#   ---------------------------------

MENU_LAYOUT = {
    "x-origin": 0,
    "y-origin": 0,
    "height": 80,
    "width": config.WINDOW_WIDTH,
}

SIMULATION_LAYOUT = {
    "x-origin": 0,
    "y-origin": MENU_LAYOUT["height"],
    "height": config.WINDOW_HEIGHT - MENU_LAYOUT["height"],
    "width": config.WINDOW_WIDTH // 2,  
}

LIBRARY_LAYOUT = {
    "x-origin": SIMULATION_LAYOUT["width"],
    "y-origin": MENU_LAYOUT["height"],
    "height": config.WINDOW_HEIGHT - MENU_LAYOUT["height"],
    "width": config.WINDOW_WIDTH // 2,
}

MENU_RECT = pygame.Rect(
    MENU_LAYOUT["x-origin"],
    MENU_LAYOUT["y-origin"],
    MENU_LAYOUT["width"],
    MENU_LAYOUT["height"],
)

SIMULATION_RECT = pygame.Rect(
    SIMULATION_LAYOUT["x-origin"],
    SIMULATION_LAYOUT["y-origin"],
    SIMULATION_LAYOUT["width"],
    SIMULATION_LAYOUT["height"],
)

LIBRARY_RECT = pygame.Rect(
    LIBRARY_LAYOUT["x-origin"],
    LIBRARY_LAYOUT["y-origin"],
    LIBRARY_LAYOUT["width"],
    LIBRARY_LAYOUT["height"],
)

def get_conway_rect(simulation: pygame.Rect, rows: int, cols: int) -> pygame.Rect:
    cell_size = cell.get_cell_size(simulation, rows, cols)
    offset = cell.get_grid_offset(simulation, rows, cols, cell_size)

    rect = pygame.Rect(
        simulation.left + offset.x,
        simulation.top + offset.y,
        simulation.width - 2*offset.x,
        simulation.height - 2*offset.y
    )

    return rect

def get_pattern_rect(library: pygame.Rect, pattern: Pattern) -> pygame.Rect:
    size = pattern.size()
    cell_size = cell.get_cell_size(library, size, size)
    offset = cell.get_grid_offset(library, size, size, cell_size)

    rect = pygame.Rect(
        library.left + offset.x,
        library.top + offset.y,
        library.width - 2*offset.x,
        library.height - 2*offset.y
    )

    return rect
