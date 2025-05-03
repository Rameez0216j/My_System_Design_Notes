# ✅ Solution: Implement Memento Pattern for undo functionality.

# 📜 Memento: Stores the state of the Editor
class Memento:
    def __init__(self, state):
        self.state = state  # Stores the editor's content

# 🏗️ Originator: The main object whose state needs saving/restoring
class Editor:
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text

    def save(self):
        return Memento(self.content)  # Saves current state

    def restore(self, memento):
        self.content = memento.state  # Restores to a saved state

    def show(self):
        print(f"Editor Content: {self.content}")

# 🛡️ Caretaker: Manages the mementos
class History:
    def __init__(self):
        self.mementos = []

    def push(self, memento):
        self.mementos.append(memento)  # Save state

    def pop(self):
        return self.mementos.pop() if self.mementos else None  # Restore state

# ✅ Usage
editor = Editor()
history = History()

editor.write("Hello, ")
history.push(editor.save())  # Save state

editor.write("World!")
editor.show()

editor.restore(history.pop())  # Undo last change
editor.show()
