
def sum_evens(m,n):
    total = 0
    while m <= n:
            total += m + 2
            m += 2
    return total 
            
print(sum_evens(4,7))
