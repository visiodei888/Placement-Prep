n = int(input())
m = int(input())

if n % 3 == 0:
    start = n + 3
elif (n + 1) % 3 == 0:
    start = n + 1
else:
    start = n + 2
    
while start < m:
    print(start, end = " ")
    start += 3
