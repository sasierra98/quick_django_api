from rest_framework import serializers
from rest_framework import fields

import pandas as pd

from API.models import Clients


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'document', 'type_document', 'first_name', 'last_name', 'email')
        read_only_fields = ('id',)


class UploadCreationClientSerializer(serializers.Serializer):
    upload_client = fields.FileField()

    def validate(self, attrs):
        csv = pd.read_csv(attrs['upload_client'])

        for csv_iter in csv.itertuples():
            Clients.objects.create(
                id=csv_iter.id,
                is_active=csv_iter.is_active,
                created_at=csv_iter.created_at,
                updated_at=csv_iter.updated_at,
                document=csv_iter.document,
                type_document=csv_iter.type_document,
                first_name=csv_iter.first_name,
                last_name=csv_iter.last_name,
                email=csv_iter.email
            )

        return attrs
