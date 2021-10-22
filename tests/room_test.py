import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Hitsville",5)

    def test_room_has_name(self):
        self.assertEqual("Hitsville",self.room.name)

    def test_room_has_entry_fee(self):
        self.assertEqual(5,self.room.entry_fee)

    def test_room_starts_empty(self):
        self.assertEqual(0,len(self.room.guest_list)

    # def test_check_in_guest(self):
    #     guest_to_check_in = Guest("Alan",40,"Last Christmas")
    #     self.room.check_in_guest(guest_to_check_in)
    #     self.assertEqual(1,len(self.guest_list))
