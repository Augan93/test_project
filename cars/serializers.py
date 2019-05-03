from rest_framework import serializers
from . import models


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = (
            'car_id',
            'color',
            'year',
            'manufacturer',
            'owner',
            'is_active',
        )
        read_only_fields = (
            'owner',
            'is_active',
        )

    def create(self, validated_data):
        request = self.context.get('request')
        return models.Car.objects.create(
            owner=request.user,
            **validated_data
        )
