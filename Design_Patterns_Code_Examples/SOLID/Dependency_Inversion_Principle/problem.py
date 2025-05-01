class Keyboard:
    def get_input(self):
        return "Keyboard input"

class Monitor:
    def display_output(self, data):
        print(f"Displaying: {data}")

class Computer:
    def __init__(self):
        self.keyboard = Keyboard()
        self.monitor = Monitor()

    def operate(self):
        input_data = self.keyboard.get_input()
        self.monitor.display_output(input_data)

# Issue:
# - The `Computer` class directly depends on the `Keyboard` and `Monitor` classes.
# - Changing the input/output device (e.g., using a `TouchScreen` or `Speaker`) requires modifying the `Computer` class.
# - This violates DIP, as high-level modules (`Computer`) depend on low-level modules (`Keyboard` and `Monitor`).
