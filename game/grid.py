class Grid:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def _is_valid_cell(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def get_grid(self) -> list[list[int]]:
        return self.grid
    
    def get_cell(self, row: int, col: int) -> int:
        if not self._is_valid_cell(row, col):
            return 0
        return self.grid[row][col]
    
    def set_cell(self, row: int, col: int, value: int) -> None:
        if not self._is_valid_cell(row, col):
            return
        self.grid[row][col] = value
        return

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

        for x in range(row-1, row+2):
            n_row = self.border(x, self.grid.rows)
            for y in range(col-1, col+2):
                if y == col and x == row:
                    continue
                n_col = self.border(y, self.grid.cols)
                count += self.grid.get_cell(n_row, n_col)
        return count
    
    def next_generation(self) -> None:
        new_grid = Grid(self.grid.rows, self.grid.cols)

        for col in range(self.grid.cols):
            for row in range(self.grid.rows):
                state = self.grid.get_cell(row, col)
                count = self.count_neighbours(row, col)

                match state:
                    case 0:
                        if count == 3:
                            new_grid.set_cell(row, col, 1)
                    case 1:
                        if count in (2, 3):
                            new_grid.set_cell(row, col, 1)
        self.grid = new_grid
        return

    def run(self) -> None:
        self.running = True
        return
    
    def pause(self) -> None:
        self.running = False
        return
