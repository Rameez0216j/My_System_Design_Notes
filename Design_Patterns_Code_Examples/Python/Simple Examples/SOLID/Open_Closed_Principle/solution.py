"""
    Definition: A class should be open for extension but closed for modification.
    Explanation: You should be able to add new functionality to a class without modifying its existing code. Violating this principle can lead to frequent changes in existing code, which may introduce bugs and increase maintenance overhead.
"""

from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount):
        pass

class RegularCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        return amount * 0.1  # 10% discount

class PremiumCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        return amount * 0.2  # 20% discount

class NoDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        return 0  # No discount

class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate_discount(self, amount):
        return self.strategy.calculate_discount(amount)

# Usage
regular_discount = DiscountCalculator(RegularCustomerDiscount())
print(regular_discount.calculate_discount(1000))  # Output: 100.0

premium_discount = DiscountCalculator(PremiumCustomerDiscount())
print(premium_discount.calculate_discount(1000))  # Output: 200.0

no_discount = DiscountCalculator(NoDiscount())
print(no_discount.calculate_discount(1000))  # Output: 0
