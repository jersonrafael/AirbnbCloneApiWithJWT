from rest_framework import serializers
from .models import order

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ("house","startDate","endDate","client")