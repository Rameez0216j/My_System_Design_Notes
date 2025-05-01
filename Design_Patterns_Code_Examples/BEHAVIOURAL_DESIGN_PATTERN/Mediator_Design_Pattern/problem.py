# ❌ PROBLEM: Objects communicate directly, leading to tight coupling.

class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, message, receiver):
        print(f"{self.name} sends message to {receiver.name}: {message}")
        receiver.receive_message(message, self)

    def receive_message(self, message, sender):
        print(f"{self.name} received message from {sender.name}: {message}")

# Creating users
user1 = User("Alice")
user2 = User("Bob")

# Direct communication (Tightly Coupled)
user1.send_message("Hello, Bob!", user2)
user2.send_message("Hey Alice, how are you?", user1)


'''
🔥 Issues With This Approach:
    ❌ Direct Dependency → User objects must know about each other.
    ❌ Difficult Scalability → Adding new users means modifying multiple classes.
    ❌ Code Duplication → Each user implements its own messaging logic.
'''
