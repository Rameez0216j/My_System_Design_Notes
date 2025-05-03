from collections.abc import Iterator, Iterable  

# Concrete Iterator
class PlaylistIterator(Iterator):
    def __init__(self, playlist):
        self._playlist = playlist  # Store reference to playlist
        self._index = 0  # Start at the first song

    def __next__(self):
        """ Returns the next song or raises StopIteration. """
        if self._index < len(self._playlist.songs):
            song = self._playlist.songs[self._index]  
            self._index += 1  
            return song  
        raise StopIteration  # Stop iteration when out of bounds

# Concrete Reverse Iterator
class ReversePlaylistIterator(Iterator):
    def __init__(self, playlist):
        self._playlist = playlist
        self._index = len(playlist.songs) - 1  # Start at the last song

    def __next__(self):
        """ Returns the previous song (reverse order). """
        if self._index >= 0:
            song = self._playlist.songs[self._index]
            self._index -= 1  
            return song
        raise StopIteration  # Stop iteration when out of bounds

# Playlist (Iterable Collection)
class Playlist(Iterable):
    def __init__(self, songs):
        self.songs = songs  # Store the list of songs

    def __iter__(self):
        """ Returns a forward iterator. """
        return PlaylistIterator(self)

    def reverse_iter(self):
        """ Returns a reverse iterator. """
        return ReversePlaylistIterator(self)

# Client Code
playlist = Playlist(["Song A", "Song B", "Song C", "Song D"])

print("\nPlaying Songs (Forward):")
for song in playlist:
    print(song)  # Uses __iter__() --> song = iterator.__next__()  Retrieves the next song (Internally)

print("\nPlaying Songs (Reverse):")
for song in playlist.reverse_iter():
    print(song)  # Uses reverse_iter()
