from __future__ import unicode_literals

from django.db import models
from django.views.generic import TemplateView
from datetime import datetime, date
from watson import search as watson


# Create your models here.


class Patients(models.Model):
    name = models.CharField(max_length=50, default="Name")
    photo = models.ImageField(upload_to="patient_photos", blank=True)
    device_id = models.AutoField(primary_key=True)
    remark = models.CharField(max_length=255, default="Remark")
    date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=255, default="active")
    schedule = models.CharField(max_length=255, default="completed")


class Prescription(models.Model):
	CHOICES = [(i,i) for i in range(4)]

	patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
	medication_type = models.CharField(max_length=255, default="Medication")
	quantity = models.CharField(max_length=50, default="Quantity")
	duration = models.DateTimeField(default=datetime.now, blank = True)
	time_interval = models.IntegerField(max_length=10, choices=CHOICES, default=1)



