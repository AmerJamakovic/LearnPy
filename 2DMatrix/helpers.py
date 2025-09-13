from typing import List

def is_black_square(i:int, j:int) -> bool:
    if (i+j) % 2 == 0:
        print(f"White {i},{j}")
    else:
        print(f"Black {i},{j}")
    return (i+j) % 2 != 0

def is_even_with_odd_number_of_elements(number:int) -> bool:
    number_of_elements = 0
    number_copy = number
    while number>0:
        number_of_elements += 1
        number = float.__floor__(number / 10)
    if number_of_elements % 2 != 0 and number_copy % 2 ==0:
        return True
    else:
        return False

def is_odd_with_even_number_of_elements(number:int) -> bool:
    number_of_elements = 0
    number_copy = number
    while number > 0:
        number_of_elements += 1
        number = float.__floor__(number / 10)
    if number_of_elements % 2 == 0 and number_copy % 2 != 0:
        return True
    else:
        return False

def check_if_main_diagonal_is_symmetrical(matrix:List[List[int]], rows:int, columns:int) -> bool:
    number_of_elements = rows * columns
    for Row in range(rows):
        for Column in range(columns):
            if matrix[Row][Column] == matrix[Column][Row]:
                number_of_elements -= 1

    if number_of_elements == 0:
        return True
    else:
        return False

def is_valid_int(string:str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False