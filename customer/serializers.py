from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Customer API. """

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'address', 'phone', 'email', 'group')
