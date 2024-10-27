from rest_framework import serializers
from ..models import Class_Section

class Serializer_Class_Section(serializers.ModelSerializer):
    class Meta:
        model = Class_Section
        fields = '__all__'