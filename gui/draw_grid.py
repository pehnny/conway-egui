import pygame
from game.grid import Grid
from config.config import CELL_SIZE

def draw_grid(screen: pygame.Surface, grid: Grid, cell_size: int = CELL_SIZE) -> None:
    for row in range(grid.rows):
        for col in range(grid.cols):
            x = col * cell_size
            y = row * cell_size
            
            rect = pygame.Rect(x, y, cell_size, cell_size)

            if grid.get_cell(row, col):
                pygame.draw.rect(screen, (255, 255, 255), rect)
            else:
                pygame.draw.rect(screen, (0, 0, 0), rect)

            pygame.draw.rect(screen, (40, 40, 40), rect, 1)
