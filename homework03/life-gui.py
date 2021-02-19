import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        # self.width =
        self.cell_size = cell_size
        # self.height = height
        self.speed = speed
        # Устанавливаем размер окна
        # Создание нового окна
        super().__init__(life)

        self.height = self.life.rows * self.cell_size
        self.width = self.life.cols * self.cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        # Copy from previous assignment
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))
        pass

    def draw_grid(self) -> None:
        # Copy from previous assignment
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

        # Создание списка клеток
        self.life.grid = self.life.create_grid(True)
        self.grid = self.life.grid
        self.draw_grid()

        running = True
        single_run = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.draw_lines()
            self.draw_grid()
            if single_run:
                self.life.get_next_generation()
                single_run = False
            self.draw_grid()

            # self.life.step()

            self.grid = self.life.grid

            pygame.display.flip()

            clock.tick(self.speed)

        pygame.quit()
        pass


if __name__ == '__main__':
    #
    gui = GUI(GameOfLife((5, 5)), 40, 1)
    # gui.life.from_file('./grid.txt')
    gui.run()

