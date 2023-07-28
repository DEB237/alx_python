def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        print() 
    else:
        for row in matrix:
            for i, num in enumerate(row):
                if i == len(row) - 1:
                    print("{:d}".format(num))
                else:
                    print("{:d}".format(num), end=" ")
  
matrix = [
    [1, 2],
    [4, 5],
    [7, 8]
]

print_matrix_integer(matrix)
print_matrix_integer()