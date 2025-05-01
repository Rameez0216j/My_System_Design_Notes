# 🏗️ Mediator Design Pattern  

## 📌 Introduction  
The **Mediator Design Pattern** is a behavioral pattern that helps in reducing **direct dependencies** between objects by introducing a **mediator** that manages communication between them.  

---

## 🧐 Why is it called the Mediator Design Pattern?  
It is called **Mediator** because it acts as a **middleman** between objects, **handling communication** and **reducing dependencies**. Instead of components interacting **directly** (which leads to complex interdependencies), they communicate **via a central mediator**.  

This **ensures**:  
✔ Objects do not need **direct references** to each other.  
✔ Communication is **centralized**, making it more **manageable**.  
✔ Components remain **loosely coupled**, improving **scalability**.  

---

## ⚡ Key Features  
✅ **Centralized Communication** – A mediator manages all interactions.  
✅ **Loose Coupling** – Components do not directly depend on each other.  
✅ **Simplifies Object Interaction** – Avoids complex interconnections.  
✅ **Encapsulates Behavior** – Message routing is handled in one place.  

---

## ❌ Issues Without Using the Mediator Pattern  
### Without a mediator, problems arise due to **direct communication**:  
❌ **Tightly Coupled Components** – Objects rely heavily on each other.  
❌ **Difficult Maintenance** – A change in one object affects many others.  
❌ **Complex Communication** – Too many interconnections create **spaghetti code**.  
❌ **Scalability Issues** – Adding new components requires modifying multiple objects.  

---

## ⏳ When Does Each Method Get Called?  
🔹 **`__init__()`** – Called **once** when the mediator instance is created.  
🔹 **`send()`** – Called when an object wants to **send a message** through the mediator.  
🔹 **`notify()`** – Called by the mediator to **notify objects** about an event.  

---

## ✅ Benefits of Using the Mediator Pattern  
✨ **Loose Coupling** – Objects do not interact directly but through a mediator.  
✨ **Better Maintainability** – Changing one component does not break others.  
✨ **Scalability** – New components can be added with minimal modifications.  
✨ **Centralized Control** – The mediator **manages communication**, making debugging easier.  

---

## 🎯 Conclusion  
The **Mediator Design Pattern** helps in **decoupling objects**, making code **more modular, scalable, and maintainable**. By introducing a mediator, we ensure **cleaner** and **more structured** communication between components.  

Using this pattern **reduces complexity** and **improves flexibility**, making it a great choice for systems with multiple interacting components. 🚀  
