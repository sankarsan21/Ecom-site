from rest_framework import routers
from django.urls import include, path
from . import views
# from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'',views.CategoryViewset)

urlpatterns = [
    path('',include(router.urls)),
]