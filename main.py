import pygame
import sys
from gui import draw
from gui import action
from game.Conway import Conway
from config import config
from game import userevent
from gui import layout
from patterns.Pattern import Pattern

def main() -> None:
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")

    cols, rows = 30, 40
    conway = Conway(rows, cols)
    conway_rect = layout.get_conway_rect(layout.SIMULATION_RECT, conway.grid)
    pattern = Pattern()

    timer = int(1000 // config.SPEED)
    
    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.MOUSEBUTTONDOWN:
                    action.action_update_cell(conway, event.button, conway_rect)
                    action.action_place_pattern(conway, event.button, conway_rect, pattern)
                case pygame.KEYDOWN:
                    action.action_start_pause(conway, event.key, timer)
                    action.action_change_pattern(event.key, pattern)
                case userevent.NEXTGENERATION:
                    action.action_next_generation(conway)

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
