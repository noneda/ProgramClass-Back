from rest_framework import serializers
from ..models import Class_SubQuestion

class Serializer_Class_SubQuestion(serializers.ModelSerializer):
    class Meta:
        model = Class_SubQuestion
        fields = '__all__'