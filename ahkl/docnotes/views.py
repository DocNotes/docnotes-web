from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Patients, Prescription
from rest_framework import viewsets
from .serializers import PatientsSerializer, PrescriptionSerializer 
from watson import search as watson

# Create your views here.
def index(request):
    patients = Patients.objects.all()
    medications = Prescription.objects.all()
    context_dict = {'patients' : patients, 'medications' : medications}
    return render_to_response("index.html", context_dict)

class PatientsViewSet(viewsets.ModelViewSet):
	queryset = Patients.objects.all()
	serializer_class = PatientsSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
	queryset = Prescription.objects.all()
	serializer_class = PrescriptionSerializer




