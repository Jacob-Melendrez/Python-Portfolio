class Dog: 
    def __init__(self,color,size):
        self.color = color
        self.size = size
    
    def dog_description(self):
        print(f"The color of the dog is {self.color} and the size of the dog is {self.size} .")

my_dog = Dog("Black", "Large")
my_dog.dog_description()
