from rest_framework import serializers
from ..models import Class_Question

class Serializer_Class_Question(serializers.ModelSerializer):
    class Meta:
        model = Class_Question
        fields = '__all__'