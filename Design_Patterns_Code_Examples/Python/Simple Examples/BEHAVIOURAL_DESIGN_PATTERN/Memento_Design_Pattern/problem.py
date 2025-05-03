# 🚨 Problem: No proper state management, making undo impossible.

class Editor:
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text  # Directly modifying state

    def undo(self):
        # ❌ No proper undo functionality
        print("Undo is not implemented!")

    def show(self):
        print(f"Editor Content: {self.content}")

# ✅ Usage
editor = Editor()
editor.write("Hello, ")
editor.write("World!")
editor.show()

editor.undo()  # ❌ Cannot revert to previous state
