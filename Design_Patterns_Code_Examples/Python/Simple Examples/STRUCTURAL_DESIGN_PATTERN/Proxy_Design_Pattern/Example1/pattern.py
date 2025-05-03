from abc import ABC, abstractmethod

# Step 1: Define the Subject Interface
# This interface defines common operations for both the RealSubject and Proxy
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Step 2: RealSubject
# The RealSubject is the actual object that performs the work (loading and displaying the image)
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

# Step 3: Proxy
# The Proxy controls access to the RealSubject, here a Virtual Proxy for lazy loading
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self):
        # Only load the image if it hasn't been loaded yet
        if not self.real_image:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Usage Example with Proxy Pattern:

# Creating ProxyImage instance
image_proxy = ProxyImage("image1.jpg")

# The image is not loaded yet, so the proxy loads it when it's needed
image_proxy.display()  # Output: Loading image: image1.jpg \n Displaying image: image1.jpg

# Now, the image is cached, and it won't be loaded again
image_proxy.display()  # Output: Displaying image: image1.jpg
