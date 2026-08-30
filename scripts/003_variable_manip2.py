# Original Code 
x = 4
y = 9
x = y
y = x + 1
print(x)
print(y)

# Modified swapped code. 
x = 4 
y = 9 
temporary = 0

temporary = x
x = y
y = temporary

print(x)
print(y) 

# The code does not swap the original values of x and y 
# because the value of x was assigned to the value of y 
# so when the value of x was used again the output was
# not the intentional 5 that was attempted. The 9 carried 
# over.
