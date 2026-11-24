'''
n = int(input("Enter a positive integer: "))

total = 0 
number = 1 

while number <= n:
    total += number 
    number += 1
    
print(total)
'''

password = ""
while password != "secret123":
    password = input("Enter your password: ")