print() 
study_hours = int(input("Enter number of hours studied this week : "))

if study_hours < 3:
    print("Very little")
elif study_hours <= 6:
    print("Some")
elif study_hours <= 10:
    print("A lot")
elif study_hours > 10:
    print("Too Much")
    