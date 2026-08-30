# Implicit conditional statement example.
temperature = 28 

print()
print(temperature < 32)
print() 

# Taking useer input and evaluating conditional. 
temperature = int(input("Enter a temperature: "))

if temperature < 32: 
    print("It is freezing.")
    
print("Done")
print() 

# Taking useer input and evaluating more complex conditional. 

number = int(input("Enter an integer: "))

if number % 2 == 0: 
    print("Even")
else:
    print("Odd")

# Taking user input and making even more complex conditional. 

print() 
number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else: 
    print("Neither")
    
print() 

# The order of your conditional statements matter and use implicit exclusion from the 
# false value of the previous conditions. 

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else: 
    print("E")
