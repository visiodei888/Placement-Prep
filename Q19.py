s=input()

total=0
available=0

for ch in s:
    if (ch == 'U' or ch == 'C') and (available == 0):
        total += 1
    elif (ch == 'U' or ch == 'C') and (available != 0):
        available -= 1
    else:
        available += 1
        
print(total)
