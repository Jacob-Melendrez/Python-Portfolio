def first_power_of_two(n):
    total = 0
    i = 1   
    
    while i <= n:
        if 2 ** i >= n: 
            total = 2 ** i
            break      
        i += 1  
    return total 
    
print(first_power_of_two(16))