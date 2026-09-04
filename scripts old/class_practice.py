# Defining a blueprint to be used elsewhere. Template
class Trail():
    # Initial Constructor method that runs everytime this class is called. Has three parameters, the first being the instance, 
    def __init__(self, dest, len = 0):
        # Create an attribute on the instance and assign it the value
        # passed in as a parameter during class instantiation. 
        self.dest = dest
        self.len= len
    
    def describe_trail(self): 
        """Prints the description of the trail."""
        desc =f"This trail goes to {self.dest}."
        if self.len:
            desc += f"\n The trail is {self.len}km."
        print(desc)
        
# Testing the method.
if __name__ == "__main__":
    print()
    trail_one = Trail("Mountain Peak", 5)
    trail_one.describe_trail()
    print(f"Destination: {trail_one.dest}")
    print(f"Length: {trail_one.len}")
    print() 
    
    trail_two = Trail("Mt.Verstovia", 4)
    trail_two.describe_trail()
    print(f"Destination: {trail_two.dest}")
    print(f"Length: {trail_two.len}") 