# Solution Using Chain of Responsibility Pattern
from abc import ABC, abstractmethod

# Step 1: Define the Handler Interface
# Abstract base class to define the structure of handlers
class Handler(ABC):
    def __init__(self):
        self.next_handler = None  # Next handler in the chain

    @abstractmethod
    def handle(self, request):
        # Each concrete handler must implement this method
        pass

    def set_next(self, handler: 'Handler'):
        self.next_handler = handler
        return handler  # Allows chaining of handlers

# Step 2: Concrete Handlers
# Concrete handler that processes "A" requests
class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Handler A handled the request")
        elif self.next_handler:
            self.next_handler.handle(request)  # Pass the request to the next handler

# Concrete handler that processes "B" requests
class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Handler B handled the request")
        elif self.next_handler:
            self.next_handler.handle(request)  # Pass the request to the next handler

# Concrete handler that processes "C" requests
class ConcreteHandlerC(Handler):
    def handle(self, request):
        if request == "C":
            print("Handler C handled the request")
        elif self.next_handler:
            self.next_handler.handle(request)  # Pass the request to the next handler

# Step 3: Usage Example with Chain of Responsibility
# Creating concrete handlers
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_c = ConcreteHandlerC()

# Set up the chain: handler_a -> handler_b -> handler_c
handler_a.set_next(handler_b).set_next(handler_c)

# Testing the chain with different requests
print("Testing with request A:")
handler_a.handle("A")  # Handled by Handler A

print("\nTesting with request B:")
handler_a.handle("B")  # Handled by Handler B

print("\nTesting with request C:")
handler_a.handle("C")  # Handled by Handler C

# Step 4: Demonstrating a case where no handler can process the request
print("\nTesting with an unhandled request:")
handler_a.handle("D")  # No handler can process "D"

# Benefits of the Chain of Responsibility Design Pattern:
# 1. Open-Closed Principle: You can add new handlers without modifying existing code.
# 2. Reduced Coupling: Handlers don’t need to know about each other, they just pass requests down the chain.
# 3. Flexible and Scalable: The chain can be easily extended or modified to suit different needs.

# This implementation supports a scalable solution where requests are processed by multiple handlers, 
# with each handler deciding whether to handle the request or pass it along the chain.
