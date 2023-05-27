from rest_framework import serializers
from .models import ModelManage

class ModelManageSerializer(serializers.ModelSerializer):
    model_file= serializers.FileField()
    model_name  = serializers.CharField()
    class Meta:
        model = ModelManage
        fields = '__all__'