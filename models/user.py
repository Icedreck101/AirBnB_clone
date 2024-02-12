#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel and represents a user in the system.
    """

    def __init__(self):
        """
        Initializes a new User instance.
        """
        super().__init__()
        self.__email = ""
        self.__password = ""
        self.__first_name = ""
        self.__last_name = ""

    @property
    def email(self):
        """
        Getter method for the email attribute.
        """
        return self.__email

    @property
    def password(self):
        """
        Getter method for the password attribute.
        """
        return self.__password

    @property
    def first_name(self):
        """
        Getter method for the first_name attribute.
        """
        return self.__first_name

    @property
    def last_name(self):
        """
        Getter method for the last_name attribute.
        """
        return self.__last_name

    @email.setter
    def email(self, value):
        """
        Setter method for the email attribute.
        """
        self.__email = value

    @password.setter
    def password(self, value):
        """
        Setter method for the password attribute.
        """
        self.__password = value

    @first_name.setter
    def first_name(self, value):
        """
        Setter method for the first_name attribute.
        """
        self.__first_name = value

    @last_name.setter
    def last_name(self, value):
        """
        Setter method for the last_name attribute.
        """
        self.__last_name = value
