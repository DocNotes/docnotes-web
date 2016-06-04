from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Patients(models.Model):
    name = models.CharField(max_length=50, default="Name")
    photo = models.ImageField(upload_to="patient_photos")
    UUID = models.CharField(max_length=50, default="UUID")
    remark = models.CharField(max_length=255, default="Remark")

class Prescription(models.Model):
	name = models.ForeignKey('Patients', on_delete=models.CASCADE)
	medication = models.CharField(max_length=255, default="Medication")
	quantity = models.CharField(max_length=50, default="Quantity")



