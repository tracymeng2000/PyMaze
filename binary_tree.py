from grid import Grid
from cell import Cell
from random import choice


def on(grid):
    for grid_row in grid:
        for cell in grid_row:
            neighbors = []
            if(cell.east is not None): neighbors.append(cell.east)
            if(cell.north is not None): neighbors.append(cell.north)
            if len(neighbors) > 0 :
                neighbor = choice(neighbors)
                cell.link(neighbor)