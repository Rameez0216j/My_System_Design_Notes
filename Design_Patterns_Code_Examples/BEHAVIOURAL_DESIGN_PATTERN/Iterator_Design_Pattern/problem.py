class Playlist:
    def __init__(self, songs):
        self.songs = songs  # Store the list of songs

    def get_songs(self):
        return self.songs  # Exposes internal data (not recommended)

# Client Code
playlist = Playlist(["Song A", "Song B", "Song C", "Song D"])

# Issues:
# 1. Direct access to internal data (`get_songs()` exposes raw list).
# 2. Client must handle iteration manually (tight coupling).
# 3. No flexibility (e.g., reverse iteration requires extra code in the client).

print("Playing Songs (Manual Iteration):")
for i in range(len(playlist.get_songs())):
    print(playlist.get_songs()[i])  # Direct access (bad practice)
