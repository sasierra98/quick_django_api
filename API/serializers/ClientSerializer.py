from rest_framework import serializers

from API.models import Clients


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'document', 'type_document', 'first_name', 'last_name', 'email')
        read_only_fields = ('id',)
