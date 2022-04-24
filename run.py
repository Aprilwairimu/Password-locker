#!/usr/bin/env python3.9
# from profile import run
from optparse import Option
from credentials import Credentials
from user import User
import string
from random import *

def create_user(user_name,password):
    """
    Function to create new user
    """
    new_user = User(user_name,password)
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

def display_user(cls):
        '''
        method that displays the user
        '''
        return User.display_user()



def create_credentials(app_name,user_name,password):
    """
    Function to create new credentials
    """
    new_credentials = Credentials(app_name,user_name,password)
    return new_credentials

def save_credentials(credentials):
    """
    Function to save credentials
    """
    Credentials.save_credentials()

def delete_credentials(credentials):
    """
    Function to delete credentials
    """
    Credentials.delete_credentials()

def display_credentials(cls):
        '''
        method that returns the credentials
        '''
        return Credentials.display_credentials()



def main():
    while True:
        print("Hello Welcome to your Password locker.What is your name?")
        user_name = input()

        print(f"Hello {user_name}. would you like to login(LOGIN) use y for yes and n for no")
        print('\n')
        Option=input()

        print("Use these short codes : ca - create a new account, dc - display credentials, fc -find a credentials, ex -exit the credentials list ")


        short_code = input().lower()

        if short_code == "ca":
            print("LOGIN")
            print("user_name")
            user_name = input()

            print("password")
            password = input()

            save_user(create_user(user_name,password))
            print(f"New Account {user_name} {password} created")
            print("/n")
            print(f"user_name:{user_name}/n password:{password}")
   
        

            



        


if __name__ == '__main__':
    main()
        

    




