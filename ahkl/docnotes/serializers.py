from .models import Patients, Prescription
from rest_framework import serializers

class PatientsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Patients
		fields = ('name', 'photo','device_id','remark','date','status', 'schedule')

class PrescriptionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Prescription
		fields = ('patient','medication_type','quantity','interval','duration')





