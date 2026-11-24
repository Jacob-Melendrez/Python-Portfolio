def first_shared_arrival_after(minute, interval1, interval2):
    match = 0
    while interval1 <= 40:
        if interval1 == interval2:
            match = interval1
        
        interval1 += interval1
        
        if interval1 == interval2:
            match = interval1
        
        interval2 += interval2
        
        return match 

"""            match = interval1
            if shuttle_arrives(match, interval1) and shuttle_arrives(match, interval2):
                total += match
"""

def shuttle_arrives(minute, interval):
        if minute % interval == 0:
            return True
        else:
            return False
        
print(first_shared_arrival_after(24,4,6))
