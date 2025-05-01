# 🚨 Problem: The operations (area and perimeter calculations) are tightly coupled with the shape classes.
# If we need to add a new operation (e.g., `scale`), we must modify every shape class, violating Open/Closed Principle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius  # Area formula for a circle

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius  # Perimeter formula for a circle


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height  # Area formula for a rectangle

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)  # Perimeter formula for a rectangle


# ✅ Usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.calculate_area())
print("Circle Perimeter:", circle.calculate_perimeter())

print("Rectangle Area:", rectangle.calculate_area())
print("Rectangle Perimeter:", rectangle.calculate_perimeter())

# ❌ Adding a new operation (e.g., `scale()`) requires modifying every shape class.
