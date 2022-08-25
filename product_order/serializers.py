from rest_framework import serializers
from .models import ProductOrder

class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Product API. """

    class Meta:
        model = ProductOrder
        fields = ('id', 'customer', 'product', 'order_discount', 'total_price', 'order_date')
