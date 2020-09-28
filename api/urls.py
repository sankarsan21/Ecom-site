from django.conf.urls import url
from django.urls import include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    url('',home,name='api.home'),
    url('category/',include('api.category.urls')),


]