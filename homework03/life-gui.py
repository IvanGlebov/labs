import pygame
import argparse

from pygame.locals import *
from life import GameOfLife
from ui import UI
from math import *

class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        self.cell_size = cell_size
        self.speed = speed
        # Устанавливаем размер окна
        # Создание нового окна
        super().__init__(life)

        self.height = self.life.rows * self.cell_size
        self.width = self.life.cols * self.cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))
        pass

    def draw_grid(self) -> None:
        for i in range(int(self.height / self.cell_size)):
            for j in range(int(self.width / self.cell_size)):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (j*self.cell_size + 1, i*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (j*self.cell_size + 1, i*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))
        pass

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        self.life.curr_generation = self.life.create_grid(True)
        self.grid = self.life.curr_generation
        self.draw_grid()

        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pause = not pause
                    if pause:
                        if event.key == K_RIGHT:
                            self.life.step()
                            self.grid = self.life.curr_generation
                            self.draw_lines()
                            self.draw_grid()
                            pygame.display.flip()
                        if event.key == K_LEFT:
                            self.grid = self.life.prev_generation
                            self.life.curr_generation = self.life.prev_generation
                            self.draw_lines()
                            self.draw_grid()
                            pygame.display.flip()

                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pause:
                        cellx = int(ceil(pos[0] / self.cell_size)) - 1
                        celly = int(ceil(pos[1] / self.cell_size)) - 1
                        if event.button == 1:
                            print("Adding cell to " + "X:" + str(cellx) + ", Y:" + str(celly))
                            self.grid[celly][cellx] = 1
                        if event.button == 3:
                            print("Removing cell from " + "X:" + str(cellx) + ", Y:" + str(celly))
                            self.grid[celly][cellx] = 0

                        self.life.curr_generation = self.grid
                        self.draw_lines()
                        self.draw_grid()
                        pygame.display.flip()

            if not self.life.is_changing:
                running = False
            if self.life.is_max_generations_exceeded:
                running = False
            if not pause:
                self.grid = self.life.curr_generation
                self.draw_lines()
                self.draw_grid()
                self.life.step()

                pygame.display.flip()
                # pause = True

            clock.tick(self.speed)

        pygame.quit()
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--width", default="100", help="Cells in width")
    parser.add_argument("--height", default="150", help="Cells in height")
    parser.add_argument("--cell-size", default="5", help="Size of cell wall in px")
    parser.add_argument("--max-generations", default="500", help="Amount of game iterations")
    parser.add_argument("--speed", default="10", help="Speed of game. More -> faster")
    arguments = parser.parse_args()

    width = int(arguments.width)
    height = int(arguments.height)
    cell_size = int(arguments.cell_size)
    max_generations = int(arguments.max_generations)
    speed = int(arguments.speed)

    gui = GUI(GameOfLife((width, height), max_generations=max_generations), cell_size, speed)
    gui.run()

