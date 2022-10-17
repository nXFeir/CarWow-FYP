from django.shortcuts import render

from .models import Review, Comment
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
import django_filters.rest_framework
from rest_framework import filters


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    ordering_fields = ['created_at']

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

@api_view(['GET'])
def get_reviews_by_car(request, pk):
    reviews = Review.objects.filter(car_model__id=pk)
    return Response(ReviewSerializer(reviews, many=True).data)

@api_view(['GET'])
def get_reviews_by_reviewer(request, pk):
    reviews = Review.objects.filter(reviewer=pk)
    return Response(ReviewSerializer(reviews, many=True).data)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    ordering_fields = ['created_at']

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer