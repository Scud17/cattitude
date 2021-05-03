# Generated by Django 3.2 on 2021-05-03 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_unit_to_si_unit'),
        ('products', '0002_product_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qty',
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='units.unit'),
        ),
    ]