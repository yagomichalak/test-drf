from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Product API. """

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'supplier', 'category')
