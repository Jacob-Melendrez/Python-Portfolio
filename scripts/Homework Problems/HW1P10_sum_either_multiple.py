def sum_either_multiple(n, a, b):
    total = 0 
    for i in range(1, n+1, 1):
        if i % a == 0:
            total += i 
        if i % b == 0:
            total += i
        if i % a == 0 and i % b == 0:
            total -= i 
    return total 

"""
print(sum_either_multiple(10, 3, 5))
"""