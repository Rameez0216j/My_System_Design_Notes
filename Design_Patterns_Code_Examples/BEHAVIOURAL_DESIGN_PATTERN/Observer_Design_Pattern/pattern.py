# Solution Using Observer Pattern
from abc import ABC, abstractmethod

# Step 1: Define the Observer Interface
# Abstract base class to define the structure of observers
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        # Each concrete observer must implement this method
        pass

# Step 2: Define the Subject Interface
# Abstract base class for subjects (observable objects)
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Step 3: Concrete Subject
# WeatherStation implements the Subject interface
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temp):
        self._temperature = temp
        self.notify_observers()

# Step 4: Concrete Observers
# Display devices that implement the Observer interface
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"Phone display updated: Temperature is now {temperature}°C")

class WindowDisplay(Observer):
    def update(self, temperature):
        print(f"Window display updated: Temperature is now {temperature}°C")

# Usage Example with Observer Pattern
station = WeatherStation()

# Creating observers
phone_display = PhoneDisplay()
window_display = WindowDisplay()

# Registering observers to the subject
station.register_observer(phone_display)
station.register_observer(window_display)

# Changing temperature and notifying observers
# Output:
# Phone display updated: Temperature is now 25°C
# Window display updated: Temperature is now 25°C
station.set_temperature(25)

# Removing an observer and updating temperature
station.remove_observer(window_display)
# Output:
# Phone display updated: Temperature is now 30°C
station.set_temperature(30)

# Benefits of the Observer Design Pattern:
# 1. Open-Closed Principle: New observers can be added without modifying the subject.
# 2. Loose Coupling: The subject and observers are independent, improving reusability and flexibility.
# 3. Automatic Notification: Observers are automatically notified of state changes, reducing manual intervention.

# This implementation avoids the drawbacks of tight coupling and provides a scalable solution for many-to-many relationships.