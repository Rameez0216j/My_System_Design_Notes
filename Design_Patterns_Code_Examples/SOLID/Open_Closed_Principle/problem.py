class DiscountCalculator:
    def calculate_discount(self, customer_type, amount):
        if customer_type == "Regular":
            return amount * 0.1  # 10% discount
        elif customer_type == "Premium":
            return amount * 0.2  # 20% discount
        else:
            return 0  # No discount

# Issue:
# - Adding a new customer type requires modifying the `calculate_discount` method.
# - This violates OCP because the existing class is not closed for modification.
