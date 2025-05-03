# Existing Payment Processor
class OldPaymentProcessor:
    def process_payment(self, amount):
        return f"Processing payment of ${amount} using Old Payment System"

# New Payment System that uses a different method
class NewPaymentSystem:
    def make_payment(self, amount):
        return f"Payment of ${amount} processed using New Payment System"

# Client Code (Violates Open-Closed Principle)
class PaymentClient:
    def __init__(self, payment_type):
        if payment_type == "old":
            self.processor = OldPaymentProcessor()
        elif payment_type == "new":
            self.processor = NewPaymentSystem()  # Directly using a class with a different interface
        else:
            raise ValueError("Unknown payment type")

    def process(self, amount):
        return self.processor.process_payment(amount)  # Will break for NewPaymentSystem!

# Usage
client = PaymentClient("new")
print(client.process(100))  # ❌ ERROR: AttributeError: 'NewPaymentSystem' object has no attribute 'process_payment'


# Problems in This Approach:
# Incompatible Interfaces → OldPaymentProcessor uses process_payment(), but NewPaymentSystem uses make_payment().
# Tight Coupling → The client must know all payment system details, leading to maintenance issues.
# Scalability Issues → Adding another payment processor will require modifying the PaymentClient class.
