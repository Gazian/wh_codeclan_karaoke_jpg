import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Skeleton Boy","Friendly Fires","Indie")

    def test_song_has_song_title(self):
        self.assertEqual("Skeleton Boy",self.song.song_title)

    def test_song_has_artist(self):
        self.assertEqual("Friendly Fires",self.song.artist)
    
    def test_song_has_genre(self):
        self.assertEqual("Indie",self.song.genre)