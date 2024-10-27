from rest_framework import serializers
from ..models.Class import Class_Main

class Serializer_Class_Main(serializers.ModelSerializer):
    class Meta:
        model = Class_Main
        fields =  [
            'id', 'title', 'text', 'type'
        ]