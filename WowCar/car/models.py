from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Brand(models.Model):
    brand = models.CharField(max_length=20)

    def __str__(self):
        return str(self.brand)


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    model_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.brand} {self.model}'


def max_value_current_year(value):
    return MaxValueValidator(datetime.date.today().year)(value)

class Generation(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='generations')
    generation_name = models.CharField(max_length=50)
    year_begin = models.IntegerField(validators=[MinValueValidator(1950), max_value_current_year])
    year_end = models.IntegerField(validators=[MinValueValidator(1950), max_value_current_year])

    def __str__(self):
        return f'{self.model} {self.generation} [{self.year_begin}-{self.year_end}]'

    
class Variant(models.Model):
    TRANSMISSION_CHOICES = (
        ('Manual', 'MANUAL'),
        ('Automatic', 'AUTOMATIC'),
        ('Electric', 'ELECTRIC')
    )
    FUEL_CHOICES = (
        ('Petrol', 'PETROL'),
        ('Diesel', 'DIESEL'),
        ('Electric', 'ELECTRIC')
    )
    BODY_CHOICES = (
        ('SUV', 'SUV'),
        ('Sedan', 'SEDAN'),
        ('Hatchback', 'HATCHBACK'),
        ('Wagon', 'WAGON'),
        ('MPV', 'MPV'),
    )

    generation = models.ForeignKey(Generation, on_delete=models.CASCADE, related_name='variants')
    variant = models.CharField(max_length=50)
    transmission = models.CharField(choices=TRANSMISSION_CHOICES, default='Automatic', max_length=10)
    fuel_type = models.CharField(choices=FUEL_CHOICES, default='Petrol', max_length=10)
    body_type = models.CharField(choices=BODY_CHOICES, default='Sedan', max_length=10)
    
    def __str__(self):
        return f'{self.generation} {self.variant}'
