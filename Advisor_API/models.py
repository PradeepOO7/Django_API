from django.db import models
from django.db.models.deletion import  DO_NOTHING
from django.db.models.fields import BigAutoField

# Create your models here.
class Advisor(models.Model):
    Advisor_Id=BigAutoField(primary_key=True)
    Name=models.CharField(max_length=60)
    Pic_url=models.CharField(max_length=256)

class User(models.Model):
    User_Id=BigAutoField(primary_key=True)
    Name=models.CharField(max_length=60)
    Email=models.CharField(max_length=60)
    Password=models.CharField(max_length=256)

class Bookings(models.Model):
    Booking_Id=BigAutoField(primary_key=True)
    Time=models.CharField(max_length=60)
    User_Id=models.ForeignKey(User,on_delete=DO_NOTHING)
    Advisor_Id=models.ForeignKey(Advisor,on_delete=DO_NOTHING)