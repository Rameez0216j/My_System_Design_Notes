# 🧠 Memento Design Pattern

## 📌 Definition  
The **Memento Pattern** is a behavioral design pattern that allows an object to save and restore its previous state without violating encapsulation.  

## 📌 Components  
1. **Originator 🏗️** – The object whose state needs to be saved and restored.  
2. **Memento 📜** – Stores the state of the Originator.  
3. **Caretaker 🛡️** – Manages and stores Mementos, allowing undo/redo functionality.  

## 📌 Why Use Memento?  
✅ **Undo & Redo functionality** – Essential for text editors, games, etc.  
✅ **Encapsulation maintained** – State is stored without exposing object internals.  
✅ **History Tracking** – Saves different states of an object efficiently.  

## 📌 When to Use?  
✅ When implementing an **Undo/Redo feature** (e.g., text editors).  
✅ When saving **game progress** in gaming applications.  
✅ When maintaining **state history** for critical transactions.  

## ❌ Drawbacks  
- 🚧 **Memory Consumption** – Storing multiple states can use a lot of memory.  
- 🚧 **Complexity** – Managing multiple saved states can be tricky.  

## 🛠️ Common Use Cases  
- **Text Editors** (Undo/Redo)  
- **Game Development** (Saving game state)  
- **Transaction History** (Restoring previous settings)

## 🚀 Summary  

| Aspect            | Without Memento ❌ | With Memento ✅ |
|------------------|------------------|----------------|
| State Management | Not possible      | Possible       |
| Undo Feature     | ❌ No             | ✅ Yes         |
| Encapsulation    | Violated          | Maintained     |
| Use Cases       | Limited           | Flexible       |
