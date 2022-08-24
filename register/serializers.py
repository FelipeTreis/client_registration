from rest_framework import serializers

from register.models import Customer


class CustomerSerializer(serializers.Serializer):
    class Meta:
        model = Customer
        fields = (
            'full_name',
            'address',
            'phone',
        )
