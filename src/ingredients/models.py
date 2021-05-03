from django.db import models
from products.models import Product
from units.models import Unit

# Create your models here.
class Ingredient(models.Model):
    ingredient = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=1)
    ingredient_amount = models.FloatField(default=1.0)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return f"{self.ingredient.name} | {self.ingredient_amount} {self.ingredient_unit}"

    def get_absolute_url(self):
        return reverse("Ingredient_detail", kwargs={"pk": self.pk})