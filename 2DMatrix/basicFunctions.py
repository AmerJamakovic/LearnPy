from typing import List
import random as rnd
import helpers as help

#testing
def make_pc_suffer_and_enter_values(matrix: List[List[int]], rows:int, columns:int) -> List[List[int]]:
    for i in range(rows):
        for j in range(columns):
            input_ok = False
            if help.is_black_square(i, j):
                while not input_ok:
                    value = rnd.randint(0, 9999)
                    print(f"Value: {value}")
                    if help.is_valid_int(value):
                        if help.is_even_with_odd_number_of_elements(int(value)):
                            matrix[i][j] = int(value)
                            input_ok=True
                        else:
                            print("Invalid number")
                    else:
                        print("Invalid number")

            if not help.is_black_square(i, j):
                while not input_ok:
                    value = rnd.randint(0, 9999)
                    print(f"Value: {value}")
                    if help.is_valid_int(value):
                        if help.is_odd_with_even_number_of_elements(int(value)):
                            matrix[i][j] = int(value)
                            input_ok=True
                        else:
                            print("Invalid number")
                    else:
                        print("Invalid number")
    return matrix



def make_user_suffer_and_enter_values(matrix: List[List[int]], rows:int, columns:int) -> List[List[int]]:

    for i in range(rows):
        for j in range(columns):
            input_ok = False
            if help.is_black_square(i, j):
                while not input_ok:
                    value = input("Enter a even number with odd numbers of elements: ")
                    if help.is_valid_int(value):
                        if help.is_even_with_odd_number_of_elements(int(value)):
                            matrix[i][j] = int(value)
                            input_ok=True
                        else:
                            print("Invalid number")
                    else:
                        print("Invalid number")

            else:
                while not input_ok:
                    value = input("Enter a odd number with even numbers of elements: ")
                    if help.is_valid_int(value):
                        if help.is_odd_with_even_number_of_elements(int(value)):
                            matrix[i][j] = int(value)
                            input_ok=True
                        else:
                            print("Invalid number")
                    else:
                        print("Invalid number")
    return matrix


#These 2 can be one f with some mods

def find_largest_average_row(matrix: List[List[int]], rows: int, columns: int) -> int:
    row_average = [0] * rows
    for Row in range(rows):
        for Col in range(columns):
            row_average[Row] += matrix[Row][Col]
        row_average[Row] /= 6

    biggest_number = row_average[0]
    index = 0
    for i in range(rows):
        if row_average[i] > biggest_number:
            biggest_number = row_average[i]
            index = i

    return index


def find_smallest_average_column(matrix: List[List[int]], rows: int, columns: int) -> int:
    column_average = [0] * columns
    for Row in range(rows):
        for Col in range(columns):
            column_average[Row] += matrix[Col][Row]
        column_average[Row] /= columns

    smallest_number = column_average[0]
    index = 0
    for i in range(columns):
        if column_average[i] < smallest_number:
            smallest_number = column_average[i]
            index = i

    return index
