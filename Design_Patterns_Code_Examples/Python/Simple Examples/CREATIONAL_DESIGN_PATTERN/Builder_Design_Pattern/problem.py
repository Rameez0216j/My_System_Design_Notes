# Without Builder Pattern - Using Telescoping Constructor (Messy and Hard to Maintain)
class Burger:
    def __init__(self, size, cheese=False, lettuce=False, tomato=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.lettuce = lettuce
        self.tomato = tomato
        self.bacon = bacon

    def __str__(self):
        return f"Burger(Size: {self.size}, Cheese: {self.cheese}, Lettuce: {self.lettuce}, Tomato: {self.tomato}, Bacon: {self.bacon})"

# Creating different burgers
burger1 = Burger(6, cheese=True)  # Small burger with cheese
burger2 = Burger(9, cheese=True, lettuce=True, tomato=True, bacon=True)  # Large fully loaded burger

print(burger1)
print(burger2)


'''
Problems in This Approach:
    Too Many Parameters → Constructor overload increases as more attributes are added.
    Hard to Read & Maintain → The order of parameters matters, making it error-prone.
    Not Flexible → If a new ingredient is added, every object creation must be updated.
'''

