import pygame
import sys
from gui.draw_grid import draw_grid
from gui.action_grid import action_update_cell
from game.grid import Conway
from config import config

def main() -> None:
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")

    conway = Conway(config.HEIGTH // config.CELL_SIZE, config.WIDTH // config.CELL_SIZE)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                action_update_cell(conway, event.button)

        config.SCREEN.fill((0, 0, 0))

        draw_grid(config.SCREEN, conway.grid)

        pygame.display.flip()
        config.CLOCK.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
