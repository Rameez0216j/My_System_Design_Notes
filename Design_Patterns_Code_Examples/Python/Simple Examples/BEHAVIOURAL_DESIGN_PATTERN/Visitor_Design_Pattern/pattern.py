# ✅ Solution: The Visitor Pattern moves operations into a separate class (ShapeVisitor),
# allowing new operations to be added without modifying the existing shape classes.

from abc import ABC, abstractmethod

# 🎨 Element Interface (Base Class for Shapes)
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass  # Each shape will allow visitors to operate on it

# ⚪ Concrete Element: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        return visitor.visit_circle(self)

# ◼ Concrete Element: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        return visitor.visit_rectangle(self)

# 🏗 Visitor Interface
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

# 📏 Concrete Visitor: Area Calculator
class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        return 3.14 * circle.radius * circle.radius  # Area of Circle

    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height  # Area of Rectangle

# 📏 Concrete Visitor: Perimeter Calculator
class PerimeterCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        return 2 * 3.14 * circle.radius  # Perimeter of Circle

    def visit_rectangle(self, rectangle):
        return 2 * (rectangle.width + rectangle.height)  # Perimeter of Rectangle

# ✅ Usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

area_visitor = AreaCalculator()
perimeter_visitor = PerimeterCalculator()

print("Circle Area:", circle.accept(area_visitor))
print("Circle Perimeter:", circle.accept(perimeter_visitor))

print("Rectangle Area:", rectangle.accept(area_visitor))
print("Rectangle Perimeter:", rectangle.accept(perimeter_visitor))

# 🎯 Now, we can easily add new operations (e.g., `ScaleShapeVisitor`) without modifying the existing shape classes.


'''
+------------------------+--------------------------+----------------------+
|        Aspect          |    Without Visitor ❌    |    With Visitor ✅  |
+------------------------+--------------------------+----------------------+
| Adding New Operations  | Requires modifying every | Just create a new    |
|                        | class                    | Visitor              |
+------------------------+--------------------------+----------------------+
| Open/Closed Principle  | ❌ Violated              | ✅ Followed         |
+------------------------+--------------------------+----------------------+
| Code Maintainability   | Harder to scale          | More flexible        |
+------------------------+--------------------------+----------------------+

'''

