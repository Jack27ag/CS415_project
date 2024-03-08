from django.contrib import admin
from .models import DriverLicense, ParkingInfo, User, UserAddress, Vehicle

admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(DriverLicense)
admin.site.register(Vehicle)
admin.site.register(ParkingInfo)