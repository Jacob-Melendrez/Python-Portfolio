def sum_fours_for(n):
    total = 0
    number = 4
    
    for number in range(0, n, 4):
        total += number
    return total

'''
print(sum_fours_for(17))
'''