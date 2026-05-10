class Grid:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_grid(self) -> list[list[int]]:
        return self.grid
    
    def get_cell(self, row: int, col: int) -> int:
        return self.grid[row][col]
    
    def set_cell(self, row: int, col: int, value: int) -> None:
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

    def count_neighbours(self, row: int, col: int) -> int:
        count = 0

        for n_r in range(row-1, row+2):
            if n_r < 0 or n_r >= self.grid.rows:
                continue

            for n_c in range(col-1, col+2):
                if n_c < 0 or n_c >= self.grid.cols:
                    continue

                if n_c == col and n_r == row:
                    continue

                count += self.grid.get_cell(n_r, n_c)
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
