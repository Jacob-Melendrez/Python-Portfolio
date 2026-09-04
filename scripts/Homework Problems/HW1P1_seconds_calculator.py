def total_seconds(hours, minutes, seconds):
        return seconds + (60 * minutes) + ((60 ** 2) * hours)

print(total_seconds(1,2,3))
print(total_seconds(0,5,20))