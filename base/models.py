from django.db import models
from django.contrib.auth.models import AbstractUser

# list of choices.
user_type_list = [('Frontdesk','Frontdesk'),('Accounting','Accounting'),('Restaurant','Restaurant'),('Management','Management')]
room_status_list = [('Available','Available'),('Unavailable','Unavailable')]
gender_list = [('Male','Male'),('Female','Female'),('Other','Other')]
bill_status_list = [('Paid','Paid'),('Unpaid','Unpaid')]
payment_method_list = [('Online','Online'),('Offline','Offline')]
food_type_list = [('Veg','Veg'),('Non-Veg','Non-Veg')]

class User(AbstractUser):#inherite abstract user in User class
    #columns for User table 
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200,default='User',null=True)
    user_type = models.CharField(max_length=20,choices=user_type_list)
    #to make the email field the required login creditials to login the system
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class RoomType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=200)
    room_no = models.IntegerField()
    bed_count = models.IntegerField()
    status = models.CharField(max_length=20, choices=room_status_list)
    room_type = models.ForeignKey(RoomType,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class CustomerDetail(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=200,choices=gender_list)
    work = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class Bill(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    amount = models.IntegerField()
    status = models.CharField(max_length=200,choices=bill_status_list)
    date = models.DateField()
    customer_detail = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class PaymentInfo(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE)
    paid_amount = models.IntegerField()
    payment_method = models.CharField(max_length=100, choices=payment_method_list)
    def __str__(self):
        return self.bill

class EmployeeInfo(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=200,choices=gender_list)
    joining_date = models.DateField()
    salary= models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class MenuType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    food_type = models.CharField(max_length=200,choices=food_type_list)
    price = models.IntegerField()
    menu_type= models.ForeignKey(MenuType,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    def __str__(self):
        return self.name

class Facilities(Service):
    pass
    
