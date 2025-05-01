# Builder Pattern Implementation
class Burger:
    """Product: The complex object being built"""
    def __init__(self, size, cheese, lettuce, tomato, bacon):
        self.size = size
        self.cheese = cheese
        self.lettuce = lettuce
        self.tomato = tomato
        self.bacon = bacon

    def __str__(self):
        return f"Burger(Size: {self.size}, Cheese: {self.cheese}, Lettuce: {self.lettuce}, Tomato: {self.tomato}, Bacon: {self.bacon})"

# Builder Class
class BurgerBuilder:
    """Builder: Helps construct a Burger step by step"""
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.lettuce = False
        self.tomato = False
        self.bacon = False

    def add_cheese(self):
        self.cheese = True
        return self  # Returning self allows method chaining

    def add_lettuce(self):
        self.lettuce = True
        return self

    def add_tomato(self):
        self.tomato = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Burger(self.size, self.cheese, self.lettuce, self.tomato, self.bacon)

# Usage of Builder Pattern
burger1 = BurgerBuilder(6).add_cheese().build()  # Small burger with cheese
burger2 = BurgerBuilder(9).add_cheese().add_lettuce().add_tomato().add_bacon().build()  # Large fully loaded burger

print(burger1)
print(burger2)



'''
Key Benefits of the Builder Pattern
    Improves Readability → Easy to understand and modify object creation.
    Flexible Object Construction → No need to pass all parameters at once.
    Encapsulates Object Creation → Clients don't need to know the internal construction logic.
    Method Chaining for Simplicity → Allows step-by-step object building.
'''


'''
Aspect                     | Builder Pattern                                           | Chain of Responsibility Pattern                   
----------------------------------------------------------------------------------------------------------
Purpose                    | Helps create complex objects step by step.                | Passes a request through multiple handlers.    
Main Focus                 | Controls how an object is built.                          | Decouples sender and receiver for flexibility.  
Flow of Execution          | Uses method chaining to add parts to an object.           | Request moves through handlers until one processes it.  
Example Use Case           | Making a custom burger, car, or house.                    | Handling support tickets, logging, or permissions.  
Real-Life Analogy          | 🏗️ Building a burger by adding one ingredient at a time. | 📬 A request going through different levels of approval in a company.  

'''
