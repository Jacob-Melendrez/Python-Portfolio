def shuttle_arrives(minute, interval):
        if minute % interval == 0:
            return True
        else:
            return False
        
def count_exactly_one_shuttle(minutes, interval1, interval2):
    total = 0 
    
    
    if shuttle_arrives(minutes, interval1) and shuttle_arrives(minute, interval2):
        total += interval1
        
    return total 

print(count_exactly_one_shuttle(20,4,6))