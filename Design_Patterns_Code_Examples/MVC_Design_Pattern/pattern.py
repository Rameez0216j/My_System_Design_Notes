# ✅ Solution: The MVC pattern separates data, business logic, and UI.

# 🗂️ Model: Handles data storage and logic
class UserModel:
    def __init__(self):
        self.users = {}

    def add_user(self, name, age):
        self.users[name] = age  # Business logic is handled here

    def get_users(self):
        return self.users

# 🎨 View: Handles displaying data
class UserView:
    def display_users(self, users):
        for name, age in users.items():
            print(f"User: {name}, Age: {age}")  # Displays the user data

# 🎮 Controller: Handles user input and connects Model & View
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_user(self, name, age):
        self.model.add_user(name, age)

    def show_users(self):
        users = self.model.get_users()
        self.view.display_users(users)

# ✅ Usage
model = UserModel()
view = UserView()
controller = UserController(model, view)

controller.add_user("Alice", 25)
controller.add_user("Bob", 30)
controller.show_users()

# 🎯 Now, we can modify the Model (use a database), change the View (web-based UI), or extend functionality easily!
