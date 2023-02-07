from django.db.models import Q

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Outlet, Item
from .serializers import OutletSerializer, ItemSerializer

from account.serializers import UserProfileSerializer
from restaurant.models import Order
from restaurant.serializers import OrderSerializer

# Create your views here.
@api_view(['GET'])
def getOutlets(response):
    outlets = Outlet.objects.all()
    serializer = OutletSerializer(outlets, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getItems(response):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def itemSearch(request):
    query = request.data.get('query', '')
    if query:
        items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(outlet__name__icontains=query))
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response({"items":[]})

@api_view(['POST'])
def outletSearch(request):
    query = request.data.get('query', '')
    if query:
        outlets = Outlet.objects.filter(Q(name__icontains=query))
        serializer = OutletSerializer(outlets, many=True)
        return Response(serializer.data)
    else:
        return Response({"outlets":[]})
    

def process(slugs):
    slugs = slugs.split('"')
    slugs.remove("[")
    slugs.remove(",]")
    slugs.remove(",")
    return slugs

class delete_all(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        for order in orders:
            order.delete()
        return Response(status=status.HTTP_200_OK)


class create_order(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, format=None):
        userSerializer = UserProfileSerializer(request.user)
        customerID = userSerializer.data["email"]
        outlet_slug = request.data.get('outlet', '')
        item_slugs = request.data.get('item', '')
        quantity_slugs = request.data.get('quantity', '')
        item_slugs = process(item_slugs)
        quantity_slugs = process(quantity_slugs)
        outlet = Outlet.objects.get(slug__icontains=outlet_slug)
        items=[]


        for item in item_slugs:
            items.append(Item.objects.get(Q(outlet=outlet) & Q(slug__icontains=item)))
        quantities = []
        for quantity in quantity_slugs:
            quantities.append(int(quantity))

        outlet = Outlet.objects.get(slug=outlet_slug)
        
        order = Order(outlet=outlet, quantities=quantities, customerID=customerID, ready = False)
        order.save()
        for item in items:
            order.items.add(item)
        order.save()
        
        serializer = OrderSerializer(order, many=False)

        if (len(items)!=0):
            return Response({"order": serializer.data})
        else:
            return Response({"outtlet": None})
        
class GetCustomerOrders(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, format=None):
        userSerializer = UserProfileSerializer(request.user)
        customerID = userSerializer.data["email"]
        orders = Order.objects.filter(customerID=customerID)

        serializer = OrderSerializer(orders, many=True)
        return Response({"orders":serializer.data})
