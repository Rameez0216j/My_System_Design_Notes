# 🚨 Problem: Hardcoded evaluation logic, difficult to extend.

class Calculator:
    def evaluate(self, expression):
        if "+" in expression:
            parts = expression.split("+")
            return int(parts[0]) + int(parts[1])
        elif "-" in expression:
            parts = expression.split("-")
            return int(parts[0]) - int(parts[1])
        else:
            raise ValueError("Unsupported operation")

# ✅ Usage
calc = Calculator()
print(calc.evaluate("10+5"))  # Outputs: 15
print(calc.evaluate("10-5"))  # Outputs: 5
