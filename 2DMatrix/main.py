#Dat je 2D niz koji simulira šahovsku tablu.
#Omogućiti korisniku unos cjelobrojnih elemenata 2D niza tako da se u svako „crno“ polje unese parni broj sa neparnim brojem cifara,
#a u „bijelo“ polje neparni broj sa parnim brijem cifara.
# Provjeriti da li je matrica simetricna po glavnoj dijagonali
# (dakle da li je broj na poziciji 1.0 jedna broju na poziciji 0.1, na 0.2 jednak onome na 2.0, na 3.1 jednak onome na 1.3 itd.)
#te ako jeste simetricna naci i ispisati index reda sa najvecim prosjekom elemenata, a ako nije u potpunosti simetricna naci i ispisati index kolone sa najmanjim prosjekom elemenata.


import helpers
import taskSpecificFunctions as tsf


ROWS = 8
COLUMNS = 8


chess_table_matrix = [[0 for _ in range(ROWS)] for _ in range(COLUMNS)]

tsf.make_pc_suffer_and_enter_values(chess_table_matrix, ROWS, COLUMNS)

for row in chess_table_matrix:
    print(' '.join(map(str, row)))

if helpers.check_if_main_diagonal_is_symmetrical(chess_table_matrix, ROWS, COLUMNS):
    print(f"Index of the largest average row is: {tsf.find_largest_average_row(chess_table_matrix, ROWS, COLUMNS)}")
else:
    print(f"Index of the smallest average column is: {tsf.find_smallest_average_column(chess_table_matrix, ROWS, COLUMNS)}")

