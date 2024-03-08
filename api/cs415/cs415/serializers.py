from rest_framework import serializers
from cs415.models import User, UserAddress, DriverLicense, Vehicle, ParkingInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields ='__all__'

class DriverLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicense
        fields ='__all__'

class ParkingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingInfo
        fields ='__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields ='__all__'
