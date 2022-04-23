class Credentials:
    """"
    Class that generates credential for the user
    """
    Credentials_list = []

    def __init__(self,app_name,user_name,password):
        self.app_name =app_name
        self.user_name =user_name
        self.password =password
    
    def save_credentials(self):
        Credentials.Credentials_list.append(self)

    def delete_contact(self):
        Credentials.Credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.Credentials_list

    @classmethod
    def find_credential(cls, app_name):
        """
        Method that takes in a app_name and returns a credential
        """
        for credential in cls.credentials_list:
            if credential.app_name == app_name:
                return credential




            