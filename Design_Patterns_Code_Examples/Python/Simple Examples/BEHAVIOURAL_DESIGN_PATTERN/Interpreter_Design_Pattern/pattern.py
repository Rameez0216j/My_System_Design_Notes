from abc import ABC, abstractmethod

# 📜 Abstract Expression Interface
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

# 🎯 Terminal Expression (Numbers)
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

# 🔄 Non-Terminal Expression (Addition)
class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

# 🔄 Non-Terminal Expression (Subtraction)
class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

# ✅ Usage
expr = Add(Number(10), Subtract(Number(5), Number(2)))  # (10 + (5 - 2))
print(expr.interpret())  # Outputs: 13
