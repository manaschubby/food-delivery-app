from django.db.models import Q
from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item, Outlet
from .serializers import ItemSerializer, OutletSerializer

class OutletsList(APIView):
    def get(self, request, format=None):
        outlets = Outlet.objects.all()
        serializer = OutletSerializer(outlets, many=True)
        return Response(serializer.data)

class ItemsList(APIView):
    def get_items_list(self, outlet_id):
        try:
            return Item.objects.filter(outlet_id=outlet_id)
        except Item.DoesNotExist:
            raise Http404 
        
    def get(self, request, outlet_slug, format=None):
        items = self.get_items_list(outlet_id=outlet_slug)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    if query:
        items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response({"products":[]})