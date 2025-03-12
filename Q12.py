n = int(input())

flag = 0
if n > 1:
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            flag = 1
            break
            
    if flag == 1:
        print(f"{n} is not a prime number")
    else:
        print(f"{n} is a prime number")
        
else:
    print(f"{n} is not a prime number")
