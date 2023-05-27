from rest_framework import serializers
from .models import PatientManage

class PatientManageSerializer(serializers.ModelSerializer):
    # patient_id = serializers.IntegerField()
    # patient_name = serializers.CharField()
    class Meta:
        model = PatientManage
        fields = '__all__'