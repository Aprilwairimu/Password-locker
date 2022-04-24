#!/usr/bin/env python3.9
# from profile import run
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
    User.save_user()

def delete_user(user):
    """
    Function to delete user
    """
    User.delete_user()

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

def save_credentials(user):
    """
    Function to save credentials
    """
    Credentials.save_credentials()

def delete_credentials(user):
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
    print("")




