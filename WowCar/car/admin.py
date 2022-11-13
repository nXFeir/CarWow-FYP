from django.contrib import admin
from .models import *

class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ['brand',]

class ModelAdmin(admin.ModelAdmin):
    model = Model
    list_display = ['id', 'brand', 'model_name']

class GenerationAdmin(admin.ModelAdmin):
    model = Generation
    list_display = ['model', 'generation_name', 'year_begin', 'year_end']

class VariantAdmin(admin.ModelAdmin):
    model = Variant
    list_display = ['generation', 'variant', 'transmission', 'fuel_type', 'body_type', 'image']

class CarSuggestionAdmin(admin.ModelAdmin):
    model = CarSuggestion
    list_display = ['id', 'brand', 'model_name', 'body_type']

    
admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Generation, GenerationAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(CarSuggestion, CarSuggestionAdmin)