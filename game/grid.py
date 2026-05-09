class Grid:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[False for _ in range(cols)] for _ in range(rows)]

    def get_grid(self) -> list[list[bool]]:
        return self.grid
    
    def get_cell(self, row: int, col: int) -> bool:
        return self.grid[row][col]
    
    def set_cell(self, row: int, col: int, value: bool) -> None:
        self.grid[row][col] = value

class Conway:
    def __init__(self, rows: int, cols: int) -> None:
        self.grid = Grid(rows, cols)

    def update_cell(self, row: int, col: int) -> None:
        if row < 0 or row >= self.grid.rows :
            return
        
        if col < 0 or col >= self.grid.cols :
            return

        match self.grid.get_cell(row, col):
            case False:
                self.grid.set_cell(row, col, True)
            case True:
                self.grid.set_cell(row, col, False)
        return
