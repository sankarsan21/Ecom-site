from rest_framework import routers
from django.urls import include, path
from . import views
# from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'',views.OrderViewset)

urlpatterns = [
    path('add/<str:id>/<str:token>',views.add , name='add'),
    path('',include(router.urls))
]