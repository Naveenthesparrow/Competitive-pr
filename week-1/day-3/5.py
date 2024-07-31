
Question Name: Rotate Matrix

n=int(input())
matrix=[]
for _ in range(n):
row=list(map(int,input().split()))
matrix.append(row)
rotated_matrix=[]
for j in range(n):
new_row=[]
for i in range(n-1,-1,-1):
new_row.append(matrix[i][j])
rotated_matrix.append(new_row)
for row in rotated_matrix:
print(*row)