'''
Real-Life Example: A Tax Calculation System
Scenario:
    Imagine you are designing a shopping cart that contains different types of items like Electronics, Groceries, and Clothes. Each item has a different tax calculation. Instead of modifying the item classes whenever tax rules change, we can use the Visitor Pattern.

Implementation:
    Visitor Interface → Defines tax calculation for different items.
    Concrete Visitor (TaxCalculator) → Implements tax logic.
    Element Interface (Item) → Accepts the visitor.
    Concrete Elements (Electronics, Groceries, Clothes) → Implement accept method.
'''


from abc import ABC, abstractmethod

# Step 1: Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_electronics(self, item):
        pass

    @abstractmethod
    def visit_groceries(self, item):
        pass

    @abstractmethod
    def visit_clothes(self, item):
        pass

# Step 2: Concrete Visitor (Tax Calculator)
class TaxCalculator(Visitor):
    def visit_electronics(self, item):
        tax = item.price * 0.18  # 18% tax
        return f"Electronics Tax: ${tax:.2f}"

    def visit_groceries(self, item):
        tax = item.price * 0.05  # 5% tax
        return f"Groceries Tax: ${tax:.2f}"

    def visit_clothes(self, item):
        tax = item.price * 0.12  # 12% tax
        return f"Clothes Tax: ${tax:.2f}"

# Step 3: Element Interface
class Item(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def accept(self, visitor):
        pass

# Step 4: Concrete Elements
class Electronics(Item):
    def accept(self, visitor):
        return visitor.visit_electronics(self)

class Groceries(Item):
    def accept(self, visitor):
        return visitor.visit_groceries(self)

class Clothes(Item):
    def accept(self, visitor):
        return visitor.visit_clothes(self)

# Step 5: Client Code
items = [Electronics(1000), Groceries(500), Clothes(800)]
visitor = TaxCalculator()

for item in items:
    print(item.accept(visitor))
