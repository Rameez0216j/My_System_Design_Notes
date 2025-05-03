from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products for Mac
class MacButton(Button):
    def render(self):
        return "Rendering Mac Button"

class MacCheckbox(Checkbox):
    def render(self):
        return "Rendering Mac Checkbox"

# Concrete Products for Windows
class WindowsButton(Button):
    def render(self):
        return "Rendering Windows Button"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering Windows Checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factory for Mac
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# Concrete Factory for Windows
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Client Code
class GUIFactoryClient:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render_ui(self):
        return f"{self.button.render()} and {self.checkbox.render()}"

# Usage
mac_factory = MacFactory()
client_mac = GUIFactoryClient(mac_factory)
print(client_mac.render_ui())  # Output: Rendering Mac Button and Rendering Mac Checkbox

windows_factory = WindowsFactory()
client_windows = GUIFactoryClient(windows_factory)
print(client_windows.render_ui())  # Output: Rendering Windows Button and Rendering Windows Checkbox
