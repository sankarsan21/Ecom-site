from rest_framework import routers
from django.urls import include
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'',views.CategoryViewset)

urlpatterns = [
    url('',include(router.urls)),
]