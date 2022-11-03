from rest_framework import serializers
from .models import RateData

class RateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateData
        fields = "__all__"