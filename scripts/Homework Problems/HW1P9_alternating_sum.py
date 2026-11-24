def alternating_sum(n):
    i = 1
    total = 0
    
    while i <= n:
        if i % 2 == 0:
            total -= i
        elif i % 2 != 0:
            total += i 
        i += 1
    return total 

"""
print(alternating_sum(6))
"""