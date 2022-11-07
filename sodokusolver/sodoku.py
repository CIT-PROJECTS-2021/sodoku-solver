"""
Sodoku class responsible for generating and solving sodoku puzzles
"""

import random
import copy
import time

class Sodoku:
    """
    Sodoku class responsible for generating sodoku puzzles
    """
    def __init__(self, size=9):
        self.size = size
        # create a sodoku puzzle board
        # each row and column can have a number from 1 to 9 but not repeated
        # each 3x3 box can have a number from 1 to 9 but not repeated
        self.sodoku = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.sodoku_solution = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.sodoku_solution_unique = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.sodoku_solution_count = 0
        self.sodoku_solution_time = 0
        
    def generate(self):
        """
        Generate a sodoku puzzle
        """
        # generate a sodoku puzzle with a single solution
        # 1. generate a sodoku puzzle with all numbers from 1 to 9
        # 2. shuffle each row
        # 3. shuffle each column
        # 4. shuffle each 3x3 box
        # 5. remove numbers from the sodoku puzzle to make it harder
        # 6. check if the sodoku puzzle has a single solution
        # 7. repeat from step 2 if the sodoku puzzle has more than one solution
        # 8. repeat from step 1 if the sodoku puzzle has no solution
        # 9. return the sodoku puzzle
        while True:
            # step 1
            self._generate_sodoku()
            # step 2
            self._shuffle_sodoku_rows()
            # step 3
            self._shuffle_sodoku_columns()
            # step 4
            self._shuffle_sodoku_boxes()
            # step 5
            self._remove_sodoku_numbers()
            # step 6
            if self._check_sodoku_solution_count() == 1:
                break
        return self.sodoku

    def _generate_sodoku(self):
        """
        Generate a sodoku puzzle with all numbers from 1 to 9
        """
        for row in range(self.size):
            for column in range(self.size):
                self.sodoku[row][column] = column + 1

    def _shuffle_sodoku_rows(self):
        """
        Shuffle each row of the sodoku puzzle
        """
        for row in range(self.size):
            random.shuffle(self.sodoku[row])

    def _shuffle_sodoku_columns(self):
        """
        Shuffle each column of the sodoku puzzle
        """
        for column in range(self.size):
            column_list = [self.sodoku[row][column] for row in range(self.size)]
            random.shuffle(column_list)
            for row in range(self.size):
                self.sodoku[row][column] = column_list[row]

    def _shuffle_sodoku_boxes(self):
        """
        Shuffle each 3x3 box of the sodoku puzzle
        """
        for box_row in range(3):
            for box_column in range(3):
                box_list = []
                for row in range(3):
                    for column in range(3):
                        box_list.append(self.sodoku[box_row * 3 + row][box_column * 3 + column])
                random.shuffle(box_list)
                for row in range(3):
                    for column in range(3):
                        self.sodoku[box_row * 3 + row][box_column * 3 + column] = box_list[row * 3 + column]

    def _remove_sodoku_numbers(self):
        """
        Remove numbers from the sodoku puzzle to make it harder
        """
        for _ in range(50):
            row = random.randint(0, self.size - 1)
            column = random.randint(0, self.size - 1)
            self.sodoku[row][column] = 0

    def _check_sodoku_solution_count(self):
        """
        Check if the sodoku puzzle has a single solution
        """
        self.sodoku_solution_count = 0
        self._solve_sodoku()
        return self.sodoku_solution_count

    def _solve_sodoku(self):
        """
        Solve the sodoku puzzle
        """
        # solve the sodoku puzzle
        # 1. find the first empty cell
        # 2. try numbers from 1 to 9
        # 3. check if the number is valid
        # 4. repeat from step 2 if the number is not valid
        # 5. repeat from step 1 if there are no more empty cells
        # 6. return the sodoku puzzle
        # 7. return the number of solutions
        # 8. return the time taken to solve the sodoku puzzle
        self.sodoku_solution_count = 0
        self.sodoku_solution_time = 0
        start_time = time.time()
        self._solve_sodoku_recursive(0, 0)
        end_time = time.time()
        self.sodoku_solution_time = end_time - start_time
        return self.sodoku_solution

    def _solve_sodoku_recursive(self, row, column):
        """
        Solve the sodoku puzzle recursively
        """
        # solve the sodoku puzzle recursively
        # 1. find the next empty cell
        # 2. try numbers from 1 to 9
        # 3. check if the number is valid
        # 4. repeat from step 2 if the number is not valid
        # 5. repeat from step 1 if there are no more empty cells
        # 6. return the sodoku puzzle
        # 7. return the number of solutions
        # 8. return the time taken to solve the sodoku puzzle
        if row == self.size:
            self.sodoku_solution_count += 1
            if self.sodoku_solution_count == 1:
                self.sodoku_solution = copy.deepcopy(self.sodoku)
            return
        if self.sodoku_solution_count > 1:
            return
        if self.sodoku[row][column] != 0:
            if column == self.size - 1:
                self._solve_sodoku_recursive(row + 1, 0)
            else:
                self._solve_sodoku_recursive(row, column + 1)
        else:
            for number in range(1, self.size + 1):
                if self._check_sodoku_number(row, column, number):
                    self.sodoku[row][column] = number
                    if column == self.size - 1:
                        self._solve_sodoku_recursive(row + 1, 0)
                    else:
                        self._solve_sodoku_recursive(row, column + 1)
                    self.sodoku[row][column] = 0

    def _check_sodoku_number(self, row, column, number):
        """
        Check if the number is valid
        """
        # check if the number is valid
        # 1. check if the number is already in the row
        # 2. check if the number is already in the column
        # 3. check if the number is already in the 3x3 box
        # 4. return True if the number is valid
        # 5. return False if the number is not valid
        # check if the number is already in the row
        for i in range(self.size):
            if self.sodoku[row][i] == number:
                return False
        # check if the number is already in the column
        for i in range(self.size):
            if self.sodoku[i][column] == number:
                return False
        # check if the number is already in the 3x3 box
        box_row = row // 3
        box_column = column // 3
        for i in range(3):
            for j in range(3):
                if self.sodoku[box_row * 3 + i][box_column * 3 + j] == number:
                    return False
        return True

    def _print_sodoku(self):
        """
        Print the sodoku puzzle
        """
        for row in range(self.size):
            if row % 3 == 0 and row != 0:
                print("- - - - - - - - - - - - -")
            for column in range(self.size):
                if column % 3 == 0 and column != 0:
                    print(" | ", end="")
                if column == self.size - 1:
                    print(self.sodoku[row][column])
                else:
                    print(str(self.sodoku[row][column]) + " ", end="")
        print()

    def _print_sodoku_solution(self):
        """
        Print the sodoku puzzle solution
        """
        for row in range(self.size):
            if row % 3 == 0 and row != 0:
                print("- - - - - - - - - - - - -")
            for column in range(self.size):
                if column % 3 == 0 and column != 0:
                    print(" | ", end="")
                if column == self.size - 1:
                    print(self.sodoku_solution[row][column])
                else:
                    print(str(self.sodoku_solution[row][column]) + " ", end="")
        print()

    def _print_sodoku_solution_count(self):
        """
        Print the number of sodoku puzzle solutions
        """
        print("Number of solutions: " + str(self.sodoku_solution_count))

    def _print_sodoku_solution_time(self):
        """
        Print the time taken to solve the sodoku puzzle
        """
        print("Time taken to solve the sodoku puzzle: " + str(self.sodoku_solution_time) + " seconds")
