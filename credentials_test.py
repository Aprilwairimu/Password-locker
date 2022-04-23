import unittest
from credentials import Credentials

class TestCredentials (unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("Twitter","April","A123#")
    

    def test_init(self):
        self.assertEqual(self.new_credentials.app_name"Password locker")
        self.assertEqual(self.new_credentials.user_name,"April")
        self.assertEqual(self.new_credentials.password,"A123#")