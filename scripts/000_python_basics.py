#Addition 
print(3 + 7)
print()
#Subtraction
print(3 - 7)
print() 
#Multiplication
print(3 * 7)
print()
#Division 
print(3 / 7)
print()
#Floor Division Operator
print(13 // 3)
print() 
#Modulus Operator
print(7 % 3)
print()
    
# Variable Manipulation 
x = 50 
print(x)
y = x + 1
print()
x = x + 1
print(x)


print()
num = 10 
print(num + 1)
print()
print(num)
print()


num_1 = 4
num_2 = 9
num_3 = 6

num_1 = num_2
num_2 = num_1 + 1
num_3 = 2 * num_1 + num_2

print(num_1)
print()
print(num_2)
print()
print(num_3)
print() 

# Using type() function do find the datatype. 
t = "Bob" 
print(type(t))

#Taking user input using the input() function. 
name = input("What is your name?")
print(name)
print()

# Modifying user input by changing string datatype to int using int() function.
age = int(input("What is your age?"))
age = age + 1
print(f"Hi {name}, your age in one year will be {age}.")
