# Generated by Django 3.2 on 2021-05-03 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20210503_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='total_cost',
            field=models.FloatField(blank=True, null=True),
        ),
    ]