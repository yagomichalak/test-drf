from rest_framework import serializers
from .models import CustomerGroup

class CustomerGroupSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the CustomerGroup API. """

    class Meta:
        model = CustomerGroup
        fields = ('id', 'name')
