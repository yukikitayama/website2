# Make 2 matrices by different ways
row = 2
col = 3
matrix1 = [[0] * col] * row  # Mutiply list
matrix2 = [[0 for _ in range(col)] for _ in range(row)]  # List comprehension

# These matrices look like the same
print('Matrix 1')
[print(row) for row in matrix1]
print()
# Matrix 1
# [0, 0, 0]
# [0, 0, 0]

print('Matrix 2')
[print(row) for row in matrix2]
print()
# Matrix 2
# [0, 0, 0]
# [0, 0, 0]

# But when you update the elements
queue = [1, 2, 3, 4, 5, 6]
for i in range(row):
    for j in range(col):
        tmp = queue.pop(0)
        matrix1[i][j] = tmp
        matrix2[i][j] = tmp

# The result is different
print('Matrix 1')
[print(row) for row in matrix1]
print()
# Matrix 1
# [4, 5, 6]
# [4, 5, 6]

print('Matrix 2')
[print(row) for row in matrix2]
print()
# Matrix 2
# [1, 2, 3]
# [4, 5, 6]

# It is because the lists made by multiplying have the same reference
print(f'id(matrix1[0]): {id(matrix1[0])}, id(matrix1[1]): {id(matrix1[1])}')
print(f'id(matrix2[0]): {id(matrix2[0])}, id(matrix2[1]): {id(matrix2[1])}')
# id(matrix1[0]): 3238279030656, id(matrix1[1]): 3238279030656
# id(matrix2[0]): 3238282160448, id(matrix2[1]): 3238282160320
