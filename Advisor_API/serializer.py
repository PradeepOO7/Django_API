from rest_framework import serializers

from Advisor_API.models import Advisor, Bookings, User

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bookings
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bookings
        exclude=['User_Id']
        depth=2