from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class DriverLicense(models.Model):
    driver_license_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("User", models.DO_NOTHING)
    driver_license_number = models.IntegerField()
    st = models.CharField(max_length=50)
    expiration_date = models.DateField()
    issue_date = models.DateField()

    class Meta:
        managed = False
        db_table = "driver_license"

    def __str__(self) -> str:
        return f"{self.user} {self.driver_license_number}"


class ParkingInfo(models.Model):
    parking_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey("Vehicle", models.DO_NOTHING)
    floor = models.IntegerField()
    section = models.CharField(max_length=1)
    bay_number = models.IntegerField()
    day_parked = models.DateField()
    length_days = models.IntegerField()
    pick_up_time = models.TimeField()

    class Meta:
        managed = False
        db_table = "parking_info"

    def __str__(self) -> str:
        return f"{self.floor} {self.section} {self.bay_number}"


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=40)
    email = models.CharField(unique=True, max_length=40)
    pass_word = models.CharField(max_length=30)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = "user"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    street_address = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    st = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user_address"

    def __str__(self) -> str:
        return f"{self.user} {self.street_address}, {self.st}"


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    vehicle_type = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    production_year = models.IntegerField(
        validators=[
            MinValueValidator(1920, message="grater than 1920"),
            MaxValueValidator(2024, message="no more than current year"),
        ],
    )
    color = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = "vehicle"

    def __str__(self) -> str:
        return f"{self.production_year} {self.make} {self.model}"
