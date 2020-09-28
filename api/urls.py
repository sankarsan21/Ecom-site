from django.conf.urls import url
from django.urls import include, path
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('',home,name='api.home'),
    path('category/',include('api.category.urls')),


]