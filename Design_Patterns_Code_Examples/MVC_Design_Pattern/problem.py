# 🚨 Problem: The UI (View), Business Logic (Model), and User Interaction (Controller) are tightly coupled.
# This violates separation of concerns and makes the code difficult to scale.

class App:
    def __init__(self):
        self.user_data = {}  # Directly handling data

    def add_user(self, name, age):
        self.user_data[name] = age  # Business logic inside the UI class

    def display_users(self):
        for name, age in self.user_data.items():
            print(f"User: {name}, Age: {age}")  # UI logic in the same class

# ✅ Usage
app = App()
app.add_user("Alice", 25)
app.add_user("Bob", 30)
app.display_users()

# ❌ If we want to change how data is stored (e.g., use a database), we must modify this class.
# ❌ If we want a web-based UI instead of print(), we must modify this class.
