class Order:
    def process_order(self):
        # Placeholder method for order processing
        pass


class OrderProcessor:
    def __init__(self, order: Order):
        self.order = order

    def process(self):
        if self.order is None:
            print("No order to process.")
        else:
            self.order.process_order()

# Usage Example:

# Invalid Order (Null Check)
invalid_order = None
order_processor_invalid = OrderProcessor(invalid_order)
order_processor_invalid.process()  # Output: No order to process.
