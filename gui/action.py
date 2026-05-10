import pygame
from typing import Optional
from game import userevent
from game.grid import Conway
from gui import cell

def action_update_cell(conway: Conway, button: int, rect: pygame.Rect) -> None:
    if button != 1:
        return
    
    if conway.running:
        return
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if not rect.collidepoint(mouse_x, mouse_y):
        return
    
    cell_size = cell.get_cell_size(rect, conway.grid)

    col = (mouse_x - rect.x) // cell_size
    row = (mouse_y - rect.y) // cell_size
    conway.update_cell(row, col)
    return

def action_start_pause(conway: Conway, key: int, timer: int) -> None:
    if key != pygame.K_SPACE:
        return
    
    match conway.running:
        case False:
            conway.run()
            pygame.time.set_timer(userevent.NEXTGENERATION, timer)
        case True:
            conway.pause()
            pygame.time.set_timer(userevent.NEXTGENERATION, 0)
    return
