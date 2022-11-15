from django.http import FileResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

import os
import pandas as pd
from psycopg2 import connect
from environ import Env

from API.models import Clients
from API.serializers.ClientSerializer import ClientSerializer
from quick_django_api.settings import BASE_DIR


class ClientView(APIView):
    def get(self, request: Request, format=None) -> Response:
        client = Clients.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None) -> Response:
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailView(APIView):
    def get(self, request: Request, client_id: int, format=None) -> Response:
        client = get_object_or_404(Clients, pk=client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, client_id: int, format=None) -> Response:
        client = get_object_or_404(Clients, pk=client_id)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, client_id: int, format=None) -> Response:
        client = get_object_or_404(Clients, pk=client_id)
        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, client_id: int, format=None):
        client = get_object_or_404(Clients, pk=client_id)
        client.delete()
        return Response(
            {"status": "Deleted", "data": request.data}, status=status.HTTP_204_NO_CONTENT
        )


class ClientReportView(APIView):
    @property
    def db(self):
        env = Env()
        Env.read_env(os.path.join(BASE_DIR, '.env'))

        conn = connect(
            dbname=env('NAME_DB'),
            user=env("USER_DB"),
            password=env("PASSWORD_DB"),
            host=env("HOST_DB"),
            port=env("PORT_DB")
        )

        return conn

    def get_client_df(self, client_id: int) -> list:
        client = pd.read_sql(f'''
            SELECT
                id AS client_id,
                document,
                CONCAT(first_name, ' ',last_name) AS full_name
            FROM "API_clients"
            WHERE
                id = {client_id}
        ''', self.db)
        if client.empty:
            raise ValidationError({'error': 'There is not client to report'})

        return client

    def get_report_df(self, client_id: int) -> pd.DataFrame:
        report = pd.read_sql(f"""
            SELECT
                Ac.document,
                CONCAT(Ac.first_name, ' ',Ac.last_name) AS full_name,
                COUNT(Ap.id) AS number_related_bills
            FROM "API_bills" Ap
            INNER JOIN "API_clients" Ac
            ON Ac.id = Ap.client_id
            WHERE client_id={client_id}
            GROUP BY (Ac.document, Ac.first_name, Ac.last_name)
        """, self.db)

        if report.empty:
            raise ValidationError({'error': 'There are not enough data to report'})
        return report
    def get_bill_df(self, client_id: int) -> list:
        bill = pd.read_sql(f'''
            SELECT
                id AS bill_id,
                client_id
            FROM "API_bills"
            WHERE
                client_id = {client_id}
        ''', self.db)

        if bill.empty:
            raise ValidationError({'error': 'There are not bills to report'})

        return bill

    def get(self, request: Request, client_id: int, format=None) -> FileResponse:
        report_df = self.get_report_df(client_id)
        report_csv = report_df.to_csv(index=None)

        with open('test.cv', 'w+') as file:
            file.write(report_csv)

        return FileResponse(
            open('test.cv', 'rb'),
            as_attachment=True,
            filename=f'report_{report_df["document"][0]}.csv'
        )