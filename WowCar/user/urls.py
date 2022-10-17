from django.urls import path

from .views import SignUpView, UserDetail

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('detail/<int:pk>', UserDetail.as_view(),name="user detail"),

]
