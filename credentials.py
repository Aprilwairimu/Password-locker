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

#     # def delete_contact(self):
#     #     Credentials.Credentials_list.remove(self)



            