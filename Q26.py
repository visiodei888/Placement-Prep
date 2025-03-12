n = int(input())  
m = int(input())  

matrix = []

for i in range(n):  
    matrix.append(list(map(int, input().split())))

count = 0
row, col = 0, m - 1  

while row < n and col >= 0:
    if matrix[row][col] < 0:
        count += (col + 1)  
        row += 1  
    else:
        col -= 1  

print(count)
