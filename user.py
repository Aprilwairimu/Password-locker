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
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

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
