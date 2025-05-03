class FontStyle:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

class FontFactory:
    def __init__(self):
        self.fonts = {}

    def get_font(self, name, size, color):
        key = (name, size, color)
        if key not in self.fonts:
            self.fonts[key] = FontStyle(name, size, color)
        return self.fonts[key]

class Character:
    def __init__(self, char, font_style):
        self.char = char
        self.font_style = font_style  # Stores reference to the shared FontStyle object

    def print_details(self):
        print(f"Character: {self.char}, Font: {self.font_style.name}, Size: {self.font_style.size}, Color: {self.font_style.color}")

# Create a font factory
factory = FontFactory()

# Get a shared font style from factory
font1 = factory.get_font("Arial", 12, "Black")

# Assign the font to a character
charA = Character("A", font1)

# Print character details before modifying the font
charA.print_details()  # Output: Character: A, Font: Arial, Size: 12, Color: Black

# Modify the shared font style
font1.size = 20  # Modifying the existing font object

# Print character details again
charA.print_details()  # Output: Character: A, Font: Arial, Size: 20, Color: Black
