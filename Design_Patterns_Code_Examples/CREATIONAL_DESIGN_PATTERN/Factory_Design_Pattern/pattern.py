# Solution Using Factory Pattern
from abc import ABC, abstractmethod

# Step 1: Define an Abstract Shape Interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Implement Concrete Shapes
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Triangle(Shape):
    def draw(self):
        return "Drawing a Triangle"

# Step 3: Create a Factory Class
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        elif shape_type == "Triangle":
            return Triangle()
        else:
            raise ValueError("Unknown shape type")

# Usage Example with Factory Pattern
shape1 = ShapeFactory.create_shape("Circle")
print(shape1.draw())  # Output: Drawing a Circle

shape2 = ShapeFactory.create_shape("Square")
print(shape2.draw())  # Output: Drawing a Square

shape3 = ShapeFactory.create_shape("Triangle")
print(shape3.draw())  # Output: Drawing a Triangle

# Benefits of the Factory Pattern:
# 1. Loose Coupling: The client code depends only on the abstract `Shape` interface and the factory, not on concrete implementations.
# 2. Scalability: Adding new shapes (e.g., `Triangle`) does not require modifying existing client code or the factory interface.
# 3. Centralized Object Creation: All object creation logic is centralized in the factory class.

# This implementation adheres to the Open-Closed Principle and makes the code more maintainable and extensible.
