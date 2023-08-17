from django.db import models
from django.contrib.auth.models import AbstractUser

# choices for user_type.
user_type_list = [('Frontdesk','Frontdesk'),('Accounting','Accounting'),('Restaurant','Restaurant'),('Management','Management')]

class User(AbstractUser):#inherite abstract user in User class
    #columns for User table 
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200,default='User',null=True)
    user_type = models.CharField(max_length=20)

    #to make the email field the required login creditials to login the system
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']