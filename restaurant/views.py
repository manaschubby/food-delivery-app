from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from account.serializers import UserProfileSerializer

from customer.models import Outlet

from .models import Order
from .serializers import OrderSerializer


# Create your views here.
class OrdersFetchView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, format=None):
        userSerializer = UserProfileSerializer(request.user)

        if (userSerializer.data['tc']==False):
            outlet_slug = request.data.get('outlet', '')
            outlet = Outlet.objects.get(slug=outlet_slug)
            orders = Order.objects.all().filter(outlet=outlet)
            
            serializer = OrderSerializer(orders, many=True)

            return Response({
                "orders": serializer.data
            })
        else:
            return Response({"errors": "No restaurant ID attached"})
        

class OrderReadyView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, format=None):
        userSerializer = UserProfileSerializer(request.user)

        if (userSerializer.data['tc']==False):
            outlet_slug = request.data.get('outlet', '')
            order_id = request.data.get('order', '')
            order = Order.objects.get(id=order_id)
            if (order.outlet.slug==outlet_slug):
                order.ready = True
                order.save()
                serializer = OrderSerializer(order)
                return Response({"messages":"success", "order":serializer.data})
            else:
                return Response({"errors":"Your outlet is not allowed to ready orders from some other outlet"})
        else:
            return Response({"errors": "No restaurant ID attached"})
        
class OrderDeleteView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, format=None):
        userSerializer = UserProfileSerializer(request.user)

        if (userSerializer.data['tc']==False):
            outlet_slug = request.data.get('outlet', '')
            order_id = request.data.get('order', '')
            order = Order.objects.get(id=order_id)
            if (order.outlet.slug==outlet_slug):
                order.delete()
                return Response({"msg":"Order completed and deleted succesfully"})
            else:
                return Response({"errors":"Your outlet is not allowed to delete orders from some other outlet"})
        else:
            return Response({"errors": "No restaurant ID attached"})