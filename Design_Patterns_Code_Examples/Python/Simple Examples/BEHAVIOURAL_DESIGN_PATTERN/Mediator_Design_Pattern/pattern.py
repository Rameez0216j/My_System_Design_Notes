# ✅ SOLUTION: Introduce a Mediator to manage communication.

class ChatMediator:
    """ Centralized mediator that handles message exchange between users. """
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        """ Notifies all users except the sender. """
        for user in self.users:
            if user != sender:
                user.receive_message(message, sender)

class User:
    """ Users communicate through the mediator, avoiding direct dependencies. """
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)  # Register with the mediator

    def send_message(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive_message(self, message, sender):
        print(f"{self.name} received from {sender.name}: {message}")

# Creating a Mediator
chat_mediator = ChatMediator()

# Creating users and associating them with the mediator
alice = User("Alice", chat_mediator)
bob = User("Bob", chat_mediator)
charlie = User("Charlie", chat_mediator)

# Sending messages through the mediator
alice.send_message("Hello everyone!")
bob.send_message("Hey Alice, welcome!")
charlie.send_message("Hi all, glad to join!")


'''
✅ Benefits of Using the Mediator Pattern:
    ✔ Loose Coupling → User objects do not interact directly.
    ✔ Scalability → New users can be added without modifying existing ones.
    ✔ Centralized Control → Message flow is handled in one place.
    ✔ Better Maintainability → Reduces interdependencies, making debugging easier.
'''
