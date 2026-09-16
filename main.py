import config
import pygame
import sys

from game import userevent, Conway
from gui import (
    action, 
    draw, 
    layout, 
    GUIConway, 
    GUIPattern
)
from patterns import LIBRARY

def main() -> None:
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")

    cols, rows = 30, 40
    gui_conway = GUIConway(Conway(rows, cols), layout.get_conway_rect(layout.SIMULATION_RECT, rows, cols))
    gui_pattern = GUIPattern(LIBRARY["default"], layout.get_library_rect(layout.LIBRARY_RECT, LIBRARY["default"]))

    timer = int(1000 // config.SPEED)
    
    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.MOUSEBUTTONDOWN:
                    action.action_update_cell(gui_conway.conway, event.button, gui_conway.rectangle)
                    action.action_place_pattern(gui_conway.conway, event.button, gui_conway.rectangle, gui_pattern)
                case pygame.KEYDOWN:
                    action.action_start_pause(gui_conway.conway, event.key, timer)
                    action.action_change_pattern(event.key, layout.LIBRARY_RECT, gui_pattern)
                case userevent.NEXTGENERATION:
                    action.action_next_generation(gui_conway.conway)
                case _:
                    pass

        config.SCREEN.fill((0, 0, 0))
        draw.draw_menu(config.SCREEN, layout.MENU_RECT)
        draw.draw_simulation(config.SCREEN, layout.SIMULATION_RECT)
        draw.draw_cells(config.SCREEN, gui_conway.conway.grid, gui_conway.rectangle)
        draw.draw_library(config.SCREEN, layout.LIBRARY_RECT)
        draw.draw_pattern(config.SCREEN, gui_pattern.pattern, gui_pattern.rectangle)
        pygame.display.flip()
        config.CLOCK.tick(60)

    pygame.quit()
    sys.exit()
    return

if __name__ == "__main__":
    main()
