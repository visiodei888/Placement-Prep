m, n = map(int, input().split())

m1 = []
m2 = []
m3 = [[0] * n for i in range(m)]

for i in range(m):
    row = list(map(int, input().split()))
    m1.append(row)
    
print("First Matrix:")
for row in m1:
    print(' '.join(map(str, row)))
    
for i in range(m):
    row = list(map(int, input().split()))
    m2.append(row)

print("Second Matrix:")
for row in m2:
    print(' '.join(map(str, row)))
    
for i in range(m):
    for j in range(n):
        m3[i][j] = m1[i][j] + m2[i][j]

print("Sum of the two matrices is:")
for row in m3:
    print(' '.join(map(str, row)))
