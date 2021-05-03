# Generated by Django 3.2 on 2021-05-03 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('brand', models.CharField(max_length=120)),
                ('store', models.CharField(max_length=120)),
                ('cost', models.FloatField()),
                ('qty', models.FloatField(default=1.0)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]