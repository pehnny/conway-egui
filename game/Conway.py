from game.Grid import Grid
from patterns.Pattern import Pattern

class Conway:
    def __init__(self, rows: int, cols: int) -> None:
        self.grid = Grid(rows, cols)
        self.running = False

    def update_cell(self, row: int, col: int) -> None:
        match self.grid.get_cell(row, col):
            case 0:
                self.grid.set_cell(row, col, 1)
            case 1:
                self.grid.set_cell(row, col, 0)
        return
    
    def border(self, index: int, limit: int) -> int:
        if index < 0:
            return limit + index
        if index >= limit:
            return index - limit
        return index

    def count_neighbours(self, row: int, col: int) -> int:
        count = 0

        for r in range(row-1, row+2):
            n_row = self.border(r, self.grid.rows)
            for c in range(col-1, col+2):
                if c == col and r == row:
                    continue
                n_col = self.border(c, self.grid.cols)
                count += self.grid.get_cell(n_row, n_col)
        return count
    
    def next_generation(self) -> None:
        new_grid = Grid(self.grid.rows, self.grid.cols)

        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                state = self.grid.get_cell(r, c)
                count = self.count_neighbours(r, c)

                match state:
                    case 0:
                        if count == 3:
                            new_grid.set_cell(r, c, 1)
                    case 1:
                        if count in (2, 3):
                            new_grid.set_cell(r, c, 1)
        self.grid = new_grid
        return
    
    def place_pattern(self, row: int, col: int, pattern: Pattern) -> None:
        for x, y in pattern.coordinates:
            p_col = self.border(col + x, self.grid.cols)
            p_row = self.border(row + y, self.grid.rows)

            if self.grid.get_cell(p_row, p_col):
                return
            
        for x, y in pattern.coordinates:
            p_col = self.border(col + x, self.grid.cols)
            p_row = self.border(row + y, self.grid.rows)
            self.grid.set_cell(p_row, p_col, 1)
        return

    def run(self) -> None:
        self.running = True
        return
    
    def pause(self) -> None:
        self.running = False
        return
