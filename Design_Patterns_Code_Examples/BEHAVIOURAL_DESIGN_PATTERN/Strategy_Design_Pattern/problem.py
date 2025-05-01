# Strategy Design Pattern Implementation

# Problem Without Strategy Pattern (Code That Violates the Pattern)
# This implementation uses a large if-else block to handle different payment methods.
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processing credit card payment of ${amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of ${amount}")
        elif payment_type == "bitcoin":
            print(f"Processing Bitcoin payment of ${amount}")
        else:
            raise ValueError("Unsupported payment type")

# Usage Example Without Strategy Pattern
processor = PaymentProcessor()
# Output: Processing credit card payment of $100
processor.process_payment("credit_card", 100)
# Output: Processing PayPal payment of $200
processor.process_payment("paypal", 200)
# Output: Processing Bitcoin payment of $300
processor.process_payment("bitcoin", 300)

# Problems with this implementation:
# 1. Adding a new payment method requires modifying the class, violating the Open-Closed Principle.
# 2. Code is harder to maintain and scale as the number of payment methods grows.