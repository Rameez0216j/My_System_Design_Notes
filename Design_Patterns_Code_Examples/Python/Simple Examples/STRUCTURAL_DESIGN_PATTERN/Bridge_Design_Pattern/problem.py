# Tight coupling between shape and color - leads to class explosion

class RedCircle:
    def draw(self):
        return "Drawing a Red Circle"

class BlueCircle:
    def draw(self):
        return "Drawing a Blue Circle"

class RedSquare:
    def draw(self):
        return "Drawing a Red Square"

class BlueSquare:
    def draw(self):
        return "Drawing a Blue Square"

# Client Code
print(RedCircle().draw())
print(BlueSquare().draw())

# 🔴 Problems:
# - If a new color (e.g., Green) is added, we must create `GreenCircle`, `GreenSquare`, etc.
# - Too many subclasses make maintenance difficult.
