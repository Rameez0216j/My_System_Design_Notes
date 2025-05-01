# Factory Design Pattern Implementation

# Problem Without Factory Pattern (Code That Violates the Pattern)
# Direct instantiation of objects leads to tight coupling and lack of scalability.

class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

class ShapeClient:
    def __init__(self, shape_type):
        if shape_type == "Circle":
            self.shape = Circle()
        elif shape_type == "Square":
            self.shape = Square()
        else:
            raise ValueError("Unknown shape type")

    def draw_shape(self):
        return self.shape.draw()

# Usage Example Without Factory Pattern
client1 = ShapeClient("Circle")
print(client1.draw_shape())  # Output: Drawing a Circle

client2 = ShapeClient("Square")
print(client2.draw_shape())  # Output: Drawing a Square

# Problems with this implementation:
# 1. Tight Coupling: The `ShapeClient` class directly depends on the `Circle` and `Square` classes.
# 2. Scalability: Adding a new shape requires modifying the `ShapeClient` class, violating the Open-Closed Principle.
# 3. Code Duplication: The object creation logic is hardcoded and repeated.