from rest_framework import serializers
from ..models import Class_SubSection

class Serializer_Class_SubSection(serializers.ModelSerializer):
    class Meta:
        model = Class_SubSection
        fields = '__all__'