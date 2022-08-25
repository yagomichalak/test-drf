from django.db import models
from customer.models import Customer
from product.models import Product

# Create your models here.
class ProductOrder(models.Model):

    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order_discount = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    order_date = models.DateTimeField()

