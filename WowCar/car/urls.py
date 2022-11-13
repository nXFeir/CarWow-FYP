from django.urls import path, include

from .views import *

urlpatterns = [
    path('brand/', BrandList.as_view(),name="Get All Brand"),
    path('brand/<int:brand_id>', ModelsByBrandList.as_view(),name="Get Cars by brand"),
    path('model/<int:pk>', CarModelView.as_view(),name="Get Model"),
    path('model/', ModelList.as_view(),name="Get All Model"),
    path('model/review', get_cars_by_review,name="Get All Model by review"),
    path('model/suggest', CarSuggestionView.as_view(),name="Suggest Car"),

]
