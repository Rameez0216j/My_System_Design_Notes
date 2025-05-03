# 🚨 Problem: Creating new database connections every time is inefficient.

import time

class DatabaseConnection:
    def __init__(self):
        print("Creating a new database connection...")
        time.sleep(1)  # Simulate expensive creation process

    def execute_query(self, query):
        print(f"Executing query: {query}")

# ✅ Usage
db1 = DatabaseConnection()  # Creates a new connection
db1.execute_query("SELECT * FROM users")

db2 = DatabaseConnection()  # Creates another new connection
db2.execute_query("SELECT * FROM orders")



'''
🔴 Issues:
    ❌ High Resource Usage – Every request creates a new database connection.
    ❌ Slow Performance – Database creation is slow.
    ❌ Not Scalable – Cannot handle many requests efficiently.
'''