import time
from queue import Queue

# 🎯 Database Connection Class
class DatabaseConnection:
    def __init__(self):
        print("Creating a new database connection...")
        time.sleep(1)  # Simulate expensive setup

    def execute_query(self, query):
        print(f"Executing query: {query}")

# 🏗️ Object Pool
class DatabaseConnectionPool:
    def __init__(self, size):
        self.pool = Queue(maxsize=size)
        for _ in range(size):
            self.pool.put(DatabaseConnection())

    def get_connection(self):
        return self.pool.get()  # Borrow connection

    def release_connection(self, connection):
        self.pool.put(connection)  # Return connection (Not termination, it is again made available to use)

# ✅ Usage
pool = DatabaseConnectionPool(size=2)  # Create a pool with 2 connections

# Borrow a connection
conn1 = pool.get_connection()
conn1.execute_query("SELECT * FROM users")

# Return connection to pool
pool.release_connection(conn1)

# Borrow another connection
conn2 = pool.get_connection()
conn2.execute_query("SELECT * FROM orders")

# Return connection
pool.release_connection(conn2)



'''
🚀 Why This Works Better?
    ✅ Efficient Reuse - Connections are reused instead of creating new ones.
    ✅ Faster Performance - Reduces the delay of object creation.
    ✅ Scalable for High Loads - Suitable for multithreading and network-heavy applications.
'''