# Problem Without Flyweight Pattern

class Character:
    def __init__(self, char, font, size, color):
        self.char = char
        self.font = font
        self.size = size
        self.color = color

    def display(self):
        return f"Character: {self.char}, Font: {self.font}, Size: {self.size}, Color: {self.color}"

# Client Code: Creating many characters with redundant font properties
characters = [
    Character('A', 'Arial', 12, 'Black'),
    Character('B', 'Arial', 12, 'Black'),
    Character('C', 'Arial', 12, 'Black'),
]

for char in characters:
    print(char.display())

# Problems:
# 1. Each character has duplicate font information, increasing memory usage.
# 2. Adding more characters exponentially increases memory consumption.
