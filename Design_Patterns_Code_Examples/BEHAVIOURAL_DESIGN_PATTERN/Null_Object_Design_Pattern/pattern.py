from abc import ABC, abstractmethod

# Step 1: Define the Subject Interface (Common Interface for both real and Null objects)
class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass

# Step 2: Real Object (Concrete Implementation)
# Represents a real order with actual behavior
class RealOrder(Order):
    def __init__(self, order_id: int, customer_name: str):
        self.order_id = order_id
        self.customer_name = customer_name
    
    def process_order(self):
        print(f"Processing order {self.order_id} for {self.customer_name}")

# Step 3: Null Object (Represents the absence of an order)
# A special object that behaves like an Order, but doesn't do anything
class NullOrder(Order):
    def process_order(self):
        print("No order to process. Null object used.")

# Step 4: Client Code
class OrderProcessor:
    def __init__(self, order: Order):
        self.order = order

    def process(self):
        self.order.process_order()

# Usage Example:

# A valid order
real_order = RealOrder(1, "John Doe")
order_processor = OrderProcessor(real_order)
order_processor.process()  # Output: Processing order 1 for John Doe

# A "null" order (absence of an order)
null_order = NullOrder()
order_processor_null = OrderProcessor(null_order)
order_processor_null.process()  # Output: No order to process. Null object used.



"""
    Imagine a scenario where you are dealing with customer orders, and sometimes, 
    an order might not exist for a particular customer. Instead of returning null for such cases, 
    you can return a NullOrder object that behaves like a regular Order object but does 
    nothing when methods are called on it.
"""
