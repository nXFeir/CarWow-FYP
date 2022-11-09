import django_filters.rest_framework
from django.shortcuts import render
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Comment, Review
from .serializers import *

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    ordering_fields = ['created_at']

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

class UserReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer 
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Review.objects.filter(reviewer=user)

@api_view(['GET'])
def get_reviews_by_car(request, pk):
    reviews = Review.objects.filter(car_model__id=pk).order_by('-created_at')
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
