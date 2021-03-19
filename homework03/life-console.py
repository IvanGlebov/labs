import curses
import time
import argparse

from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife, speed) -> None:
        super().__init__(life)
        self.speed = speed/100

    def draw_borders(self, screen) -> None:
        # """ Отобразить рамку. """
        firstRow = "+" + str("-" * self.life.cols) + "+"
        screen.addstr(0, 0, firstRow)
        # screen.addstr("SIMPLE STRING")
        for i in range(self.life.rows):
            screen.addstr(i+1, 0, "|" + str(" " * self.life.cols) + "|")
        screen.addstr(self.life.rows+1, 0, firstRow)
        # screen.refresh()



    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        pass
        for row_number in range(self.life.rows):
            row_to_print = ""
            for col_number in range(self.life.cols):
                if self.life.curr_generation[row_number][col_number] == 1:
                    row_to_print += "*"
                else:
                    row_to_print += " "
            screen.addstr(row_number+1, 1, row_to_print)
            # screen.refresh()

    def run(self) -> None:
        screen = curses.initscr()
        # PUT YOUR CODE HERE
        running = True
        while(running):
            if not self.life.is_changing:
                running = False
            self.draw_borders(screen)
            self.life.step()
            self.draw_grid(screen)
            screen.refresh()
            time.sleep(self.speed)
        curses.endwin()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("--help")
    parser.add_argument("--rows", default="20", help="Cells in height")
    parser.add_argument("--cols", default="50", help="Cells in width")
    parser.add_argument("--max-generations", default="50", help="Amount of game iterations")
    parser.add_argument("--speed", default="10", help="Speed of game. 100 -> field will update every 1 second. "
                                                      "10 -> every 0.1 second")
    args = parser.parse_args()
    # help = args.help
    rows = int(args.rows)
    cols = int(args.cols)
    max_generations = int(args.max_generations)
    speed = int(args.speed)
    # print("Rows: " + str(rows))
    # print("Cols: " + str(cols))
    print("Max_generations: " + str(max_generations))
    console = Console(GameOfLife((rows, cols), max_generations=max_generations), speed)
    console.run()
