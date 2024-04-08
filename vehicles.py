from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    license_number = models.CharField(max_length=35, unique=True)

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=35, unique=True)

class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField(null=True)

class VehicleMaintenanceRecord(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete= models.CASCADE, unique=True)
    maintenance_date = models.DateField()
    details = models.TextField()