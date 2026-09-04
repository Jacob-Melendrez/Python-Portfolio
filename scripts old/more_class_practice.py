# Class = blueprint for an object. 
class Pizza:
    # A global class variable shared by all pizzas
    price_per_topping = 1.50

#This method is an initial constructor of the class. 
#When you see self you should think this specific object. 
    def __init__(self, size, toppings):
        self.size = size          # Instance variable
        self.toppings = toppings  # Instance variable

    # 1. Instance Method
    def get_total_price(self):
        # Uses instance data (self.toppings) and class data (self.price_per_topping)
        return 10.00 + (len(self.toppings) * self.price_per_topping)

    # 2. Class Method
    @classmethod
    def create_marg(cls):
        # Uses cls to create a new Pizza object with specific defaults
        return cls("Large", ["cheese", "tomato"])

    # 3. Static Method
    @staticmethod
    def is_healthy(topping):
        # Independent utility function: just checks the input string
        return topping in ["tomato", "spinach", "mushrooms"]
    
my_pizza = Pizza("Medium", ["cheese"])
print(my_pizza.get_total_price())
marg = my_pizza.create_marg()

print(my_pizza.is_healthy())