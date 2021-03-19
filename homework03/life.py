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

        left_border = max(0, min(cell[1] - 1, self.cols - 1))
        right_border = min(self.cols, min(cell[1] + 1, self.cols - 1)) + 1

        # print("Width")
        # print(str(left_border) + " <= x <= " + str(right_border-1))
        # print([i for i in range(left_border, right_border)])

        top_border = max(0, min(cell[0] - 1, self.rows - 1))
        bottom_border = min(self.rows - 1, min(cell[0] + 1, self.rows - 1)) + 1

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
                        result_list.append(self.curr_generation[i][j])
                    except:
                        exeption = True
                        # print("Error in row " + str(i) + ", column " + str(j))
        # print(result_list)
        return result_list

    def get_next_generation(self) -> Grid:
        self.prev_generation = self.curr_generation
        next_grid = [[0] * len(self.prev_generation[0]) for i in range(len(self.prev_generation))]
        neighbours_grid = [[0] * len(self.prev_generation[0]) for i in range(len(self.prev_generation))]
        for row in range(self.rows):
            for col in range(self.cols):
                neighbours = sum(self.get_neighbours((row, col)))
                neighbours_grid[row][col] = neighbours

        # something strange is here
        # Well, error was above
        for row in range(len(neighbours_grid)):
            for col in range(len(neighbours_grid[0])):
                if self.curr_generation[row][col] == 1:
                    if 2 <= neighbours_grid[row][col] <= 3:
                        next_grid[row][col] = 1
                if self.curr_generation[row][col] == 0:
                    if neighbours_grid[row][col] == 3:
                        next_grid[row][col] = 1
        self.curr_generation = next_grid

        pass
        return next_grid

    def step(self) -> None:
        if not self.is_max_generations_exceeded:
            self.get_next_generation()
            self.generations += 1

        """
        Выполнить один шаг игры.
        """
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        # """
        #         Не превысило ли текущее число поколений максимально допустимое.
        #         """
        # pass
        if self.generations >= self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        # """
        #         Изменилось ли состояние клеток с предыдущего шага.
        #         """
        # pass
        if self.prev_generation != self.curr_generation:
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

        for row in self.curr_generation:
            for el in row:
                save_string += str(el)
            save_string += '\n'

        with open(filename, 'w') as saveFile:
            saveFile.write(save_string)

        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
