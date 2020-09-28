# from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer


# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('first_name')
    serializer_class = CategorySerializer