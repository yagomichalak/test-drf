from django.db import models
from customer_group.models import CustomerGroup

# Create your models here.
class Customer(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    group = models.ForeignKey(CustomerGroup, on_delete=models.DO_NOTHING)
