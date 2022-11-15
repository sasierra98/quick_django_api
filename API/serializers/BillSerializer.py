from rest_framework import serializers

from API.models import Bills


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ('id', 'client', 'company_name', 'nit', 'code', 'products')
        read_only_fields = ('id',)
