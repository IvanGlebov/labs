import pygame
import random

from pygame.locals import *
from typing import List, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.grid = self.create_grid(True)

        # self.grid = [
        #     [1, 1, 0, 0, 1, 1, 1, 1],
        #     [0, 1, 1, 1, 1, 1, 1, 0],
        #     [1, 0, 1, 1, 0, 0, 0, 0],
        #     [1, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 0, 1, 1, 1, 1, 0, 0],
        #     [1, 1, 1, 1, 0, 1, 1, 1]
        # ]

        self.draw_grid()
        # PUT YOUR CODE HERE

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()

            self.draw_grid()
            # first arg  - x coordinate
            # second arg - y coordinate

            # neighbours = self.get_neighbours((5, 7))
            # print(neighbours)
            # print("len : " + str(len(neighbours)))
            # print("sum : " + str(sum(neighbours)))

            self.get_next_generation()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False, full_true: bool = False) -> Grid:
        """
        
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        pass
        if full_true is True:
            return [[1] * self.cell_width for i in range(self.cell_height)]
        else:
            if randomize is True:
                # Простой генератор списка, который генерирует self.cell_height списков
                # длиной self.cell_width заполненных random.randint(0,1)
                return [[random.randint(0, 1) for i in range(self.cell_width)] for j in range(self.cell_height)]
            else:
                # Генератор списка, который генерирует список заполненный нулями
                return [[0] * self.cell_width for i in range(self.cell_height)]

    def draw_grid(self) -> None:
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (
                    j * self.cell_size + 1, i * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (
                    j * self.cell_size + 1, i * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        pass

    def get_neighbours(self, cell: Cell) -> Cells:

        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        pass
        # cell[0], cell[1] = cell[1], cell[0]
        left_border = max(0, min(cell[1] - 1, self.cell_width - 1))
        right_border = min(self.cell_width, min(cell[1] + 1, self.cell_width - 1)) + 1

        # print("Width")
        # print(str(left_border) + " <= x <= " + str(right_border-1))
        # print([i for i in range(left_border, right_border)])

        top_border = max(0, min(cell[0] - 1, self.cell_height - 1))
        bottom_border = min(self.cell_height - 1, min(cell[0] + 1, self.cell_height - 1)) + 1

        # print("\n")
        # print("Height")
        # print(str(top_border) + " <= y <= " + str(bottom_border-1))
        # print([i for i in range(top_border, bottom_border)])

        result_list = []
        exeption = False
        for i in range(top_border, bottom_border):
            for j in range(left_border, right_border):
                if i == cell[0] and j == cell[1]:
                    # print('cell x,y : ' + str(j) + ", " + str(i) + ' checked')
                    continue
                else:
                    try:
                        result_list.append(self.grid[i][j])
                    except:
                        exeption = True
                        # print("Error in row " + str(i) + ", column " + str(j))
        # print(result_list)
        return result_list

    def get_next_generation(self) -> Grid:
        old_grid = self.grid
        new_grid = self.create_grid(False)

        def count_elements(in_list, element_type):
            counter = 0
            for i in in_list:
                if i == element_type:
                    counter += 1
            return counter

        for row in range(self.cell_height):
            for element in range(self.cell_width):
                if 2 <= count_elements(self.get_neighbours((element, row)), 1) <= 3 and self.grid[row][element] == 1:
                    new_grid[row][element] = 1
                if self.grid[row][element] == 0 and count_elements(self.get_neighbours((element, row)), 1) == 3:
                    new_grid[row][element] = 1

        self.grid = new_grid
        # if old_grid == new_grid:
        #     print("Repeat!")

        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        pass


if __name__ == '__main__':
    game = GameOfLife(640, 480, 20, 5)
    game.run()
