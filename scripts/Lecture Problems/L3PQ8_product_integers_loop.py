n = int(input("Enter an integer: "))
i = 1
total = 1 

while i <= n:
    if i % 3 == 0:
        total *= i 
    else:
        total += 0 
        
        i += 1

print(total)
    