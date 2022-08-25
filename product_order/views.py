from django.shortcuts import render
from rest_framework import viewsets
from .models import ProductOrder
from .serializers import ProductOrderSerializer

class ProductOrderViewSet(viewsets.ModelViewSet):
    """ Viewset for the Product. """

    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']