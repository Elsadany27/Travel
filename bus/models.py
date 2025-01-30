from django.db import models

# Create your models here.
class Guests(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(max_length=2)
    phone=models.IntegerField(max_length=11)

    def __str__(self):
        return self.name
    

class Bus(models.Model):
    destination=models.CharField(max_length=20)
    busno=models.IntegerField(max_length=4)

    def __str__(self):
        return self.destination

class Reservation(models.Model):
    guset=models.ManyToManyField(Guests,related_name="reservation")
    bus=models.ManyToManyField(Bus,related_name="reservation")

    def __str__(self):
        return "reservation"