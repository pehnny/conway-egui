import pygame
import sys
from gui import draw
from gui.action import action_update_cell, action_start_pause
from game.grid import Conway
from config import config
from game import userevent
from gui import layout

def main() -> None:
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")

    x_size, y_size = 40, 40
    conway = Conway(x_size, y_size)
    conway_rect = layout.get_conway_rect(layout.SIMULATION_RECT, conway.grid)

    timer = int(1000 // config.SPEED)
    
    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.MOUSEBUTTONDOWN:
                    action_update_cell(conway, event.button, conway_rect)
                case pygame.KEYDOWN:
                    action_start_pause(conway, event.key, timer)
                case userevent.NEXTGENERATION:
                    conway.next_generation()

        config.SCREEN.fill((0, 0, 0))
        draw.draw_menu(config.SCREEN, layout.MENU_RECT)
        draw.draw_simulation(config.SCREEN, layout.SIMULATION_RECT)
        draw.draw_library(config.SCREEN, layout.LIBRARY_RECT)
        draw.draw_cells(config.SCREEN, conway.grid, conway_rect)
        pygame.display.flip()
        config.CLOCK.tick(60)

    pygame.quit()
    sys.exit()
    return

if __name__ == "__main__":
    main()
