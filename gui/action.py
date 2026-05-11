import pygame
from game import userevent
from game.Conway import Conway
from gui import cell
from patterns import library
from patterns.Pattern import Pattern

def action_update_cell(conway: Conway, button: int, hitbox: pygame.Rect) -> None:
    if button != pygame.BUTTON_LEFT:
        return
    
    if conway.running:
        return
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if not hitbox.collidepoint(mouse_x, mouse_y):
        return
    
    cell_size = cell.get_cell_size(hitbox, conway.grid)

    col = (mouse_x - hitbox.x) // cell_size
    row = (mouse_y - hitbox.y) // cell_size
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

def action_next_generation(conway: Conway) -> None:
    if not conway.running:
        return
    conway.next_generation()
    return

def action_change_pattern(key: int, pattern: Pattern) -> None:
    match key:
        case pygame.K_g:
            pattern.set_pattern(library.GLIDER)
        case _:
            return
    return

def action_place_pattern(conway: Conway, button: int, hitbox: pygame.Rect, pattern: Pattern) -> None:
    if button != pygame.BUTTON_RIGHT:
        return
        
    if conway.running:
        return
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if not hitbox.collidepoint(mouse_x, mouse_y):
        return
    
    cell_size = cell.get_cell_size(hitbox, conway.grid)

    col = (mouse_x - hitbox.x) // cell_size
    row = (mouse_y - hitbox.y) // cell_size
    
    conway.place_pattern(row, col, pattern)
    return
