# Decorator Design Pattern Implementation

# Problem Without Decorator Pattern (Code That Violates the Pattern)
# This implementation uses inheritance for extending functionality, leading to class explosion and lack of flexibility.
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Basic Coffee"

# Adding milk to coffee by extending the Coffee class
class MilkCoffee(Coffee):
    def cost(self):
        return super().cost() + 2

    def description(self):
        return super().description() + ", Milk"

# Adding sugar to coffee by extending the Coffee class
class SugarMilkCoffee(MilkCoffee):
    def cost(self):
        return super().cost() + 1

    def description(self):
        return super().description() + ", Sugar"

# Usage Example Without Decorator Pattern
basic_coffee = Coffee()
# Output: Cost: 5, Description: Basic Coffee
print(f"Cost: {basic_coffee.cost()}, Description: {basic_coffee.description()}")

milk_coffee = MilkCoffee()
# Output: Cost: 7, Description: Basic Coffee, Milk
print(f"Cost: {milk_coffee.cost()}, Description: {milk_coffee.description()}")

sugar_milk_coffee = SugarMilkCoffee()
# Output: Cost: 8, Description: Basic Coffee, Milk, Sugar
print(f"Cost: {sugar_milk_coffee.cost()}, Description: {sugar_milk_coffee.description()}")

# Problems with this implementation:
# 1. Class explosion: Adding more features requires new classes for every combination.
# 2. Lack of flexibility: Changing the composition at runtime is not possible.