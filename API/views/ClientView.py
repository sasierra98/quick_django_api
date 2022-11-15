from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from API.models import Clients
from API.serializers.ClientSerializer import ClientSerializer


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
