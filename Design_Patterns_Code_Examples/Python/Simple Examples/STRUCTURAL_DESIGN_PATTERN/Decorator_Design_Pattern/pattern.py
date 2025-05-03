# Solution Using Decorator Pattern
from abc import ABC, abstractmethod

# Step 1: Define the Component Interface
# Abstract base class for all coffee objects
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Step 2: Concrete Component
# Basic Coffee implementation
class BasicCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Basic Coffee"

# Step 3: Decorator Base Class
# Abstract base class for coffee decorators
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

# Step 4: Concrete Decorators
# Adding milk functionality
# inherited constructor of parent as well
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2

    def description(self):
        return super().description() + ", Milk"

# Adding sugar functionality
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1

    def description(self):
        return super().description() + ", Sugar"

# Usage Example with Decorator Pattern
basic_coffee = BasicCoffee()
# Output: Cost: 5, Description: Basic Coffee
print(f"Cost: {basic_coffee.cost()}, Description: {basic_coffee.description()}")

milk_coffee = MilkDecorator(basic_coffee)
# Output: Cost: 7, Description: Basic Coffee, Milk
print(f"Cost: {milk_coffee.cost()}, Description: {milk_coffee.description()}")

sugar_milk_coffee = SugarDecorator(milk_coffee)
# Output: Cost: 8, Description: Basic Coffee, Milk, Sugar
print(f"Cost: {sugar_milk_coffee.cost()}, Description: {sugar_milk_coffee.description()}")

# Benefits of the Decorator Design Pattern:
# 1. Open-Closed Principle: New features can be added without modifying existing code.
# 2. Flexibility: Allows dynamic composition of features at runtime.
# 3. Reusability: Features are encapsulated in independent decorator classes.

# This implementation avoids the drawbacks of class explosion and provides a scalable solution for extending functionality dynamically.
