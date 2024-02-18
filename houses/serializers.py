from rest_framework import serializers
from .models import house


class houseSerializer(serializers.ModelSerializer):
    class Meta:
        model = house
        fields = ('name', 'description' ,'price','images','owner','avaliable')