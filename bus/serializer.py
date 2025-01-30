from rest_framework import serializers
from .models import Guests,Bus,Reservation

class GusetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guests
        fields=['pk','name','phone','reservation','age']

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields='__all__'   

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Reservation
        fields='__all__'         
