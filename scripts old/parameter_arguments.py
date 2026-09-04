
def hello(name):
        # Greet someone by name.  
        print(f"Hello, {name}!")

def fav_color(color):
        # Ask favorite color. 
        print(f"{color} is a cool color! ")


while True: 
        name = input("What is your name? ")
        hello(name)

        color = input("What is your favorite color? ")
        fav_color(color)

        again = input("Do you want to continue? (yes/no)")

        if again.lower() != "yes":
                print("Goodbye!")
                break
