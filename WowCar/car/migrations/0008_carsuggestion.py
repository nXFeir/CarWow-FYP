# Generated by Django 4.0.4 on 2022-11-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_remove_model_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarSuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('model_name', models.CharField(max_length=50)),
                ('transmission', models.CharField(choices=[('Manual', 'MANUAL'), ('Automatic', 'AUTOMATIC'), ('Electric', 'ELECTRIC')], default='Automatic', max_length=10)),
                ('fuel_type', models.CharField(choices=[('Petrol', 'PETROL'), ('Diesel', 'DIESEL'), ('Electric', 'ELECTRIC'), ('Hybrid', 'HYBRID')], default='Petrol', max_length=10)),
                ('body_type', models.CharField(choices=[('SUV', 'SUV'), ('Sedan', 'SEDAN'), ('Hatchback', 'HATCHBACK'), ('Wagon', 'WAGON'), ('MPV', 'MPV'), ('Pickup Truck', 'PICKUP TRUCK'), ('Coupe', 'COUPE'), ('Convertible', 'CONVERTIBLE')], default='Sedan', max_length=15)),
            ],
        ),
    ]
