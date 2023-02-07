from rest_framework import serializers
from .models import Outlet, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
        )

class OutletSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Outlet
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "outlet",
            "items",
        )