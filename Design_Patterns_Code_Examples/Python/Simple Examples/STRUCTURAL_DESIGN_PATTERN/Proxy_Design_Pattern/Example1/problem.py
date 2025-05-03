class RealImage:
    def __init__(self, filename: str):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

# Usage Example Violating Proxy Pattern:

# Creating RealImage instance directly
image = RealImage("image2.jpg")

# Loading and displaying the image without any control (directly calling load_image)
image.display()  # Output: Loading image: image2.jpg \n Displaying image: image2.jpg
