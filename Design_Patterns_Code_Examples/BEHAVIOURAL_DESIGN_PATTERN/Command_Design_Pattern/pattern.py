# Command Interface
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver Class
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

# Concrete Command for Turning Light ON
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

# Concrete Command for Turning Light OFF
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Invoker Class (Switch)
class Switch:
    def __init__(self):
        self.history = []  # Stores command history

    def execute_command(self, command):
        command.execute()
        self.history.append(command)  # Save for undo

    def undo_last(self):
        if self.history:
            self.history.pop().undo()

# Usage Example
light = Light()
switch = Switch()

light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

switch.execute_command(light_on)   # Output: Light is ON
switch.execute_command(light_off)  # Output: Light is OFF

switch.undo_last()  # Undo last command -> Output: Light is ON



'''
Benefits of Command Pattern
    1. Decouples Invoker from Receiver → Switch doesn't directly call Light methods.
    2. Easier to Add New Commands → Simply create new command classes.
    3. Supports Undo/Redo → Maintains a command history.

Real-World Analogy
    Think of a TV remote control:
    1. Each button (invoker) triggers a command.
    2. The command executes an action on the TV (receiver).
    3. The remote doesn't directly modify the TV but sends commands, making it flexible.
'''