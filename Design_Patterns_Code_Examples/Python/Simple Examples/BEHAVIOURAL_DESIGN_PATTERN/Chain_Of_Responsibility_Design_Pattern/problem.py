# Code that violates the Chain of Responsibility Pattern by using if-else blocks
class RequestHandler:
    def handle(self, request):
        if request == "A":
            print("Handler A processed the request")
        elif request == "B":
            print("Handler B processed the request")
        elif request == "C":
            print("Handler C processed the request")
        else:
            print("No handler could process the request.")

# Usage Example Violating Chain of Responsibility:
handler = RequestHandler()

# Directly using if-else statements to handle requests
handler.handle("A")  # Should be handled by Handler A in the chain
handler.handle("B")  # Should be handled by Handler B in the chain
handler.handle("C")  # Should be handled by Handler C in the chain
handler.handle("D")  # No handler can process "D"
