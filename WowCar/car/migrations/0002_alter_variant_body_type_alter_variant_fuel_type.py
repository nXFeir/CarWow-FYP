# Generated by Django 4.0.4 on 2022-10-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='body_type',
            field=models.CharField(choices=[('SUV', 'SUV'), ('Sedan', 'SEDAN'), ('Hatchback', 'HATCHBACK'), ('Wagon', 'WAGON'), ('MPV', 'MPV'), ('Pickup Truck', 'PICKUP TRUCK'), ('Coupe', 'COUPE'), ('Convertible', 'CONVERTIBLE')], default='Sedan', max_length=15),
        ),
        migrations.AlterField(
            model_name='variant',
            name='fuel_type',
            field=models.CharField(choices=[('Petrol', 'PETROL'), ('Diesel', 'DIESEL'), ('Electric', 'ELECTRIC'), ('Hybrid', 'HYBRID')], default='Petrol', max_length=10),
        ),
    ]
