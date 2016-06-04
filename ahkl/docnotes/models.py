from __future__ import unicode_literals

from django.db import models
from django.views.generic import TemplateView
from datetime import datetime, date

# Create your models here.



class Patients(models.Model):
    name = models.CharField(max_length=50, default="Name")
    photo = models.ImageField(upload_to="patient_photos")
    id = models.AutoField(primary_key=True)
    remark = models.CharField(max_length=255, default="Remark")
    date = models.DateTimeField(default=datetime.now, blank=True)

class Prescription(models.Model):
	ONE = '1 time a day'
	TWO = '2 times a day'
	THREE = '3 times a day'
	FOUR = '4 times a day'
	FIVE = '5 times a day'
	SIX = '6 times a day'

	TIME_INTERVALS = (
	(ONE, '1 time a day'),
	(TWO, '2 times a day'),
	(THREE, '3 times a day'),
	(FOUR, '4 times a day'),
	(FIVE, '5 times a day'),
	(SIX, '6 times a day'),
)

	patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
	medication_type = models.CharField(max_length=255, default="Medication")
	quantity = models.CharField(max_length=50, default="Quantity")
	interval = models.CharField(max_length=5, choices=TIME_INTERVALS, default="Time")


