def shuttle_arrives(minute, interval):
        if minute % interval == 0:
            return True
        else:
            return False
        
"""
print(shuttle_arrives(15,5))
"""