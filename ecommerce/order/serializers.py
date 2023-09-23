from rest_framework import serializers
from .models import Order, OrderItems
from dataclasses import field

class OrderItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    orderItems = serializers.SerializerMethodField(method_name='get_order_items', read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
    
    def get_order_items(self, obj):
        order_items = obj.orderitems.all()
        serializer = OrderItemsSerializer(order_items, many=True)
        return serializer.data