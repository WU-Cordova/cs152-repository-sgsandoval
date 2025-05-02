# Class: Grid

from typing import List
from cell import Cell
from datastructures.array2d import Array2D

class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.cells = Array2D([[Cell(row, col) for col in range(cols)] for row in range(rows)])
        self.scratch_grid = Array2D([[Cell(row, col) for col in range(cols)] for row in range(rows)])
        self.history: List[List[List[bool]]] = []

    def get_neighbors(self, row: int, col:int) -> List[Cell]:
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbor_row = row + i
                neighbor_col = col + j
                if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols:
                    neighbors.append(self.cells[neighbor_row][neighbor_col])
                    return neighbors
                
    def update_grid(self) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = sum(1 for neighbor in self.get_neighbors(row, col) if neighbor.is_alive())
                self.scratch_grid[row][col].next_state(live_neighbors)
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].state = self.scratch_grid[row][col].state

    def add_to_history(self) -> None:
        grid_snapshot = [[cell.state for cell in row] for row in self.cells]
        self.history.append(grid_snapshot)
        if len(self.history) > 5:
            self.history.pop(0)
    
    def is_stable(self) -> bool:
        if len(self.history) < 2:
            return False
        return self.history[-1] == self.history[-2]
    
    def __str__(self) -> str:
        return "\n".join(" ".join(str(cell.state) for cell in row) for row in self.cells)