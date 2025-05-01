# 🚨 Problem: Code duplication and inconsistent structure across classes.

class Coffee:
    def prepare(self):
        print("Boiling water")
        print("Brewing coffee")
        print("Pouring into cup")
        print("Adding sugar and milk")

class Tea:
    def prepare(self):
        print("Boiling water")
        print("Steeping tea")
        print("Pouring into cup")
        print("Adding lemon")

# ✅ Usage
coffee = Coffee()
coffee.prepare()

tea = Tea()
tea.prepare()
