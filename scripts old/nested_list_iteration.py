visit_times = [
    [30,45,20],
    [60,90,45],
    [15,25,35,40],
    [120,50,60]
]

def departments_over_120(visit_times):
    count = 0 
    for group in visit_times:
        total = 0 
        for time in group:
            total += time 
            
        if(total >= 120):
            count += 1
    return count 

print(departments_over_120(visit_times))