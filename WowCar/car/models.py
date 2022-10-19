from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Brand(models.Model):
    brand = models.CharField(max_length=20)
    image = models.ImageField(upload_to='brand', blank=True, null=True) 

    def __str__(self):
        return str(self.brand)


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    model_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.brand} {self.model_name}'

    def get_gen_variant_list(self):
        data = []
        gens = self.generations.all()
        for gen in gens:
            variants = gen.get_variant_list()
            for variant in variants:
                if variant not in data:
                    data.append(variant)
        return data # ['Premium Spec', 'Premium+ Spec', 'E Spec', 'BLM +']

    def get_gen_fuel_type_list(self):
        data = []
        gens = self.generations.all()
        for gen in gens:
            fuels = gen.get_fuel_type_list()
            for fuel in fuels:
                if fuel not in data:
                    data.append(fuel)
        return data # ['PETROL', 'DIESEL', 'HYBRID']

    def get_gen_transmission_list(self):
        data = []
        gens = self.generations.all()
        for gen in gens:
            transmissions = gen.get_transmission_list()
            for transmission in transmissions:
                if transmission not in data:
                    data.append(transmission)
        return data # ['AUTOMATIC', 'ELECTRIC']
        
    def get_gen_body_type_list(self):
        data = []
        gens = self.generations.all()
        for gen in gens:
            bodies = gen.get_body_type_list()
            for body in bodies:
                if body not in data:
                    data.append(body)
        return data # ['Sedan', 'Hatchback', 'SUV']

def max_value_current_year(value):
    return MaxValueValidator(datetime.date.today().year)(value)

class Generation(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='generations')
    generation_name = models.CharField(max_length=50)
    year_begin = models.IntegerField(validators=[MinValueValidator(1950), max_value_current_year])
    year_end = models.IntegerField(validators=[MinValueValidator(1950), max_value_current_year])

    def __str__(self):
        return f'{self.model} {self.generation_name} [{self.year_begin}-{self.year_end}]'

    def get_variant_list(self):
        return list(self.variants.all().values_list('variant', flat=True))

    def get_fuel_type_list(self):
        variants = self.variants.all()
        return list(variants.values_list('fuel_type', flat=True).distinct('fuel_type'))

    def get_transmission_list(self):
        variants = self.variants.all()
        return list(variants.values_list('transmission', flat=True).distinct('transmission'))

    def get_body_type_list(self):
        variants = self.variants.all()
        return list(variants.values_list('body_type', flat=True).distinct('body_type'))
    
class Variant(models.Model):
    TRANSMISSION_CHOICES = (
        ('Manual', 'MANUAL'),
        ('Automatic', 'AUTOMATIC'),
        ('Electric', 'ELECTRIC')
    )
    FUEL_CHOICES = (
        ('Petrol', 'PETROL'),
        ('Diesel', 'DIESEL'),
        ('Electric', 'ELECTRIC'),
        ('Hybrid', 'HYBRID')
    )
    BODY_CHOICES = (
        ('SUV', 'SUV'),
        ('Sedan', 'SEDAN'),
        ('Hatchback', 'HATCHBACK'),
        ('Wagon', 'WAGON'),
        ('MPV', 'MPV'),
        ('Pickup Truck', 'PICKUP TRUCK'),
        ('Coupe', 'COUPE'),
        ('Convertible', 'CONVERTIBLE')
    )

    generation = models.ForeignKey(Generation, on_delete=models.CASCADE, related_name='variants')
    variant = models.CharField(max_length=50)
    transmission = models.CharField(choices=TRANSMISSION_CHOICES, default='Automatic', max_length=10)
    fuel_type = models.CharField(choices=FUEL_CHOICES, default='Petrol', max_length=10)
    body_type = models.CharField(choices=BODY_CHOICES, default='Sedan', max_length=15)
    
    def __str__(self):
        return f'{self.generation} {self.variant}'
