Question Name: Rotate Image

def rotate(matrix):
    n = len(matrix) 
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

n = int(input("Enter the size of the matrix (n x n): "))
matrix = []
for i in range(n):
    matrix.append(list(map(int, input(f"Enter row {i + 1} elements separated by space: ").split())))

rotate(matrix)
print("Matrix after 90-degree rotation:")
for row in matrix:
    print(" ".join(map(str, row)))
