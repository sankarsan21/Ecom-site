from django.conf.urls import url
from django.urls import include, path
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('',home,name='api.home'),
    path('category/',include('api.category.urls')),
    path('product/',include('api.product.urls')),
    path('user/',include('api.user.urls')),
    path('order/',include('api.order.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-auth-token'),

]