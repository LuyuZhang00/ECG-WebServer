from rest_framework import serializers
from .models import HospitalManage

class HospitalManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalManage
        fields = '__all__'