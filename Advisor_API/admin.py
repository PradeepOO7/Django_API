from django.contrib import admin
from .models import Advisor,User,Bookings

# Register your models here.
admin.site.register(Advisor)
admin.site.register(User)
admin.site.register(Bookings)