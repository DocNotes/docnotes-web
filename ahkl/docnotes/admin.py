from django.contrib import admin

from .models import Patients
from .models import Prescription
# Register your models here.

admin.site.register(Patients)
admin.site.register(Prescription)