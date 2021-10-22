import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Claire",25,"Hall of Fame")

    def test_guest_has_name(self):
        self.assertEqual("Claire",self.guest.name)

