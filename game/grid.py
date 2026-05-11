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


