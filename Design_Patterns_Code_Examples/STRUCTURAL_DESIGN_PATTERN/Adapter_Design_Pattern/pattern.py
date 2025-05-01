# Existing Payment Processor
class OldPaymentProcessor:
    def process_payment(self, amount):
        return f"Processing payment of ${amount} using Old Payment System"

# New Payment System with a different interface
class NewPaymentSystem:
    def make_payment(self, amount):
        return f"Payment of ${amount} processed using New Payment System"

# Adapter: Converts NewPaymentSystem's method to match OldPaymentProcessor's interface
class PaymentAdapter:
    def __init__(self, new_payment_system):
        self.new_payment_system = new_payment_system

    def process_payment(self, amount):
        return self.new_payment_system.make_payment(amount)  # Converts method call

# Client Code using Adapter
class PaymentClient:
    def __init__(self, payment_type):
        if payment_type == "old":
            self.processor = OldPaymentProcessor()
        elif payment_type == "new":
            self.processor = PaymentAdapter(NewPaymentSystem())  # Using Adapter
        else:
            raise ValueError("Unknown payment type")

    def process(self, amount):
        return self.processor.process_payment(amount)  # Now works for both systems!

# Usage
client1 = PaymentClient("old")
print(client1.process(100))  # ✅ Output: Processing payment of $100 using Old Payment System

client2 = PaymentClient("new")
print(client2.process(200))  # ✅ Output: Payment of $200 processed using New Payment System



# Key Benefits of the Adapter Pattern
# Solves Interface Mismatch → Enables old and new systems to work together without modifying existing code.
# Loose Coupling → The client class depends only on the adapter, not on implementation details.
# Scalability → Easily integrates new payment systems without modifying existing logic.