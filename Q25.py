arr = list(map(int, input().split(',')))
k = int(input())

arr.sort()
minimum_unfairness = float('inf')
result = []

for i in range(len(arr) - k + 1):
    subset = arr[i:i + k]
    unfairness = max(subset) - min(subset)
    
    if unfairness < minimum_unfairness:
        minimum_unfairness = unfairness
        result = subset
        
print(" ".join(map(str, result)))
