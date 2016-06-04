from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from docnotes.models import Patients, Prescription


# Create your views here.
def index(request):
    patients = Patients.objects.all()
    return render(request, "index.html", {'patients' : patients})
