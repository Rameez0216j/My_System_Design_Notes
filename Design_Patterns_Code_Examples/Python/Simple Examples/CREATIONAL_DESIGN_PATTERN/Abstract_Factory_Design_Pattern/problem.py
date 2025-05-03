# Concrete Products
class MacButton:
    def render(self):
        return "Rendering Mac Button"

class MacCheckbox:
    def render(self):
        return "Rendering Mac Checkbox"

class WindowsButton:
    def render(self):
        return "Rendering Windows Button"

class WindowsCheckbox:
    def render(self):
        return "Rendering Windows Checkbox"

# Client Code
class GUIFactoryClient:
    def __init__(self, os_type):
        if os_type == "Mac":
            self.button = MacButton()
            self.checkbox = MacCheckbox()
        elif os_type == "Windows":
            self.button = WindowsButton()
            self.checkbox = WindowsCheckbox()
        else:
            raise ValueError("Unsupported OS type")
    
    def render_ui(self):
        return f"{self.button.render()} and {self.checkbox.render()}"

# Usage
client_mac = GUIFactoryClient("Mac")
print(client_mac.render_ui())  # Output: Rendering Mac Button and Rendering Mac Checkbox

client_windows = GUIFactoryClient("Windows")
print(client_windows.render_ui())  # Output: Rendering Windows Button and Rendering Windows Checkbox

# Problems with this implementation:
# 1. **Tight Coupling**: The client directly depends on concrete classes (MacButton, WindowsButton, etc.).
# 2. **Scalability Issues**: Adding a new OS type (e.g., Linux) requires modifying the client.
# 3. **Violation of Open-Closed Principle**: The client must be updated for every new product family.
