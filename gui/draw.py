import pygame
from game.Grid import Grid
from gui import cell
from patterns.Pattern import Pattern

def draw_menu(screen: pygame.Surface, menu: pygame.Rect, color: pygame.Color = pygame.Color(30, 30, 30)) -> None:
    pygame.draw.rect(screen, color, menu)
    return

def draw_simulation(screen: pygame.Surface, simulation: pygame.Rect, color: pygame.Color = pygame.Color(0, 0, 0)) -> None:
    pygame.draw.rect(screen, color, simulation)
    return

def draw_library(screen: pygame.Surface, library: pygame.Rect, color: pygame.Color = pygame.Color(50, 50, 50)) -> None:
    pygame.draw.rect(screen, color, library)
    return

def draw_cells(screen: pygame.Surface, grid: Grid, rect: pygame.Rect) -> None:
    cell_size = cell.get_cell_size(rect, grid)

    for row in range(grid.rows):
        for col in range(grid.cols):
            x = col * cell_size + rect.x 
            y = row * cell_size + rect.y
            
            cell_rect = pygame.Rect(x, y, cell_size, cell_size)

            if grid.get_cell(row, col):
                pygame.draw.rect(screen, (255, 255, 255), cell_rect)
            else:
                pygame.draw.rect(screen, (0, 0, 0), cell_rect)

            pygame.draw.rect(screen, (40, 40, 40), cell_rect, 1)
    return

def draw_pattern(screen: pygame.Surface, grid: Grid, rect: pygame.Rect, pattern: Pattern) -> None:
    pass
