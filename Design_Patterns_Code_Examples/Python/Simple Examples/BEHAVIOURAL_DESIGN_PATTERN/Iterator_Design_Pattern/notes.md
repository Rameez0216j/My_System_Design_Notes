# Iterator Design Pattern

## Why is it called the Iterator Design Pattern?
The **Iterator Design Pattern** is named so because it provides a standard way to **iterate (traverse) through a collection** without exposing its underlying structure. It encapsulates the traversal logic in a separate iterator class, making the collection easier to manage and extend.

## Key Features of Iterator Pattern
- **Encapsulation:** Hides the internal details of the collection.
- **Decoupling:** The client does not need to know the data structure's details.
- **Flexibility:** Supports different types of iteration (e.g., forward, reverse).
- **Reusability:** Iterators can be used across different collections.

## Issues Without Using the Iterator Pattern
1. **Direct access to internal data**  
   - Exposing internal data allows unintended modifications.
2. **Tightly coupled iteration logic**  
   - The client must manually handle traversal, leading to duplicated logic.
3. **No flexibility**  
   - Changing iteration behavior (e.g., reverse order) requires modifying the client code.

## When Does Each Method Get Called?
1. **`__init__()` (Iterator Initialization)**
   - Called **once** when the iterator instance is created inside `__iter__()`.
   - Initializes the iterator with a reference to the collection.

2. **`__iter__()` (Iterator Creation)**
   - Called when iteration starts (e.g., `for item in collection:`).
   - Returns the iterator instance.

3. **`__next__()` (Fetching the Next Item)**
   - Called each time the loop requests the next item.
   - Returns the next element or raises `StopIteration` when complete.

4. **`StopIteration` (Ending the Iteration)**
   - Raised when `__next__()` reaches the end of the collection.
   - Signals the loop to stop.

## Benefits of Using Iterator Pattern
✅ **Encapsulation** – Internal data is hidden from the client.  
✅ **Separation of Concerns** – Iteration logic is independent.  
✅ **Flexibility** – Can introduce different types of iterators (e.g., forward, reverse).  
✅ **Reusability** – Works for different iterable structures.  

---

This is how the **Iterator Design Pattern** enhances code maintainability, making it **scalable, reusable, and easy to modify**! 🚀
