from django.db import models
from units.models import Unit

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    store = models.CharField(max_length=120)
    cost = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default='1', blank=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}|{self.brand}"