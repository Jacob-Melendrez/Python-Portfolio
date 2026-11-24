n = int(input("Enter an integer: "))
i = 1
total = 0

while i <= n:
    if i % 2 == 0:
        total += 0
    elif i % 2 == 1:
        total += i 
    i += 1 
    
print(total)