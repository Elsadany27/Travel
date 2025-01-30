from django.contrib import admin
from .models import Bus,Guests,Reservation
# Register your models here.

admin.site.register(Bus)
admin.site.register(Guests)
admin.site.register(Reservation)
