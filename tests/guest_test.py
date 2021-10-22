import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Claire",25,"Skeleton Boy")

    def test_guest_has_name(self):
        self.assertEqual("Claire",self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(25,self.guest.money)

    def test_guest_has_fave_song(self):
        self.assertEqual("Skeleton Boy",self.guest.fave_song)

