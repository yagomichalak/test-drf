from django.shortcuts import render
from rest_framework import viewsets
from .models import Supplier
from .serializers import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    """ Viewset for the Product. """

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']