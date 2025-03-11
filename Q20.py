n = int(input())
l = list(map(int, input().split()))

d = {}

for ch in l:
    if ch not in d:
        d[ch] = 1
    else:
        print("true")
        exit()
        
print("false")
