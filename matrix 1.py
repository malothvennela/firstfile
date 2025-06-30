def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            column = []
def print_matrix(matrix):
    for row in matrix:
        print(row)
    for column in matrix:
        print(column)
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = create_matrix(rows, cols)
print("Matrix:")
print_matrix(matrix)

