import unittest
from user import User

class TestUser (unittest.TestCase):
    def setUp(self):
        self.new_user = User("April","A123$")

    def tearDown(self):
        User.User_list =[]

    def test_init(self):
        self.assertEqual(self.new_user.user_name,"April")
        self.assertEqual(self.new_user.password,"A123$")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.User_list),1)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("username","A123$") # new contact
        test_user.save_user() 
        self.new_user.delete_user()# Deleting a contact object
        self.assertEqual(len(User.User_list),1)

    
        
        


    def test_display_all_user(self):
          '''
          method that returns a list of all user saved
          '''

          self.assertEqual(User.display_user(),User.User_list)

    








if __name__ == '__main__':
    unittest.main()