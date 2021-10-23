import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Hitsville",5,6)

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
        self.room.print_guest_list()
        self.room.clear_guest_list()
        self.assertEqual(0, self.room.room_guest_list_count())

    def test_song_list_starts_empty(self):
        self.assertEqual(0, self.room.room_song_count())

    def test_add_song_to_room(self):
        song = Song("It Was a Good Day","Ice Cube","Rap")
        self.room.add_song(song)
        self.room.print_song_list()
        self.assertEqual(1,self.room.room_song_count())

    def test_clear_song_list_all(self):
        song_1 = Song("I shot the Sheriff","Bob Marley & the Wailers","Reggae")
        song_2 = Song("You Need To Calm Down","Taylor Swift","Pop")
        self.room.add_song(song_1)
        self.room.add_song(song_2)
        self.room.print_song_list()
        self.assertEqual(2,self.room.room_song_count())
        self.room.clear_song_list_all()
        self.assertEqual(0,self.room.room_song_count())

    def test_room_has_capacity_limit(self):
        self.assertEqual(6,self.room.capacity_limit)

    def test_room_capacity_limit_reached(self):
        room = Room ("Aftermath",5,3)
        guest_1 = Guest("Paul",24,"Ain't No Doubt")
        guest_2 = Guest("Shaz",45,"There's No Limit")
        guest_3 = Guest("Karen",30,"You Can't Touch This")
        guest_4 = Guest("Simon",15,"Broken Stones")
        self.room.check_in_guest(guest_1)
        self.room.room_capacity_limit_reached()
        self.room.check_in_guest(guest_2)
        self.room.room_capacity_limit_reached()
        self.room.check_in_guest(guest_3)
        self.room.room_capacity_limit_reached()
        # self.room.check_in_guest(guest_4)
        # self.room.room_capacity_limit_reached()
        self.assertEqual(3,self.room.room_guest_list_count())
        
        
