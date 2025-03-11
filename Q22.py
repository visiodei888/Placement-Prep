n = int(input())

c = 0

for i in range(n):
    num = int(input())
    
    if num % 2 != 0:
        c += 1
        
if c == 0:
    print("No odd elements are present")
else:
    print(f"Odd Elements: {c}")
