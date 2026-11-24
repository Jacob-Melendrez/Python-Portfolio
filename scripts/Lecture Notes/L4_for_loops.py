""" 
n = int(input("Enter a positive integer: "))

for number in range(1, n + 1):
    if number % 2 == 0:
        print(number) 


        COMPARING LOOPS 
        
WHILE LOOP 
n = int(input("Enter an integer: "))
total = 0 
start = 1 
while start <= n: 
    total += start
    start += 1
    
print(total)

FOR LOOP 
n  = int(input("Enter an integer: "))
total = 0 
for start in range(1, n+1):
    total += start 
print(total)


n = 10 
for i in range(0, 9):
    print(i)
    
n = int(input("Give me an intger greater than 1: "))
total = 0 

for i in range(2, n+1):
    if i % 2 == 0:
        total += i 
    else:
        total += 0
print(total)


n = int(input("Give me an intger greater than 1: "))
total = 0 

for i in range(0, n + 1):
    if i % 2 == 0: 
        total += 0 
    elif i % 2 == 1:
        total += i 
        
print(total)


n = int(input("Enter me an integer greater than 1: "))
total = 0 

for i in range(3, n+1, 3):
    total += i 
print(total)

n = int(input("Enter me an integer greater than 1: "))
total = 1

for i in range(1, n+1):
    total *= i
print(total)

"""

