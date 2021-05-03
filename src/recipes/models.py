from django.db import models
from ingredients.models import Ingredient

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(unique=True, max_length=120)
    ingredients = models.ManyToManyField(Ingredient)
    total_cost = models.FloatField(null=True, blank=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Recipe_detail", kwargs={"pk": self.pk})
