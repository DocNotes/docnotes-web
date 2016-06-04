from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from docnotes.models import Patients, Prescription


# Create your views here.
def index(request):
    patients = Patients.objects.all()
    medications = Prescription.objects.all()
    context_dict = {'patients' : patients, 'medications' : medications}
    return render_to_response("index.html", context_dict)
