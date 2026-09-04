def even_cubes(n):
    total = 0
    number = 2
    
    for number in range(2,n+1,2):
        total += number ** 3
    print(total)

even_cubes(4)