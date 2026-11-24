def double(num):
    return 2 * num

def square(num):
    return num ** 2
""" 
print(double(square(5)))
print(square(double(5)))


def sum_even(n):
    total = 0 
    for num in range(2, n+1, 2):
        total += num 
    return total 
        
print(sum_even(4))

def absolute_value(n):
    if n < 0:
        return -n 
    else:
        return n 

print(absolute_value(-5))
"""

def sum_multiples(n, divisor):
    total = 0 
    for num in range(1, n+1, num):
        total += num 
    return total
            
print(sum_multiples(10,3))

