from abc import ABC, abstractmethod
import time

# Step 1: Define the Subject Interface
# This interface defines the common operation for both the RealSubject and Proxy
class DataFetcher(ABC):
    @abstractmethod
    def fetch_data(self, query: str):
        pass

# Step 2: RealSubject (DataFetcher)
# The RealSubject is responsible for fetching data from the slow external source (e.g., API or DB)
class RealDataFetcher(DataFetcher):
    def fetch_data(self, query: str):
        # Simulate an expensive operation (e.g., network call, database query)
        print(f"Fetching data for query: '{query}'...")
        time.sleep(2)  # Simulate delay in data fetching
        return f"Data for {query}"

# Step 3: Proxy (Cache Proxy)
# The Proxy handles caching and fetches data from RealSubject when not available in cache
class CachedDataFetcher(DataFetcher):
    def __init__(self):
        self.cache = {}
        self.real_data_fetcher = RealDataFetcher()

    def fetch_data(self, query: str):
        # Check if the data is already cached
        if query in self.cache:
            print(f"Cache hit for query: '{query}'")
            return self.cache[query]
        else:
            # If not in cache, fetch the data from RealSubject and cache it
            print(f"Cache miss for query: '{query}'")
            data = self.real_data_fetcher.fetch_data(query)
            self.cache[query] = data
            return data

# Usage Example with Proxy Pattern:

# Creating CachedDataFetcher (Proxy)
data_fetcher = CachedDataFetcher()

# First fetch will go to the RealDataFetcher (Cache miss)
print(data_fetcher.fetch_data("query1"))  # Output: Fetching data for query: 'query1' ...

# Second fetch will return the cached result (Cache hit)
print(data_fetcher.fetch_data("query1"))  # Output: Cache hit for query: 'query1'

# Fetching another data (Cache miss)
print(data_fetcher.fetch_data("query2"))  # Output: Fetching data for query: 'query2' ...
