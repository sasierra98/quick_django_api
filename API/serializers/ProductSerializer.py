from rest_framework import serializers

from API.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)
