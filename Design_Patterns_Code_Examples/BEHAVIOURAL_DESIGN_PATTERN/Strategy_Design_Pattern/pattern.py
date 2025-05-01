# Solution Using Strategy Pattern
from abc import ABC, abstractmethod

# Step 1: Define the Strategy Interface
# Abstract base class to define the structure of payment strategies
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        # Each concrete strategy must implement this method
        pass

# Step 2: Concrete Strategies
# Strategy for credit card payment
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        # Implementation for processing credit card payment
        print(f"Processing credit card payment of ${amount}")

# Strategy for PayPal payment
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        # Implementation for processing PayPal payment
        print(f"Processing PayPal payment of ${amount}")

# Strategy for Bitcoin payment
class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        # Implementation for processing Bitcoin payment
        print(f"Processing Bitcoin payment of ${amount}")

# Step 3: Context Class
# This class uses a strategy to process payments dynamically
class PaymentProcessorWithStrategy:
    def __init__(self, strategy: PaymentStrategy):
        # Initialize with a default strategy
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        # Allow changing the strategy dynamically at runtime
        self._strategy = strategy

    def process_payment(self, amount):
        # Delegate payment processing to the selected strategy
        self._strategy.pay(amount)

# Usage Example with Strategy Pattern
# Creating concrete strategy instances
credit_card = CreditCardPayment()
paypal = PayPalPayment()
bitcoin = BitcoinPayment()

# Initializing the context class with a default strategy
processor = PaymentProcessorWithStrategy(credit_card)

# Processing payment using the initial strategy
# Output: Processing credit card payment of $100
processor.process_payment(100)

# Changing the strategy to PayPal at runtime
processor.set_strategy(paypal)
# Output: Processing PayPal payment of $200
processor.process_payment(200)

# Changing the strategy to Bitcoin at runtime
processor.set_strategy(bitcoin)
# Output: Processing Bitcoin payment of $300
processor.process_payment(300)

# Benefits of the Strategy Design Pattern:
# 1. Open-Closed Principle: New payment methods can be added without modifying existing code.
# 2. Separation of Concerns: Each payment method is encapsulated in its own class.
# 3. Flexibility: Strategies can be changed dynamically at runtime, making the system adaptable.

# This implementation avoids the drawbacks of large if-else blocks and makes the code easier to extend and maintain.
