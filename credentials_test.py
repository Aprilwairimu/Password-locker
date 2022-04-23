import unittest
from credentials import Credentials

class TestCredentials (unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("Facebook","April","A123#")
    

    def tearDown(self):
        Credentials.Credentials_list =[]

    def test_init(self):
        self.assertEqual(self.new_credentials.app_name,"Facebook")
        self.assertEqual(self.new_credentials.user_name,"April")
        self.assertEqual(self.new_credentials.password,"A123#")

    
    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.Credentials_list),1)

    def test_save_multiple_credentials(self):
          self.new_credentials.save_credentials()
          test_credential = Credentials("Instagram","username","1234#") # new contact
          test_credential.save_credentials()
          self.assertEqual(len(Credentials.Credentials_list),2)

    def test_display_all_credentials(self):
          '''
          method that returns a list of all credentials saved
          '''

          self.assertEqual(Credentials.display_credentials(),Credentials.Credentials_list)

    
    def test_delete_credentials(self):
          self.new_credentials.save_credentials()
          test_credentials = Credentials("Instagram","username","1234#") # new contact
          test_credentials.save_credentials() 
          self.new_credentials.delete_contact()# Deleting a credential object
          self.assertEqual(len(Credentials.Credentials_list),1)















if __name__ == '__main__':
    unittest.main()