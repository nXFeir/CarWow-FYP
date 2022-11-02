from rest_framework import serializers

from .models import *


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.brand')
    variant = serializers.SerializerMethodField()
    body_type = serializers.SerializerMethodField()
    fuel_type = serializers.SerializerMethodField()
    transmission = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Model
        fields = ['id' ,'brand', 'model_name', 'variant', 'body_type', 'fuel_type', 'transmission', 'image', 'reviews']

    def get_variant(self, obj):
        return obj.get_gen_variant_list()

    def get_body_type(self, obj):
        return obj.get_gen_body_type_list()

    def get_fuel_type(self, obj):
        return obj.get_gen_fuel_type_list()

    def get_transmission(self, obj):
        return obj.get_gen_transmission_list()

    def get_image(self, obj):
        var = Variant.objects.filter(generation__model=obj, image__isnull=False).first()
        if var:
            return var.image
        return None
        