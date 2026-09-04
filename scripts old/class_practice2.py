class Dog():
    def __init__(self,color):
        self.color = color
    
    def dog_description(self):
        print(f"The dog is {self.color} .")

dog_color = input("What is the color of your dog? ")

my_dog = Dog(dog_color)
my_dog.dog_description()
