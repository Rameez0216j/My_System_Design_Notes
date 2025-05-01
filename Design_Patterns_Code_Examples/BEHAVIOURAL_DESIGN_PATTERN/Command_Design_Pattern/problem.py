# Receiver class
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

# Invoker directly calling receiver's method
class Switch:
    def __init__(self, light):
        self.light = light  # Tight coupling

    def press(self, action):
        if action == "ON":
            self.light.turn_on()
        elif action == "OFF":
            self.light.turn_off()

# Usage
light = Light()
switch = Switch(light)

switch.press("ON")   # Output: Light is ON
switch.press("OFF")  # Output: Light is OFF


'''
Problems in This Approach
    Tight Coupling → Switch is directly dependent on Light.
    No Undo/Redo Mechanism → No way to track or reverse actions.
    Difficult to Extend → Adding new actions requires modifying Switch, violating Open/Closed Principle.
'''


