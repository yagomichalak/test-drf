from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Product API. """

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
