from django.db import models

# Create your models here.
class CustomerGroup(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
