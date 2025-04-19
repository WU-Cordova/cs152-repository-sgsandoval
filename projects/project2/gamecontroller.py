# GameController Class

from grid import Grid

class GameController:
    def __init__(self, grid: Grid, sleep_time: float = 1.0) -> None:
        self.grid = grid
        self.history = []
        self.mode = "automatic"
        self.paused = False
        self.sleep_time = sleep_time
        self.user_input = " "

    def run(self) -> None:
        while True:
            if key_pressed == "Q":
                break
            if key_pressed == "S":
                self.mode = "manual"
            if key_pressed == "A":
                self.mode = "automatic"
            if self.mode == "automatic":
                time.sleep(self.sleep_time)
            self.grid.update_grid()
            self.grid.add_to_history()
            if self.grid.is_stable():
                break
            if self.detect_repeating_patterns():
                break
            self.display_grid()
            if self.mod == "manual":
                self.wait_for_user_input()

    def display_grid(self) -> None:
        print(self.grid)

    def wait_for_user_input(self) -> None:
        user_input = input("Press 'S' to step, 'A' for automatic, or 'Q' to quit").strip().lower()
        if user_input == 's':
            self.mode = "manual"
        elif user_input == 'a':
            self.mode = "automatic"
        elif user_input == 'q':
            exit()
    
    def toggle_pause(self) -> None:
        self.paused = not self.paused
        if self.paused:
            print("paused")
        else:
            print("resumed")
    
    def restart_simulation(self) -> None:
        print("restarting")
        self.grid = Grid(self.grid.rows, self.grid.cols)
        self.history.clear()
        self.run()