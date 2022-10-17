from django.urls import path, include

from .views import *


urlpatterns = [
    path('', ReviewList.as_view(),name="List review"),
    path('detail/<int:pk>', ReviewDetail.as_view(),name="review detail"),
    path('car/<int:pk>', get_reviews_by_car,name="Get review by car"),
    path('reviewer/<int:pk>', get_reviews_by_reviewer,name="Get review by reviewer"),

    path('comment', CommentList.as_view(),name="Get comment"),
    path('comment/detail/<int:pk>', CommentDetail.as_view(),name="comment detail"),

]