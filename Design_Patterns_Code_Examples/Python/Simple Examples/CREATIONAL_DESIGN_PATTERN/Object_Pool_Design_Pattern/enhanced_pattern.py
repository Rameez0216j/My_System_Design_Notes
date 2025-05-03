import time
import logging
from queue import Queue, Empty

# 🔹 Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 🎯 Database Connection Class
class DatabaseConnection:
    def __init__(self, conn_id):
        self.conn_id = conn_id
        logging.info(f"🔗 Creating database connection {conn_id}...")
        time.sleep(1)  # Simulate expensive setup

    def execute_query(self, query):
        logging.info(f"📝 [Connection {self.conn_id}] Executing query: {query}")

# 🏗️ Object Pool (Manages Reusable Connections)
class DatabaseConnectionPool:
    def __init__(self, size):
        self.pool = Queue(maxsize=size)
        for i in range(size):
            self.pool.put(DatabaseConnection(i + 1))  # Create initial connections

    def get_connection(self, timeout=5):
        try:
            return self.pool.get(timeout=timeout)  # Borrow connection (Waits if needed)
        except Empty:
            logging.error("⛔ No available connections! Please try again later.")
            return None  # Handle failure case gracefully

    def release_connection(self, connection):
        logging.info(f"🔄 Returning connection {connection.conn_id} to the pool.")
        self.pool.put(connection)  # Return connection (Reused, not terminated)

# ✅ Usage
if __name__ == "__main__":
    pool = DatabaseConnectionPool(size=2)  # Create a pool with 2 connections

    # Borrow a connection
    conn1 = pool.get_connection()
    if conn1:
        conn1.execute_query("SELECT * FROM users")
        pool.release_connection(conn1)  # Return connection to pool

    # Borrow another connection
    conn2 = pool.get_connection()
    if conn2:
        conn2.execute_query("SELECT * FROM orders")
        pool.release_connection(conn2)  # Return connection

    # 🚨 Trying to borrow when no connections are available
    conn3 = pool.get_connection()
    conn4 = pool.get_connection()  # This may fail if no connections are released

    if conn4:
        conn4.execute_query("DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY")
        pool.release_connection(conn4)
