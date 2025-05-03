# Step 1: Define an Implementation Interface (Bridge)
class Color:
    def fill(self):
        pass

# Step 2: Implement Concrete Color Implementations
class Red(Color):
    def fill(self):
        return "Filled with Red Color"

class Blue(Color):
    def fill(self):
        return "Filled with Blue Color"

# Step 3: Define an Abstract Class (Abstraction)
class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass  # Implemented in subclasses

# Step 4: Create Concrete Shape Classes
class Circle(Shape):
    def draw(self):
        return f"Drawing a Circle - {self.color.fill()}"

class Square(Shape):
    def draw(self):
        return f"Drawing a Square - {self.color.fill()}"

# Client Code
red_circle = Circle(Red())
print(red_circle.draw())  # Output: Drawing a Circle - Filled with Red Color

blue_square = Square(Blue())
print(blue_square.draw())  # Output: Drawing a Square - Filled with Blue Color

# ✅ Benefits of Bridge:
# - Abstraction (`Shape`) and implementation (`Color`) can change independently.
# - New colors or shapes can be added **without modifying existing code**.
# - Reduces subclass explosion by using composition.
