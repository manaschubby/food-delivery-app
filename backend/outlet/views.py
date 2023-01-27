from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Item, Outlet
from .serializers import ItemSerializer, OutletSerializer

class OutletsList(APIView):
    def get(self, request, format=None):
        outlets = Outlet.objects.all()
        serializer = OutletSerializer(outlets, many=True)
        return Response(serializer.data)