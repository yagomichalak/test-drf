from django.db import models

# Create your models here.
class Category(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)
