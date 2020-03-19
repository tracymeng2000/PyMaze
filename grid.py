from cell import Cell
from direction import Direction
from random import randint

class Grid:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._grid = self.prepare_grid()
        self.configure_cells()

    @property
    def rows(self):
        return self._rows
    
    @property
    def cols(self):
        return self._cols
    
    @property
    def __len__(self):
        return self._rows * self._cols 

    def __getitem__(self, pos):
        row, col = pos
        if(row in range(0, self.rows) and col in range(0, self.cols)):
            return self._grid[row][col]
        else:
            return None
    
    def __iter__(self):
        self.cur_row = 0
        return self

    def __next__(self):
        if(self.cur_row < self.rows):
            result = self._grid[self.cur_row]
            self.cur_row += 1
            return result
        else:
            raise StopIteration

    def prepare_grid(self):
        return [[Cell(row, col) for col in range(self._cols)] 
                for row in range(self._rows)]
    
    
    def configure_cells(self):
        for row, grid_row in enumerate(self._grid):
            for col, cell in enumerate(grid_row):
                cell.add_neighbor(Direction.north, self[row - 1, col]) 
                cell.add_neighbor(Direction.south, self[row + 1, col])
                cell.add_neighbor(Direction.west, self[row, col - 1])
                cell.add_neighbor(Direction.east, self[row, col + 1])
    
    def random_cell(self):
        row = randint(0, self._rows - 1)
        col = randint(0, self._cols - 1)
        return self[row, col]

    def __str__(self):
        output = '+' + '---+' * self._cols + '\n'
        for row in self._grid:
            top = '|'
            bottom = '+'

            for cell in row:
                if(cell is not None):
                    body = " " * 3
                    east_boundary = ' ' if (cell.linked(cell.east)) else '|'
                    top += body + east_boundary

                    south_boundary = ' ' * 3 if (cell.linked(cell.south)) else '-' * 3
                    corner = '+'
                    bottom += south_boundary + corner
            output += top + '\n'
            output += bottom + '\n'
        return output

    def __repr__(self):
        return str(self)
