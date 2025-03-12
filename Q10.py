n = int(input())

temp = n

total = 0

while n != 0:
    num = float(input())
    total += num
    n -= 1

avg = total / temp

print(f"The average is: {avg:.3f}")
