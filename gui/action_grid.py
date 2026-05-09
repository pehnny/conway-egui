from pygame import mouse
from game.grid import Conway
from config.config import CELL_SIZE

def action_update_cell(conway: Conway, button: int, cell_size: int = CELL_SIZE) -> None:
    if button != 1:
        return
    
    mouse_x, mouse_y = mouse.get_pos()
    col = mouse_x // cell_size
    row = mouse_y // cell_size
    conway.update_cell(row, col)
    return
