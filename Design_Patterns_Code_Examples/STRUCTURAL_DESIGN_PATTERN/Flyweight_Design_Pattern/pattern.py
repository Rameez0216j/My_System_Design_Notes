# Solution Using Flyweight Pattern

# Step 1: Flyweight class (Shared State)
class FontStyle:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

# Step 2: Flyweight Factory (Manages Object Reuse)
class FontFactory:
    _fonts = {}

    @staticmethod
    def get_font(font, size, color):
        key = (font, size, color)
        if key not in FontFactory._fonts:
            FontFactory._fonts[key] = FontStyle(font, size, color)
        return FontFactory._fonts[key]

# Step 3: Character Class (Unique State)
class Character:
    def __init__(self, char, font_style):
        self.char = char  # Unique state
        self.font_style = font_style  # Shared state

    def display(self):
        return f"Character: {self.char}, Font: {self.font_style.font}, Size: {self.font_style.size}, Color: {self.font_style.color}"

# Client Code: Using Flyweight Factory
factory = FontFactory()

characters = [
    Character('A', factory.get_font('Arial', 12, 'Black')),
    Character('B', factory.get_font('Arial', 12, 'Black')),
    Character('C', factory.get_font('Arial', 12, 'Black')),
]

for char in characters:
    print(char.display())

# Benefits:
# 1. Font properties are shared among multiple characters, reducing memory usage.
# 2. New characters can reuse existing font styles without creating duplicates.
