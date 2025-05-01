# Observer Design Pattern Implementation

# Problem Without Observer Pattern (Code That Violates the Pattern)
# This implementation tightly couples the subject and observers, making the system less flexible and harder to maintain.
class WeatherStation:
    def __init__(self):
        self.temperature = 0

    def set_temperature(self, temp):
        self.temperature = temp
        # Notifying observers manually
        print(f"Temperature updated to {self.temperature}. Display updated.")

# Usage Example Without Observer Pattern
station = WeatherStation()
# Output: Temperature updated to 25. Display updated.
station.set_temperature(25)
# Output: Temperature updated to 30. Display updated.
station.set_temperature(30)

# Problems with this implementation:
# 1. Adding more observers requires modifying the WeatherStation class, violating the Open-Closed Principle.
# 2. The station is tightly coupled with the display logic, making it less reusable and harder to test.