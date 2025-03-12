arr = list(map(int, input().split(',')))


small = arr[0]
profit = 0

for i in range(1, len(arr)):
    if arr[i] < small:
        small = arr[i]
    elif arr[i] - small > profit:
        profit = arr[i] - small
        
print(profit)
