import time

class RealDataFetcher:
    def fetch_data(self, query: str):
        # Simulate an expensive operation (e.g., network call, database query)
        print(f"Fetching data for query: '{query}'...")
        time.sleep(2)  # Simulate delay in data fetching
        return f"Data for {query}"

# Usage Example Violating Proxy Pattern:

# Creating RealDataFetcher instance directly
data_fetcher = RealDataFetcher()

# First fetch will always go to the RealDataFetcher (no cache)
print(data_fetcher.fetch_data("query1"))  # Output: Fetching data for query: 'query1' ...

# Second fetch will also go to the RealDataFetcher (no cache)
print(data_fetcher.fetch_data("query1"))  # Output: Fetching data for query: 'query1' ...
