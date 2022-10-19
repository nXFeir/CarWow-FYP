from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import User
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]