n = int(input())

product = 1

for i in range(n):
    num = float(input())
    
    product *= num
    
print(f"The product of the numbers is: {product:.2f}")
