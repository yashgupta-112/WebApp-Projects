from rest_framework import serializers
from .models import saiyan

class saiyanSerializer(serializers.ModelSerializer):
    class Meta:
        model = saiyan
        fields ='__all__'