from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length = 10, choices = GENDER_CHOICES)

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=100)
    patients = models.ManyToManyField(Patient)

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES)

class PatientMedicalRecord(models.Model):
    paitent = models.OneToOneField(Patient, on_delete=models.CASCADE, unique=True)
    record_details = models.TextField()
    last_update = models.DateTimeField()