n = int(input("Enter an integer: "))


sum = 0 
i = 2 

while i <= n:
    sum = (i ** 3) + sum
    i += 2
    
print(sum)