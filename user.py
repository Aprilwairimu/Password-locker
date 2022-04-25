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


    def login_user(username,password):
        """
        function that checks whether a user exist and then login the user in.
        """
    
        check_user = User.verify_user(username,password)
        return check_user

