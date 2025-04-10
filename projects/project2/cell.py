# Class: Cell

class Cell:
    def __init__(self, row: int, col: int, state: bool = False) -> None:
        self.row = row
        self.col = col
        self.state = state
    
    def is_alive(self) -> bool:
        return self.state
    
    def set_alive(self) -> None:
        self.state = True

    def set_dead(self) -> None:
        self.state = False

    def next_state(self, live_neighbors: int) -> None:
        if self.state:
            if live_neighbors < 2 or live_neighbors > 3:
                self.set_dead()
        else:
            if live_neighbors == 3:
                self.set_alive()
    
    def __str__(self) -> str:
        return "🦠" if self.state else "."
