# Generated by Django 3.2 on 2021-05-03 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ingredients.ingredient'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
