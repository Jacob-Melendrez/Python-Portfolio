def count_arrivals(minutes, interval):
    count = 0
    for i in range(interval, minutes + 1, interval):
        count += 1
    return count 

print(count_arrivals(25,5))