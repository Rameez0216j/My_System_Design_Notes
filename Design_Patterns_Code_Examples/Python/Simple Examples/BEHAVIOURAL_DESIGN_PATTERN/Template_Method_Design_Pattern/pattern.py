# ✅ Solution: Use the Template Method pattern for a structured and reusable approach.

from abc import ABC, abstractmethod

# 📜 Abstract Class: Defines the template method
class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self):
        pass  # Must be implemented by subclasses

    @abstractmethod
    def add_condiments(self):
        pass  # Must be implemented by subclasses

# 🏗️ Concrete Class: Coffee
class Coffee(Beverage):
    def brew(self):
        print("Brewing coffee")

    def add_condiments(self):
        print("Adding sugar and milk")

# 🏗️ Concrete Class: Tea
class Tea(Beverage):
    def brew(self):
        print("Steeping tea")

    def add_condiments(self):
        print("Adding lemon")

# ✅ Usage
coffee = Coffee()
coffee.prepare()

tea = Tea()
tea.prepare()
