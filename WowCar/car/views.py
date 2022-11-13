import django_filters.rest_framework
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = CarBrandSerializer
    filter_backends = [filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    ordering_fields = ['brand']


class ModelsByBrandList(generics.ListAPIView):
    serializer_class = CarModelSerializer
    filter_backends = [filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    ordering_fields = ['generations__year_begin', 'model_name', 'brand__brand']

    def get_queryset(self):
        brand = get_object_or_404(Brand, id=self.kwargs['brand_id'])
        return Model.objects.filter(brand=brand)


class ModelList(generics.ListAPIView):
    queryset = Model.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = [filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    ordering_fields = ['generations__year_begin', 'model_name', 'brand__brand']
    search_fields = ['brand__brand', 'model_name', 'generations__variants__body_type', 'generations__variants__fuel_type','generations__variants__transmission']


class CarModelView(generics.RetrieveAPIView):
    queryset = Model.objects.all()
    serializer_class = CarModelSerializer

@api_view(['GET'])
def get_cars_by_review(request):
    cars = Model.objects.all().annotate(review_count=Count('reviews')).order_by('-review_count')
    return Response(CarModelSerializer(cars, many=True).data)


class CarSuggestionView(generics.CreateAPIView):
    queryset = CarSuggestion.objects.all()
    serializer_class = CarSuggestionSerializer
