from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from API.models import Bills
from API.serializers import BillSerializer


class BillView(APIView):
    def get(self, request: Request, format=None) -> Response:
        bill = Bills.objects.all()
        serializer = BillSerializer(bill, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None) -> Response:
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillDetailView(APIView):
    def get(self, request: Request, bill_id: int, format=None) -> Response:
        bill = get_object_or_404(Bills, pk=bill_id)
        serializer = BillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, bill_id: int, format=None) -> Response:
        bill = get_object_or_404(Bills, pk=bill_id)
        serializer = BillSerializer(bill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, bill_id: int, format=None) -> Response:
        bill = get_object_or_404(Bills, pk=bill_id)
        serializer = BillSerializer(bill, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, bill_id: int, format=None):
        bill = get_object_or_404(Bills, pk=bill_id)
        bill.delete()
        return Response(
            {"status": "Deleted", "data": request.data}, status=status.HTTP_204_NO_CONTENT
        )
