from django.db import models

# Create your models here.
class Unit(models.Model):
    name = models.CharField(unique=True, max_length=50)
    to_SI_unit = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.name