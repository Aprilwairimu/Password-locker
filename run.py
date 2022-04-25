#!/usr/bin/env python3.9
# from profile import run
from optparse import Option

# from jmespath import search
from credentials import Credentials
from user import User
import string
from random import *

def create_user(username,password):
    """
    Function to create new user
    """
    new_user = User(username,password)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user()

def delete_user(user):
    """
    Function to delete user
    """
    user.delete_user()

def display_user():
        '''
        method that displays the user
        '''
        return User.display_user()



def create_credentials(app_name,username,password):
    """
    Function to create new credentials
    """
    new_credentials = Credentials(app_name,username,password)
    return new_credentials

def save_credentials(credentials):
    """
    Function to save credentials
    """
    credentials.save_credentials()

def delete_credentials(credentials):
    """
    Function to delete credentials
    """
    Credentials.delete_credentials()

def display_credentials():
        '''
        method that returns the credentials
        '''
        return Credentials.display_credentials()

def find_credentials(credentials):
    """
    method that finds the credentials
    """
    return Credentials.find_credentials(credentials)

def existing_credentials (credentials):
    """
    method that finds existing credentials
    """
    return Credentials.credentials_exist(credentials)





def main():
   
    print("Hello Welcome to your Password locker.What is your name?")
    user_name = input()

    print(f"Hello {user_name}. would you like to login(LOGIN)")
    print('\n')
    # Option=input()
    while True:

        print("Use these short codes : ca - create a new account, dc - display credentials, fc -find a credentials, ex -exit the credentials list ")


        short_code = input().lower()

        if short_code == "ca":
            print("CREATING A NEW ACCOUNT")
            print("-"*10)

            print("app_name ....")
            app_name = input()

            print("user_name ....")
            user_name = input()

            print("password ....")
            password = input()

            save_credentials(create_credentials(app_name,user_name,password))
            print(f"New Account {app_name} user_name: {user_name} password: {password} created")
            print("\n")
            
           
        elif short_code =="dc":
            if display_credentials():
                print("Here is a list of all your accounts")
                print('\n')
                
                for credential in display_credentials():
                    print(f"{credential.app_name } {credential.user_name} {credential.password}")
                    print("\n")
            else:
                print("\n")
                print("You don't seem to have any accounts saved yet")
                print("\n")

        elif short_code == 'fc':

                    print("Enter the account name you want to search for")

                    search_credentials = input()
                    if existing_credentials(search_credentials):
                            search_cred = find_credentials(search_credentials)
                            print(f"{search_cred.app_name} {search_cred.user_name}")
                            print('-' * 20)

                            print(f"Password.......{search_cred.password}")
                           
                    else:
                            print("That account does not exist")

        elif short_code == "ex":
            print("bye........")
            break
        else:
            print("I really didn't get that. Please use the short codes")
   
        

            



        


if __name__ == '__main__':
    main()
        

    




