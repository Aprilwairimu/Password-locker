class User:
    """
    Class that generates 
    """

    User_list = []

    def __init__(self,user_name,password):
        self.user_name =user_name
        self.password =password

    def save_user(self):
        User.User_list.append(self)

    def delete_user(self):
        User.User_list.remove(self)

    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.User_list

    # @classmethod
    # def login(cls):
    #     '''
    #     method that returns the credentials list
    #     '''
    #     return cls.Credentials
