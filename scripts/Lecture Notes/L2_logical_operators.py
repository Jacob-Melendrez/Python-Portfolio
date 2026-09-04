# Logical operators. 

# and operator (Evaluates to true if both conditions are true.)
print()
temperature = int(input("Enter a temperature."))

if temperature >= 65 and temperature <= 75:
    print("It is perfect weather outside.")

# or operator (Evaluates to true if one condition is true.)
print() 
day = input("Enter a day: ")

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!" )
else:
    print("Its a weekday.")

# not operator (Flips value to opposite booelan value.)
print() 
raining = False 
print(not raining)
