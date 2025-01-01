from rest_framework import serializers
from .models import Cost

class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = ['id', 'description', 'sum', 'user']
