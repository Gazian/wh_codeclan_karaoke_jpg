import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Hitsville",5)

    def test_room_has_name(self):
        self.assertEqual("Hitsville",self.room.name)

    def test_room_has_entry_fee(self):
        self.assertEqual(5,self.room.entry_fee)

    def test_room_starts_empty(self):
        self.assertEqual(0, self.room.room_guest_list_count())

    def test_check_in_guest(self):
        guest = Guest("Alan",40,"Last Christmas")
        self.room.check_in_guest(guest)
        self.assertEqual(1,self.room.room_guest_list_count())

    def test_check_out_guest(self):
        guest = Guest("Katy",25,"The best song in the World")
        self.room.check_in_guest(guest)
        self.room.check_out_guest(guest)
        self.assertEqual(0, self.room.room_guest_list_count())

    def test_song_list_starts_empty(self):
        self.assertEqual(0, self.room.room_song_count())

    def test_add_song_to_room(self):
        song = Song("It Was a Good Day","Ice Cube","Rap")
        self.room.add_song(song)
        self.assertEqual(1,self.room.room_song_count())
