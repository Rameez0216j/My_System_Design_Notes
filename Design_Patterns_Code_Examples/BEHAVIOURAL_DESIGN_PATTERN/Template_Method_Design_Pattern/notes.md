# 📜 Template Method Design Pattern  

## 📌 Definition  
The **Template Method Pattern** is a behavioral design pattern that defines the skeleton of an algorithm in a base class but lets subclasses override specific steps without modifying the overall structure.  

## 📌 Components  
1. **Abstract Class 📖** – Defines the template method with steps.  
2. **Concrete Classes 🏗️** – Implement specific steps of the algorithm.  

## 📌 Why Use Template Method?  
✅ **Code Reusability** – Common logic stays in one place.  
✅ **Enforces a Structure** – Ensures a consistent algorithm flow.  
✅ **Encapsulation of Common Behavior** – Reduces duplicate code.  

## 📌 When to Use?  
✅ When multiple classes share a common workflow but differ in details.  
✅ When you want to **prevent changes to the overall algorithm structure**.  
✅ When designing frameworks that allow extensibility.  

## ❌ Drawbacks  
- 🚧 **Limited Flexibility** – Subclasses must follow the predefined structure.  
- 🚧 **Difficult to Change Algorithm Flow** – Any major change requires modifying the base class.  

## 🛠️ Common Use Cases  
- **Sorting Algorithms** (Different comparison logic but same structure)  
- **Game AI Behaviors** (Different enemy behaviors but same attack strategy)  
- **Data Processing Pipelines** (Parsing and transforming data in a defined sequence)  

## 🚀 Summary  

| Aspect            | Without Template Method ❌ | With Template Method ✅ |
|------------------|-------------------------|------------------------|
| Code Reusability | ❌ Low                    | ✅ High                 |
| Structure        | Inconsistent             | Predefined & Clear     |
| Encapsulation    | ❌ Violated               | ✅ Maintained           |
| Use Cases       | Limited                   | Flexible & Scalable    |
