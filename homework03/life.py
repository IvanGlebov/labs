import pathlib
import random

from typing import List, Optional, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float('inf')
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1
        # self.grid = []

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize is True:
            # Простой генератор списка, который генерирует self.cell_height списков
            # длиной self.cell_width заполненных random.randint(0,1)
            return [[random.randint(0, 1) for i in range(self.cols)] for j in range(self.rows)]
        else:
            # Генератор списка, который генерирует список заполненный нулями
            return [[0] * self.cols for i in range(self.rows)]
        pass

    def get_neighbours(self, cell: Cell) -> Cells:

        left_border = max(0, min(cell[0] - 1, self.cols - 1))
        right_border = min(self.cols, min(cell[0] + 1, self.cols - 1)) + 1

        # print("Width")
        # print(str(left_border) + " <= x <= " + str(right_border - 1))
        # print([i for i in range(left_border, right_border)])

        top_border = max(0, min(cell[1] - 1, self.rows - 1))
        bottom_border = min(self.rows, min(cell[1] + 1, self.rows - 1)) + 1

        # print("\n")
        # print("Height")
        # print(str(top_border) + " <= y <= " + str(bottom_border - 1))
        # print([i for i in range(top_border, bottom_border)])

        result_list = []
        for i in range(top_border, bottom_border):
            for j in range(left_border, right_border):
                if i == cell[1] and j == cell[0]:
                    continue
                else:
                    try:
                        result_list.append(self.grid[i][j])
                    except:
                        print("Error in row " + str(i) + ", column " + str(j))
        return result_list
        pass

    def get_next_generation(self) -> Grid:

        old_grid = self.grid
        new_grid = self.create_grid(False)
        neighbours_grid = [[0] * len(old_grid[0]) for i in range(len(old_grid))]

        def count_elements(in_list, element_type):
            counter = 0
            for i in in_list:
                if i == element_type:
                    counter += 1
            return counter

        for row in range(self.rows):
            for element in range(self.cols):
                if 2 <= count_elements(self.get_neighbours((element, row)), 1) <= 3 and self.grid[row][element] == 1:
                    new_grid[row][element] = 1
                # print("row: " + str(row) + ", element: " + str(element))
                if self.grid[row][element] == 0 and count_elements(self.get_neighbours((element, row)), 1) == 3:
                    new_grid[row][element] = 1
                neighbours_grid[row][element] = count_elements(self.get_neighbours((element, row)), 1)

        self.grid = new_grid
        # print(neighbours_grid)
        for row in neighbours_grid:
            print(row)
        print('\n')
        if old_grid == new_grid:
            print("Repeat!")

        pass
        return new_grid

    def step(self) -> None:
        self.get_next_generation()
        self.generations += 1
        """
        Выполнить один шаг игры.
        """
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
                Не превысило ли текущее число поколений максимально допустимое.
                """
        pass
        if self.generations > self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
                Изменилось ли состояние клеток с предыдущего шага.
                """
        pass

        if self.curr_generation != self.prev_generation:
            return True
        else:
            return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
                Прочитать состояние клеток из указанного файла.
                """
        pass
        return_matrix = []
        with open(filename, 'r') as readFile:
            return_matrix = [[int(el) for el in row if el != '\n'] for row in readFile.readlines()]
        game = GameOfLife((len(return_matrix), len(return_matrix[0])), False)
        game.grid = return_matrix

        return game

    def save(self, filename: pathlib.Path) -> None:
        save_string = ''

        for row in self.grid:
            for el in row:
                save_string += str(el)
            save_string += '\n'

        with open(filename, 'w') as saveFile:
            saveFile.write(save_string)

        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
