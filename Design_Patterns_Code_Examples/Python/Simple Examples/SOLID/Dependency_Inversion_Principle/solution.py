"""
    Definition: High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details, and details should depend on abstractions.

    Explanation:
    The Dependency Inversion Principle ensures that:
    ->  High-level modules (policy setters) remain flexible and reusable.
    ->  Low-level modules (implementation details) can be changed without impacting the high-level modules.
    ->  Dependencies are inverted: instead of high-level modules depending directly on low-level implementations, both depend on abstractions (e.g., interfaces or abstract classes).
"""

from abc import ABC, abstractmethod

# Abstract Input Device
class InputDevice(ABC):
    @abstractmethod
    def get_input(self):
        pass

# Abstract Output Device
class OutputDevice(ABC):
    @abstractmethod
    def display_output(self, data):
        pass

# Concrete implementations of InputDevice
class Keyboard(InputDevice):
    def get_input(self):
        return "Keyboard input"

class TouchScreen(InputDevice):
    def get_input(self):
        return "Touch input"

# Concrete implementations of OutputDevice
class Monitor(OutputDevice):
    def display_output(self, data):
        print(f"Displaying on monitor: {data}")

class Speaker(OutputDevice):
    def display_output(self, data):
        print(f"Playing through speaker: {data}")

# High-level module depends on abstractions
class Computer:
    def __init__(self, input_device: InputDevice, output_device: OutputDevice):
        self.input_device = input_device
        self.output_device = output_device

    def operate(self):
        input_data = self.input_device.get_input()
        self.output_device.display_output(input_data)

# Usage
keyboard = Keyboard()
monitor = Monitor()

computer = Computer(keyboard, monitor)
computer.operate()  # Output: Displaying on monitor: Keyboard input

touch_screen = TouchScreen()
speaker = Speaker()

computer_with_new_devices = Computer(touch_screen, speaker)
computer_with_new_devices.operate()  # Output: Playing through speaker: Touch input
