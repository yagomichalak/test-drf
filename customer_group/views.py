from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomerGroup
from .serializers import CustomerGroupSerializer

class CustomerGroupViewSet(viewsets.ModelViewSet):
    """ Viewset for the CustomerGroup. """

    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']