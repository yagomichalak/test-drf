from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Product API. """

    class Meta:
        model = Supplier
        fields = ('id', 'name', 'address', 'phone', 'email')
